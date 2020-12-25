from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from main import views


urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('mainpage/', auth(views.home), name = 'home'),
    path('blogs/<int:pk>', auth(views.BlogDetail.as_view()), name = 'blog'),
    path('trendingblogs/', auth(views.AllBlogList.as_view()), name = 'trendingblogs'),
]