from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from tutorial.items import PlayersItem

class PlayersSpider(CrawlSpider):
    name = "players"
    allowed_domains = ["espncricinfo.com"]
    start_urls = [
        "http://www.espncricinfo.com/indian-premier-league-2013/content/squad/624076.html"
    ]

    rules = (
        # Extract links matching 'categoryID/xxx'
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('/indian-premier-league-2013/content/player/(\d*)\.html')), callback='parse_item'),
        #/indian-premier-league-2013/content/player/49764.html
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = PlayersItem()
        item['title'] = hxs.select('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[1]/span/text()').extract()[0]
        item['desc'] = hxs.select('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[2]/span/text()').extract()[0]
        return item

    