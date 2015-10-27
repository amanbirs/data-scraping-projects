# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndiaElectionDataItem(scrapy.Item):
	constituency_name = scrapy.Field()
	constituency_number = scrapy.Field()
	reservation = scrapy.Field()
	district_name = scrapy.Field()
	winning_candidate = scrapy.Field()
	winning_party = scrapy.Field()
	total_electors = scrapy.Field()
	total_votes = scrapy.Field()
	total_votes_perc = scrapy.Field()
	victory_margin = scrapy.Field()
	victory_margin_perc = scrapy.Field()
	state_name = scrapy.Field()
	election_year = scrapy.Field()
