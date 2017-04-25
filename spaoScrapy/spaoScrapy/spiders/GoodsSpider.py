import scrapy
import re
from ..items import PageItem
from ..pipelines import SpaoscrapyPipeline
from BeautifulSoup import BeautifulSoup

class PageSpider(scrapy.Spider):

    name = 'page'
    url = ''

    start_urls = [
        'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1704316476&pageSize=1000&listOnly=Y&color_info='
    ]

    def parse(self, res):
        pass