import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from multiprocessing import Process



#This is my crawler
class spider(scrapy.Spider):
    name = 'body'
    start_urls = [
        'https://en.wikipedia.org/wiki/Main_Page',
    ]
    base_url = 'https://en.wikipedia.org'
    rules = [Rule(LinkExtractor(), callback='parse', follow=True)]
    #MAX_PAGES = 12
    custom_settings = {
        'DEPTH_LIMIT': 3,
        #'CLOSESPIDER_PAGECOUNT': MAX_PAGES
    }
    seen = set('https://en.wikipedia.org/wiki/Main_Page')
    
    def start_requests (self):
        yield scrapy.Request('https://en.wikipedia.org/wiki/Main_Page')
    
    #Crawler parser
    def parse(self, response):
        MAX_PAGES = 5
        res  = []
        for body in response.selector.xpath('//body//text()[not (ancestor-or-self::script or ancestor-or-self::noscript or ancestor-or-self::style)][re:test(., "\w+")]'):
            res.append(body.extract())
        yield {
                'body': ' '.join(res),
            }
        links = []
        counter = 0

        #checks to make sure that the links we are about to follow have not been visited yet
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            if url not in links and url not in spider.seen and counter < MAX_PAGES:
                links.append(url)
                spider.seen.add(url)
                counter+=1
        print("---------------- URL Links HERE ---------")
        print(links)
        for next_page in links:
            yield response.follow(next_page, callback= self.parse)
            #MAX_PAGES-=1

#These functions allow me to run the crawler in another python script instead of terminal          
def func():
    proc = CrawlerProcess(settings={
        'FEED_URI': 'wikibody.json',
        'FEED_FORMAT': 'json'
    })
    proc.crawl(spider)
    proc.start()
    proc.join()
def runSpider():
    process = Process(target=func)
    process.start()
    process.join()
    return process
if __name__ == '__main__': 
    func()


# IGNORE
        #next_page = response.css('.next a').attrib['href']
        #if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)

        #Get links to follow
        #do a double loop based on width and length, and keep calling back
        #print("here")

        #next_page = LinkExtractor(restrict_css='.next a').extract_links(response)[0]
        #if next_page.url is not None:
        #    yield response.follow(next_page, callback=self.parse)
        #for href in response.css('.next a::attr("href")'):
        #    print("HERE")
        #    next_page = href.get()
        #    if next_page is not None:
        #        yield response.follow(next_page, self.parse)
        #    print("HERE2")


        #MAKE SURE TO DECODE ALL UNICODE CHARACTERS LATER

                    #if MAX_PAGES > 0 and next_page not in spider.seen:
                #print("running " + next_page)
                #spider.seen.add(next_page)
                