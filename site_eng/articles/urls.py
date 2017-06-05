from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
    url(r'^login/$', views.log_in, name="login"),
    url(r'^logout/$', views.log_out, name="logout"),
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name="comment"),
    url(r'^(?P<article_id>[0-9]+)/', views.detail, name="detail"),
]
