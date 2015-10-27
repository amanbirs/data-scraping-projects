# din't work, so I ran the Lua script from Splash directly and manually saved the result in 3 html files
import json
import scrapy
import scrapyjs
import base64
from nsdc_calender.items import NsdcCalenderItem


class calenderSpider(scrapy.Spider):
    name = "nsdc_cal"
    start_urls = [
        "http://c20cp2.saas.talismaonline.com/PTCalender.aspx"
    ]


    def start_requests(self):
        script = """
            nsdc_html = ""
            
            splash:go("http://c20cp2.saas.talismaonline.com/PTCalender.aspx")
            
            for i = 1,20,1 do
                field="document.getElementById('ddlSector').selectedIndex="..i ..";"
                splash:runjs(field)
                splash:runjs("document.getElementById('ddState').selectedIndex=1;")
                
                splash:runjs("getDistrict();")
                splash:runjs("getData();")
                
                nsdc_html = nsdc_html..splash:html()
            end
            
            return {
                nsdc_html
            }
        """

        for url in self.start_urls:
            yield scrapy.Request(url, self.parse,meta={
                'splash': {
                    'args': {'lua_source': script},
                    'endpoint': 'execute',
                }
            })


    def parse(self, response):
        filename = 'nsdccal.html'
        with open(filename, 'wb') as f: 
            f.write(response.body)


        #for i in range(1,48):
            #body.response = nsdc_html[i]
            #item = NsdcCalenderItem()
            #item['course_name'] = response.xpath("//*[@id='divData']/div/div/table/tbody/tr[*]/td[1]/text()'").extract()
            #item['course_fees'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[2]/text()').extract()
            #item['trained_for_job_role'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[3]/text()').extract()
            #item['course_duration_days'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[5]/text()').extract()
            #item['batch_startdate'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[6]/text()').extract()
            #item['batch_enddate'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[6]/text()').extract()
            #item['training_centre_name'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[7]/text()').extract()
            #item['training_centre_address'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[8]/text()').extract()
            #item['contact_name'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[9]/text()').extract()
            #item['contact_email'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[10]/text()').extract()
            #item['contact_mobile'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[11]/text()').extract()
            #item['training_provider_name'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[12]/text()').extract()
            #item['state'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[13]/text()').extract()
            #item['district'] = response.xpath('//*[@id="divData"]/div/div/table/tbody/tr[*]/td[14]/text()').extract()
            #item['sector'] = response.xpath('//*[@id="divSector"]/text()').extract()
        #yield item


        #filename = 'nsdccal.html'
        #with open(filename, 'wb') as f: 
        #    f.write(response.body)



