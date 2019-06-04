import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from ..items import FrisbeeItem

class FrisbeeSpider(scrapy.Spider):
    name = 'tweets'
    allowed_domains = ["usaultimate.org"]
    start_urls = [
        "https://play.usaultimate.org/events/tournament/?ViewAll=true&IsLeagueType=false&IsClinic=false&FilterByCategory=AE&CompetitionLevelId=27&SeasonId=14&GenderDivisionId=17&EventTypeId=16",
    ]

    def parse(self, response):
        tournaments = Selector(response).xpath('//td/a')
        del tournaments[0]

        for tourney in tournaments:
            item = FrisbeeItem()
            item['tournament_name'] = tourney.xpath('./text()').extract()
            item['tournament_url'] = tourney.xpath('./@href').extract()

            yield item

