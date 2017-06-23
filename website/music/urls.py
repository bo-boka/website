from django.conf.urls import url
from . import views

# specified to avoid namespace collision in html
app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/23/
    # name='detail' is for non hard coded urls in html
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/23/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]