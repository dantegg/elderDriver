import scrapy
import urllib
import re

class oldDriverSpider(scrapy.Spider):
    name = 'elderDriver'
    allowed_domains = ['rosiok.com']
    start_urls=[
        "http://www.rosiok.com/shipin/",
        "http://www.rosiok.com/sishu/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        pattern = re.compile(r'http\:\/\/tu.')
        tempArray = []
        for sel in response.xpath('//img'):
            #print sel.xpath('@src').extract()
            imagePath = sel.xpath('@src').extract()
            getimage = imagePath[0]
            repath = pattern.match(getimage)
            if repath:
                tempArray.append(getimage)

        print tempArray

        print 'get '+str(len(tempArray))+ ' images'

        # savePattern = re.compile(r'http\:\/\/.')

        for index in range(len(tempArray)):
            print tempArray[index]
            print tempArray[index][7:]
            saveName = tempArray[index][7:]
            saveName = saveName.replace('/','.')
            # saveName = savePattern.match(tempArray[index])
            # #print saveName
            urllib.urlretrieve(tempArray[index],'./pictures/'+saveName)
            # print getimage

            # print repath.group(0)
            # try:
            #     urllib.urlretrieve(getimage,'./pictures/'+getimage)
            # finally:
            #     print 'hhh===='
