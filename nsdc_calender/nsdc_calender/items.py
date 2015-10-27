# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NsdcCalenderItem(scrapy.Item):
	course_name = scrapy.Field()
	course_fees	= scrapy.Field()
	trained_for_job_role = scrapy.Field()
	course_duration_days = scrapy.Field()
	batch_startdate = scrapy.Field()
	batch_enddate = scrapy.Field()
	training_centre_name = scrapy.Field()
	training_centre_address = scrapy.Field()
	contact_name = scrapy.Field()
	contact_email = scrapy.Field()
	contact_mobile = scrapy.Field()
	training_provider_name = scrapy.Field()
	state = scrapy.Field()
	district = scrapy.Field()
	sector = scrapy.Field()

