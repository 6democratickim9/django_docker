
from django.db import models
from django.db.models import F
from django.db.models.base import Model



class it_news(models.Model):

    title = models.CharField(max_length=100,unique=True)
    time = models.CharField(max_length=100)
    preview = models.CharField('preview',unique=True,max_length=500)
    id = models.IntegerField('id',primary_key=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'it_news_post'
        verbose_name_plural = 'it_news_posts'
        db_table = 'it_news_posts'
        ordering = ('-id',)      

    
    # def update_result(self):
        
    #     it_news.objects.filter(pk=it_news.pk).update(val=F('val')+1)
    #     Model.delete()
    #     Model.refresh_from_db()
    #     self.assertEqual(it_news.val,101)
    

    def get_previous_post(self):
        return self.get_previous_by_id()

    def get_next_post(self):
        return self.get_next_by_id()
    