from django.shortcuts import redirect, render
from .models import it_news
from django.views.generic.edit import FormView
from .forms import PostSearchForm
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import RefreshForm
import os
from django.db.models import Q


class NewsLV(ListView):
    model = it_news
    template_name = "test_app/templates/test_app/post_all.html"
    context_object_name = "it_news_posts" 

    paginate_by = 10

class RefreshFormView(FormView):
    template_name = "test_app/templates/test_app/post_all.html"
    form_class = RefreshForm
    success_url = '/it_news/refresh/'
    context_object_name = "it_news_posts" 

    paginate_by = 10


    def form_valid(self, form):
        it_news.objects.all().delete()
        print("잘 됐으면 좋겠당 ^^")
        # print(self.request)
        # os.chdir('C:/Users/MIN/Desktop/module_project/weather_linking/news_app/news_app')
        os.chdir('C:/Users/MIN/django_project/weather_linking/news_app/news_app')
        os.system('scrapy crawl mybots_it')
        return redirect('/it_news') 
        # return super().form_valid(form)

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "test_app/templates/test_app/post_search.html"

    def form_valid(self,form):
        schword= self.request.POST['search_word']

        post_list= it_news.objects.filter( Q(title__icontains = schword)| Q(preview__icontains= schword)|Q(id__icontains=schword)).distinct()

        #검색된 결과
        context={}

        context['form'] = form
        context['search_keyword']=schword
        context['search_list']=post_list
        print(post_list)

        return render(self.request, self.template_name,context)