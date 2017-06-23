from django.conf.urls import url
from . import views

# specified to avoid namespace collision in html
app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]