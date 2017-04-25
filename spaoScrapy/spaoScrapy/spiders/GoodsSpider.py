#-*- coding: utf-8 -*-

import scrapy
import re
from ..items import GoodsItem
from ..pipelines import SpaoscrapyPipeline
from BeautifulSoup import BeautifulSoup


class GoodsSpider(scrapy.Spider):

    name = 'goods'
    """
        이 패이지들에서 문제 있음
        http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1611077200 
        http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1701118952
        
        bs_object를 만드는것 까진 되나, find 과정에서 None Object를 return한다.
        
        왜지?!
    """
    start_urls = [
        'http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1701118952'
    ]

    def parse(self, res):
        errors = {
            1611077200: True,
            1701118952: True
        }

        pipeline = SpaoscrapyPipeline()

        #   product_code를 regex로 찾아오기
        product_code = re.findall(r'[0-9]{6,15}', res.url)[0]

        if errors.has_key(int(str(product_code))) is False:
            page = pipeline.get_page_by_no(product_code)

            if page is None:
                print 'Page Is None!'
                return

            product_name = page['goods_title']
            original_price = page['goods_original_price']
            discount_price = page['goods_sale_price']
            product_category = page['category']
            product_fabric = None
            product_color = None
            product_thumbnail_images = []
            product_url = res.url

            bs_object = BeautifulSoup(res.body)

            tables = bs_object.find('div', {'class': 'data_table01'}).findAll('th')

            print product_name

            """
                Table의 경우 
                http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1610064534 형식과
                http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1608008679 형식이 존재한다.
                내가 파악하지 못한 형태의 table이 있을 경우도 있으므로,
                table을 전체 검색 후 필요한 정보인 색상과 소재를 뽑아내자
            """

            for table in tables:
                if table.text.find(u"소재") != -1:
                    product_fabric = table.findNextSibling('td').text
                if table.text.find(u'색상') != -1:
                    product_color = [_str.strip() for _str in table.findNextSibling('td').text.split(',')]

            """
                Image 영역 추출
            """
            images = bs_object.find('div', {'class': 'dt_ve_thumnail'}).findAll('img')

            for image in images:
                product_thumbnail_images.append(image['src'][2:])

            item = GoodsItem()
            item['product_code'] = product_code
            item['product_name'] = product_name
            item['product_category'] = product_category
            item['product_color'] = product_color
            item['original_price'] = original_price
            item['discount_price'] = discount_price
            item['product_thumbnail_images'] = product_thumbnail_images
            item['product_url'] = product_url
            item['product_fabric'] = product_fabric

            """
                저장
            """
            pipeline.store_product(item)

        """
            다음 아이탬을 찾으러 떠난다
        """

        pipeline.set_crawled_page(product_code)
        next_product = pipeline.get_uncrawled_page()

        if next_product is not None:
            next_product_no = next_product['goods_no']
            url = 'http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=%d'%(next_product_no)

            request = scrapy.Request(url=url)
            yield request