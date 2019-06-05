# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy import Spider

# contains all the information I will need
class FrisbeeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    tournament_name = Field()
    tournament_url = Field()
    tournament_teams = Field()

# Will be a list containing the team names and twitters
class TeamListItem(scrapy.Item):
    teams = Field()

class team(scrapy.Item):
    team_name = Field()
    team_twitter = Field()

