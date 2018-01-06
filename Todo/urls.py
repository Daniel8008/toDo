from django.conf.urls import url, include
from django.conf.urls.static import static,settings
from sys import path

from pip._vendor.html5lib.treeadapters.sax import namespace

from    Todo.views import Index



from . import  views
app_name='Todo'


urlpatterns = [

    url(r'^$',Index.as_view(),name='Index'),
    url(r'^Todo/(?P<id>[0-9]+)/$',views.TodoDetails,name='TodoDetails'),
    url(r'^login/$','django.contrib.auth.views.login'),
   ]
urlpatterns += [
        url('', include('django.contrib.auth.urls'))
]




if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
