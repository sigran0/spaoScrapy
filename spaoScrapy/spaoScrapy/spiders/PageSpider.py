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

        self.driver.get(res.url)

        numbers = self.driver.find_elements_by_css_selector('div#page_idx > span.num > a')

        for number in numbers:
            self.driver.implicitly_wait(3)
            print number.text
            number.click()

            print 'clicked'

            try:
                self.driver.implicitly_wait(3)
            except TimeoutException as ex:
                print('Exception has been thrown. ' + str(ex))
                self.driver.close()
            finally:
                page_source = self.driver.page_source
                bs_object = BeautifulSoup(page_source)

                lists = bs_object.find(id='goodsList').findAll('ul', {'class': 'list'})

                for list in lists:

                    products = list.findAll('li')

                    for product in products:

                        name = product.find('span', {'class': 'prod_nm'})
                        print name.text