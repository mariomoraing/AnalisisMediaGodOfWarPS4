# -*- coding: utf-8 -*-
import scrapy


class GowbotSpider(scrapy.Spider):
    name = 'gowbot'
    allowed_domains = ['www.metacritic.com/game/playstation-4/god-of-war/critic-reviews']
    start_urls = ['http://www.metacritic.com/game/playstation-4/god-of-war/critic-reviews/']

    def parse(self, response):

    	notas = response.css(".metascore_w::text").extract()
    	notas_depuradas = notas[:-4]

    	for item in zip(notas_depuradas):
    		scrapped_notas = {
    			'GOW_Notas' : item[0],
    		}
    		yield scrapped_notas
        
