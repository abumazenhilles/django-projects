from django.urls import path, re_path, reverse
from django.conf.urls import url
from . import views


app_name = 'articles'

urlpatterns = [
    path('list/', views.article_list, name='list'),
    path('info/', views.about_article, name='about_us'),
    # path('detail/<slug>[\w-]+', views.article_detail, name='detail'),
    path('articles/<int:year>/<int:month>/<slug:slug>/',
         views.article_detail, name='articles_detail'),
    path('article/create/', views.article_create, name='article_create'),
    # path('articles/addComment', views.addComment, name='addComment'),
    re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$',
            views.addComment, name='addComment'),
    # url(r'^$', views.article_list),
    # url(r'^(?P<slug>[\w-]+)/$', views.article_detail),
    # url(r'^$', views.article_list, name="list"),
    # url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
