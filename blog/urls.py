from django.conf.urls import url
from . import views #dalla cartella corrente importa le liste che sono state create

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), 
]
#dire che la vista principale deve essere ad una determinata pagina e lo devoquindi definire qui negli url
