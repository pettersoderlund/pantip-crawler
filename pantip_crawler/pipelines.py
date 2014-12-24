# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class PantipCrawlerPipeline(object):
#     def process_item(self, item, spider):
#         return item
import codecs
import os
from csv_helper import UnicodeWriter
class CSVWriterPipeline(object):

    def __init__(self):
        print "hello!"
        self.file = codecs.open('result.csv', 'wb', encoding='utf-8')
        self.writer = UnicodeWriter(self.file)

    def process_item(self, item, spider):
        row = [item["category"], "true" if item["recommended"] else "false", item["title"], item["author"], str(item["comment_count"]), str(item["anon_comment_count"]), str(item["subcomment_count"]), str(item["anon_subcomment_count"])]
        row = [unicode(s) for s in row]
        self.writer.writerow(row)

    def spider_closed(self, spider):
        self.file.close()