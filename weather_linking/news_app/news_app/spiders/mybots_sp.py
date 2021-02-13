# from scrapy_news.items import MulticampusModuleprjItem_sp
# import scrapy
# from scrapy.http import Request
# import requests


# URL_SP = 'https://news.joins.com/sports?page=%s'

# start_page = 1



# class MybotsSpider(scrapy.Spider):
#     name = 'mybots_sp'
#     allowed_domains = ['naver.com']
#     start_urls = [URL_SP%start_page]
#     # print("------------------->", start_urls)
#     def start_requests(self):
#         # print("chk1----------------------------------")
#         for i in range(7):
#             yield Request(url=URL_SP%(i+start_page), callback=self.parse)

#     def parse (self,response):
#         # test = response.xpath('').extract()
#         previews = response.xpath('//*[@id="content"]/div[3]/ul/li/span[2]/a/text()').extract()
#         times = response.css('.byline::text').extract()
#         titles = response.xpath('//*[@id="content"]/div[3]/ul/li/h2/a/text()').extract() 
#         # titles_npic = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt/a/text()').extract()

#         print("-------------->", previews)
     
#         # print("-------------->", previews)
        
#         items = []
        
       
#         for idx in range(len(titles)):
#             item = MulticampusModuleprjItem_sp()
#             item['preview'] = previews[idx]
#             item['time'] = times[idx]
#             # item['title_npic'] = titles_npic[idx]
#             item['title'] = titles[idx]

            

#             items.append(item)
#         # print("--------------2>", items)
#         return items
