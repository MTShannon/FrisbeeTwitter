import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from ..items import FrisbeeItem
from ..items import TeamListItem

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
            item['tournament_name'] = tourney.xpath('./text()').extract()[0]
            item['tournament_url'] = tourney.xpath('./@href').extract()[0]

            tournament_schedule = item['tournament_url'] + '/schedule/Men/CollegeMen/'

            item['tournament_teams'] = scrapy.Request(url=tournament_schedule, callback=self.parse_schedule)


            yield scrapy.Request(url=tournament_schedule, callback=self.parse_schedule, meta={'item' : item})

    def parse_schedule(self, response):
        item = response.meta.get('item')
        tourney_teams = Selector(response).xpath('//div[@class = "pool"]//td/a')

        teams = []

        for team in tourney_teams:
            teams.append(team.xpath('./text()').extract())

        item['tournament_teams'] = teams

        yield item









