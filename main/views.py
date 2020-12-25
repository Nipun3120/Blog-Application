from django.http import HttpResponse, request
from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

# from main.models import Blog, BlogTitle
from main import models
def index(request):
    return render(request, 'main/index.html', {})

def home(request):
    return render(request, 'main/home.html', {})



def bloglist(request):
    blog = models.Blog
    context = {
        'posts' : blog.objects.all(),
    }
    return render(request, 'main/trendingblogs.html', context)




def blog(request):
    blog = models.Blog
    context = {
        'posts' : blog.objects.all(),
    }
    return render(request, 'main/blog.html', context)






# class BlogDetail(DetailView, User):
#     model = models.Blog 
#     template_name = 'main/blog.html'
#     context_object_name = 'object'
    
#     # queryset = models.BlogTitle.objects.order_by('content')
    

#     # def get_context_data(self, **kwargs):
        
#     #     qs = super().get_queryset()
#     #     return super().get_context_data(qs)

#     #     # return qs.order_by('title')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['User'] = self.User
#         context["category"] = "MISC"
#         return context


