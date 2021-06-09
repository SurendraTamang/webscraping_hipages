import scrapy
import  re
import string

class HipagesSpiderSpider(scrapy.Spider):
    name = 'hipages_spider'
    allowed_domains = ['hipages.com.au']
    start_urls = ['https://hipages.com.au/trade_business_names/'+letter for letter in string.ascii_uppercase]

    def parse(self, response):
        list_of_links = response.xpath('//li/a/@href').extract()
        links = ['https://hipages.com.au'+ a for a in list_of_links if '/connect/' in a]
        for link in links:
            yield  scrapy.Request(url=link, callback=self.get_details)

    def get_details(self, response):
        website = self.extract_first(re.compile('"website":"(.*?)"').findall(response.text.replace('\\','')))
        business_name = response.xpath("//h4/text()").extract_first()

        address = self.extract_first(re.compile('"address":"(.*?)"').findall(response.text.replace('\\','')))
        phone = self.extract_first(re.compile('"phone":"(.*?)"').findall(response.text.replace('\\','')))
        fax = self.extract_first(re.compile('"fax":"(.*?)"').findall(response.text.replace('\\','')))
        mobile = self.extract_first(re.compile('"mobile":"(.*?)"').findall(response.text.replace('\\','')))
        full_service_categories = response.xpath('//div/h4[contains(text(),"Service Categories")]/following-sibling::div//li/p/text()').extract()
        yield {
            'website':website,
            'business_name':business_name,
            'address':address,
            'phone':phone,
            'fax':fax,
            'mobile':mobile,
            'full_service_categories':full_service_categories
        }

    def extract_first(self, value):
        try:
            ans = value[0]
        except IndexError:
            ans = ''
        return  ans