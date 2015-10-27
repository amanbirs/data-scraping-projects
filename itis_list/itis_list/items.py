# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItisListItem(scrapy.Item):
    # define the fields for your item here like:
	name = scrapy.Field()
	iti_type = scrapy.Field()
	address = scrapy.Field()
	district = scrapy.Field()
	pin_code= scrapy.Field()
	email = scrapy.Field()
	affiliation_status = scrapy.Field()
	status = scrapy.Field()
	rural_urban = scrapy.Field()
	established_date = scrapy.Field()
	last_update = scrapy.Field()
	state = scrapy.Field()
	number = scrapy.Field()
	
	trade_codes = scrapy.Field()
	trade_names = scrapy.Field()
	duration = scrapy.Field()
	shift = scrapy.Field()
	units = scrapy.Field()
	seats = scrapy.Field()
	seats_filled_current = scrapy.Field()
	seats_filled_previous = scrapy.Field()

	grant_dates = scrapy.Field()
	grant_schemes = scrapy.Field()
	grant_trades = scrapy.Field()
	grant_shifts = scrapy.Field()
	grant_no_units = scrapy.Field()
	grant_files = scrapy.Field()

