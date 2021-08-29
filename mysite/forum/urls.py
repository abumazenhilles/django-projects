from django.urls import path
from . import views
from django.conf.urls import url
# from .models import Post
# from .views import PostCreateView, PostUpdateView, PostDeleteView

app_name = 'forum'

urlpatterns = [
    path('post/home/', views.PostListView, name='post_list'),
    path('about/', views.Aboutview, name='about'),
    path('post/<int:pk>/', views.PostDetailView, name='post_detail'),
    path('post/new/', views.CreatePostView, name='post_new'),
    path('post/<int:pk>/update/', views.PostUpdateView, name='post_update'),

    #     path('post/<slug:pk>/remove/',
    #          views.PostDeleteView.as_view(), name='post_remove'),
    #     path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    #     path('comment/<slug:pk>/approve/',
    #          views.comment_approve, name='comment_approve'),
    #     path('comment/<slug:pk>/remove/', views.comment_remove, name='comment_remove'),
    #     path('post/<slug:pk>/publish/', views.post_publish, name='post_publish'),

    #     url(r'^$',views.PostListView.as_view(), name='post_list'),
    # #     url(r'^about/$',views.AboutView.as_view(),name='about'),
    #     url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    #     url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    #     url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    #     url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    #     url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    #     url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #     url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #     url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    #     url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]