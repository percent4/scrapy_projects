import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ['http://www.runoob.com/git/git-tutorial.html',]

    def parse(self,response):
        with open('/home/vagrant/python.txt', 'w') as f:
            for i in range(1,12):
                text = response.xpath('//*[@id="leftcolumn"]/a[%d]/text()'%i).extract()[0].strip('\n').strip('\t')
                print(type(text))
                f.write(text+'\n')
