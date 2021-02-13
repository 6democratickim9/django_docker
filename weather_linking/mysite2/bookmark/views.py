from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# from rest_framework.views import APIView
# from rest_framework.response import Response
'''
ListView.py
    object_list = SELECT * FROM bookmark;
DetailView.py
    object = SELECT * FROM bookmark WHERE id=?; 
'''

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

# class ApiBookmark(APIView):
#     def get(self, request):
#         return Response("ok", status=200)
