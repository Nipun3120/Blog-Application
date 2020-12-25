from django.http import HttpResponse, request
from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView, DetailView
from main import models

def index(request):
    return render(request, 'main/index.html', {})

def home(request):
    return render(request, 'main/home.html', {})



class AllBlogList(ListView):
    model = models.BlogTitle
    template_name = 'main/trendingblogs.html'
    context_object_name = 'allblogs'
    
    def queryset(self):
        return models.BlogTitle.objects.order_by('title')

# class BlogDetail(DetailView):
#     model_name = models.Blog
#     template_name = 'main/blog.html'
#     context_object_name = 'object'

#     def queryset(self):
#         return models.BlogTitle.objects.order_by('title')
    

class BlogDetail(DetailView):
    model = models.Blog                 # not "model_name"
    template_name = 'main/blog.html'
    context_object_name = 'object'
    
    # queryset = models.BlogTitle.objects.order_by('content')
    

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('category')