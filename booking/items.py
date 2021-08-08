# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
	nome_hotel = scrapy.Field()
	notaMediaTotal_hotel = scrapy.Field()
	notaLimpeza_hotel = scrapy.Field()
	notaConforto_hotel = scrapy.Field()
	notaLocalizacao_hotel = scrapy.Field()
	notaComodidade_hotel = scrapy.Field()
	notaFuncionarios_hotel = scrapy.Field()
	notaCustoBeneficio_hotel = scrapy.Field()
	notaWifi_hotel = scrapy.Field()
	usuario = scrapy.Field()
	data_avaliacao = scrapy.Field()
	quant_avaliacoes = scrapy.Field()
	pais_usuario = scrapy.Field()
	nota = scrapy.Field()
	titulo_comentario = scrapy.Field()
	tag_1 = scrapy.Field()
	tag_2 = scrapy.Field()
	tag_3 = scrapy.Field()
	tag_4 = scrapy.Field()
	tag_5 = scrapy.Field()
	comentario_pos = scrapy.Field()
	comentario_neg = scrapy.Field()
	periodo_hospedagem = scrapy.Field()
