from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', include('main.urls')),
    path('auth/', include('authen.urls')),
]


# default: home page,
# for login / is passed, amd in urls.py of authen, there are seprate login and logout urlpatterns..