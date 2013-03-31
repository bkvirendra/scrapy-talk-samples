from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from players.items import PlayersItem

# spider 
class PlayersSpider(BaseSpider):
	name = "players"

	allowed_domains = ["cricinfo.com"]

	start_urls = [
		"http://www.espncricinfo.com/indian-premier-league-2013/content/squad/624076.html"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		players_links = hxs.select('//td[@class="left"]/p[@class="ciHOFplayer"]/a/@href').extract()
		players_names = hxs.select('//td[@class="left"]/p[@class="ciHOFplayer"]/a/text()').extract()
		items = [] # container of items
		for i in xrange(0, len(players_links)):
			item = PlayersItem()
			item['name'] = players_names[i]
			item['link'] = players_links[i]
			items.append(item)
		return items