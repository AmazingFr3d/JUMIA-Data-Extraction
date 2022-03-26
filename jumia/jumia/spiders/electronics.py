# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['www.jumia.com.ng']
    start_urls = ['https://www.jumia.com.ng/computing']

    def parse(self, response):
        for product in response.xpath("//div[@class='-paxs row _no-g _4cl-3cm-shs']/article[@class='prd _fb col c-prd']/a"):
            yield{
                'name': product.xpath(".//div[2]/h3/text()").get(),
                'url': response.urljoin(product.xpath(".//@href").get()),
                'price': product.xpath(".//div[@class='info']/div[@class='prc']/text()").get()
            }
        next_page = response.urljoin(response.xpath("//a[@aria-label='Next Page']/@href").get())
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

