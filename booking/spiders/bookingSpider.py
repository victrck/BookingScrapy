import scrapy
import re
from scrapy.selector import Selector
from scrapy.http import Request,Response
from booking.items import BookingItem

class bookingSpider(scrapy.Spider):
	name = "booking"
	start_urls = [
		"https://www.booking.com/reviews/br/city/fortaleza.pt-br.html?aid=376377;label=booking-name-pt-row-bwMffLz%2AfdB8PTKNsC9tlgS267778091914%3Apl%3Ata%3Ap1%3Ap22%2C189%2C000%3Aac%3Aap1t1%3Aneg%3Afi%3Atikwd-65526620%3Alp1001629%3Ali%3Adec%3Adm;sid=8ddcf94ea1a265dbd5362acc96e7ba1a"
	]


	#Variáveis que são uteis na formação de outros links
	def __init__(self):
		self.avaliacao = "https://www.booking.com/reviews/br/hotel/"
		self.base_url = "https://www.booking.com/"
		
	#Primeira chamada, coleta primeira lista de links de celulares e avança pra próxima página
	def parse(self, response):
		sel = Selector(response)

		hoteis = sel.xpath("//*[@id='b2reviews_cityPage']/div[4]/div[4]/div[1]/div/div[2]/ul[1]/li/div/div[1]/ul/li[4]/a/@href").extract()
		for hotel in hoteis:
			half = hotel.split('/')[-1]
			url = self.avaliacao + half
			 
			new_request = Request(url, callback=self.parse_phone)
			yield new_request

		next_page = sel.xpath("//*[@id='b2reviews_cityPage']/div[4]/div[4]/div[1]/div/div[2]/ul[2]/li[7]/a/@href").extract()[0]
		next_page = self.base_url + next_page
		new_new_request = Request(next_page, callback=self.parse)
		yield new_new_request



	def parse_phone(self,response):
		sel = Selector(response)

		try:
			nome_hotel = sel.xpath("//*[@id='standalone_reviews_hotel_info_wrapper']/div[1]/h1/a/text()").extract()[0]
		except:
			nome_hotel = " "
		try:
			notaMediaTotal_hotel = sel.xpath("//*[@id='review_list_score']/span/span/text()").extract()[0]
		except:
			notaMediaTotal_hotel = " "
		try:
			notaLimpeza_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_clean']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaLimpeza_hotel = " "
		try:
			notaConforto_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_comfort']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaConforto_hotel = " "
		try:
			notaLocalizacao_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_location']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaLocalizacao_hotel = " "
		try:
			notaComodidade_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_services']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaComodidade_hotel = " "
		try:
			notaFuncionarios_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_staff']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaFuncionarios_hotel = " "
		try:
			notaCustoBeneficio_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_value']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaCustoBeneficio_hotel = " "
		try:
			notaWifi_hotel = sel.xpath("//*[@id='review_list_score_breakdown']/li[@data-question='hotel_wifi']/p[@class='review_score_value']/text()").extract()[0]
		except:
			notaWifi_hotel = " "
		
		for id in range(75):
			item = BookingItem()
			item['nome_hotel'] = nome_hotel
			item['notaMediaTotal_hotel'] = notaMediaTotal_hotel
			item['notaLimpeza_hotel'] = notaLimpeza_hotel
			item['notaConforto_hotel'] = notaConforto_hotel
			item['notaLocalizacao_hotel'] = notaLocalizacao_hotel
			item['notaComodidade_hotel'] = notaComodidade_hotel
			item['notaFuncionarios_hotel'] = notaFuncionarios_hotel
			item['notaCustoBeneficio_hotel'] = notaCustoBeneficio_hotel
			item['notaWifi_hotel'] = notaWifi_hotel
			# item['usuario'] = usuario[id]
			number = id + 1
			aux = str(number)
			try:
				item['usuario'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[2]/p/span/text()").extract()[0]
				 
			except:
				item['usuario'] = " "
				 
			try:
				item['data_avaliacao'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/p/text()").extract()[0]
				 
			except:
				item['data_avaliacao'] = " "
				 
			try:
				item['quant_avaliacoes'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[2]/div[3]/text()").extract()[0]
				 
			except:
				item['quant_avaliacoes'] = " "
				 
			try:
				item['pais_usuario'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[2]/span/span[2]/span/text()").extract()[0]
				 
			except:
				item['pais_usuario'] = " "
				 
			try:
				item['nota'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/div[1]/div[1]/span/span/text()").extract()[0]
				 
			except:
				item['nota'] = " "
				 
			try:
				item['titulo_comentario'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/div[1]/div[2]/div/span/text()").extract()[0]
				 
			except:
				item['titulo_comentario'] = " "
				 
			try:
				item['tag_1'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/ul[@class='review_item_info_tags']/li[1]/text()").extract()[1]
				 
			except:
				item['tag_1'] = " "	
				 
			try:
				item['tag_2'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/ul[@class='review_item_info_tags']/li[2]/text()").extract()[1]
				 
			except:
				item['tag_2'] = " "
				 
			try:
				item['tag_3'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/ul[@class='review_item_info_tags']/li[3]/text()").extract()[1]
				 
			except:
				item['tag_3'] = " "
				 
			try:
				item['tag_4'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/ul[@class='review_item_info_tags']/li[4]/text()").extract()[1]
				 
			except:
				item['tag_4'] = " "
				 
			try:
				item['tag_5'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/ul[@class='review_item_info_tags']/li[5]/text()").extract()[1]
				 
			except:
				item['tag_5'] = " "
				 
			try:
				item['comentario_pos'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/div[2]/p[@class='review_pos ']/span/text()").extract()[0]
				 
			except:
				item['comentario_pos'] = " "
				 
			try:
				item['comentario_neg'] = sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/div[2]/p[@class='review_neg ']/span/text()").extract()[0]
				 
			except:
				item['comentario_neg'] = " "
				 
			try:
				item['periodo_hospedagem']= sel.xpath("//*[@id='review_list_page_container']/ul/li["+ aux +"]/div[3]/div/div[@class='review_item_review_content']/p[@class='review_staydate ']/text()").extract()[0]
				 
			except:
				item['periodo_hospedagem'] = " "
				 
			yield item

		next_url = sel.xpath("//*[@id='review_next_page_link']/@href").extract()[0]
		next_url_full = self.base_url+next_url
		next_request = Request(next_url_full, callback=self.parse_phone)
		yield next_request
