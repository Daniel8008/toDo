"""toDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:url(r'^login/$','django.contrib.auth.views.login'),
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from Todo import views as core_views, views

app_name='Todo'

urlpatterns = [
url(r'^$', include('Todo.urls')),
    url(r'^Todo/(?P<Todo_id>\d+)$', views.TodoDetails, name='TodoDetails'),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'/'},name='logout'),
    url(r'^signup/$',core_views.signup,name='signup'),
     # url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^Todo/register',views.register,name='register'),
    #url(r'^Todo/login',views.user_login,name='login'),
    #url(r'^Todo/login',auth_views.auth_login.as_view(template_name='Todo/login.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^searchPost/$',views.Search,name='Search'),
    url(r'^new/$',views.Todocreate.as_view(),name='Todo_new'),
    #url(r'^delete/(?P<pk>\d+)$',views.TodoDelete.as_view(),name='Todo_delete')
]
urlpatterns += [
url('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

