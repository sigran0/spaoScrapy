import scrapy


class CategorySpider(scrapy.Spider):

    name = "category"

    start_urls = [
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300073'   #   Men
    ]

    def parse(self, res):
        upper_categories = res.css('div.lnb_cate01 > ul > li')

        print 'print data'
        for upper_category in upper_categories:
            upper_category_title = upper_category.xpath('@data-ga-tag').extract()[0][9:]

            lower_categories = res.css('div.depth2 > ul > li')

            for lower_category in lower_categories:
                lower_category_title = lower_category.xpath('@data-ga-tag').extract()[0][9:]
                print upper_category_title, ' > ', lower_category_title