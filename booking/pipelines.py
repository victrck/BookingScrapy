# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb 
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import json

class BookingPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect(host="localhost", user="root", passwd="sckk", db="booking",charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		i = 0;
		try:
			self.cursor.execute("INSERT INTO fortaleza(nome_hotel,notaMediaTotal_hotel,notaLimpeza_hotel,notaConforto_hotel,notaLocalizacao_hotel,notaComodidade_hotel,notaFuncionarios_hotel,notaCustoBeneficio_hotel,notaWifi_hotel, usuario, data_avaliacao, quant_avaliacoes,pais_usuario, nota, titulo_comentario, tag_1, tag_2, tag_3, tag_4, tag_5, comentario_pos, comentario_neg, periodo_hospedagem) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (item['nome_hotel'],item['notaMediaTotal_hotel'],item['notaLimpeza_hotel'],item['notaConforto_hotel'],item['notaLocalizacao_hotel'],item['notaComodidade_hotel'],item['notaFuncionarios_hotel'],item['notaCustoBeneficio_hotel'],item['notaWifi_hotel'], item['usuario'], item['data_avaliacao'], item['quant_avaliacoes'], item['pais_usuario'], item['nota'], item['titulo_comentario'], item['tag_1'], item['tag_2'], item['tag_3'], item['tag_4'], item['tag_5'], item['comentario_pos'], item['comentario_neg'], item['periodo_hospedagem'])) 
			self.conn.commit()	
		except MySQLdb.Error as e:
			print (e)
		return item
class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item