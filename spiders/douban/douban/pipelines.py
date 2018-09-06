# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DoubanPipeline(object):
    def open_spider(self,spider):
        self.fw = open('movie.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        obj = dict(item)
        str = json.dumps(obj,ensure_ascii=False)
        self.fw.write(str)
        return item

    def close_spider(self,spider):
        self.fw.close()