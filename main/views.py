from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main import models

def index(request):
    return render(request, 'main/index.html', {})

def home(request):
    return render(request, 'main/home.html', {})



class AllBlogList(ListView):
    model_name = models.BlogTitle
    template_name = 'main/trendingblogs.html'
    context_object_name = 'allblogs'
    
    def queryset(self):
        return models.BlogTitle.objects.order_by('title')

class BlogDetail(DetailView):
    model_name = models.BlogTitle
    template_name = 'main/blog.html'
