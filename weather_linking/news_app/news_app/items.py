
import scrapy
from scrapy_djangoitem import DjangoItem

from test_app.models import it_news


class ScrapyItnews(DjangoItem):
    django_model = it_news
    title = scrapy.Field()
    time = scrapy.Field()
    preview = scrapy.Field()

