from django.contrib import admin
from .models import it_news

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','preview','id')
    search_fields = ('title','preview')
    
admin.site.register(it_news)
# Register your models here.
