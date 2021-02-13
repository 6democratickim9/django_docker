# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



from test_app.models import it_news


class NewsAppPipeline(object):

    def process_item(self, item, spider):
        title = item['title']
        time = item['time']
        preview = item['preview']
        try :
            it_news.objects.create(
                title = title,
                time = time,
                preview = preview
            )
        except:
            print("왜 졸리지..?")
        return item

