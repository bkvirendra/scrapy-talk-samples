# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class TutorialPipeline(object):
    def process_item(self, item, spider):
        item['title'] = item['title'].strip()
        item['desc'] = item['desc'].strip()
        return item
