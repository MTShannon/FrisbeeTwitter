
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
<<<<<<< HEAD

from inline_requests import inline_requests
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess



from frisbee.frisbee.items import FrisbeeItem

=======
from ..items import FrisbeeItem
from ..items import TeamListItem
>>>>>>> master

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

<<<<<<< HEAD
            yield scrapy.Request(url=tournament_schedule, callback=self.parse_schedule, meta={'item' : item})

    @inline_requests
    def parse_schedule(self, response):
        item = response.meta.get('item')

        tourney_teams = Selector(response).xpath('//div[@class = "pool"]//td/a')
        team_list = []

        for team in tourney_teams:
            team_name = team.xpath('./text()').extract()[0]
            team_url = 'https://play.usaultimate.org/' + team.xpath('./@href').extract()[0]

            team_page = yield Request(team_url)
            result = {}

            team_twitter = team_page.xpath('//dl[@id="CT_Main_0_dlTwitter"]//a/text()').extract()

            if len(team_twitter) == 0:
                result = {'name': team_name, 'twitter': ''}
            else:
                result = {'name': team_name, 'twitter': team_twitter[0]}

            team_list.append(result)

        item['tournament_teams'] = team_list
=======
            item['tournament_teams'] = scrapy.Request(url=tournament_schedule, callback=self.parse_schedule)


            yield scrapy.Request(url=tournament_schedule, callback=self.parse_schedule, meta={'item' : item})

    def parse_schedule(self, response):
        item = response.meta.get('item')
        tourney_teams = Selector(response).xpath('//div[@class = "pool"]//td/a')

        teams = []

        for team in tourney_teams:
            teams.append(team.xpath('./text()').extract())

        item['tournament_teams'] = teams
>>>>>>> master

        yield item







<<<<<<< HEAD










=======
>>>>>>> master


