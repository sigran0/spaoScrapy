#-*- coding: utf-8 -*-

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import
from time import sleep
from BeautifulSoup import BeautifulSoup

class PageSpider(scrapy.Spider):

    name = 'page'

    start_urls = [
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300159'
    ]

    driver = webdriver.PhantomJS(executable_path=r'D:/dev/workspace/python/spaScrapy/venv/util/phantomjs.exe')

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def parse(self, res):

        self.driver.get('http://spao.elandmall.com/dispctg/initDispCtg.action?page_idx=mall_no=0000037&sort=2&category_1depth=&color_info=&category_2depth=1607300159&deliCostFreeYn=&applyEndDate=&vend_no=&dispStartDate=&newGoodsStartDate=&min_price=&category_4depth=&srchFd=null&category_3depth=&setDicountYn=&applyStartDate=&_=1493112823844&brand_no=&category_5depth=null&category_6depth=null&kwd=&listType=image&giftYn=&pageSize=999&newGoodsEndDate=&reSrch=&disp_ctg_no=1607300159&size_info=&oneMoreYn=&dispEndDate=&listOnly=Y&discountYn=&max_price=&material_info=')
"""
        numbers = self.driver.find_elements_by_css_selector('div#page_idx > span.num > a')
        number_names = []
        number_params = []

        for number in numbers:
            number_names.append(number.text)
            number_params.append(number.get_attribute('parameters'))

        print number_params
"""
        page_source = self.driver.page_source
        bs_object = BeautifulSoup(page_source)

        lists = bs_object.find(id='goodsList').findAll('ul', {'class': 'list'})

        for list in lists:

            products = list.findAll('li')

            for product in products:

                name = product.find('span', {'class': 'prod_nm'})
                print name.text