from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.conf.urls import url
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.home, name='dashboard'),
    path('researchGuide/', views.researchG, name='researchguide'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('forum/', include('forum.urls', namespace='forum')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('accounts/', include('accounts.urls')),
    # path('articles:/', include('articles.urls', namespace='article_list')),
    # path('accounts/', include('accounts.urls', namespace='PostListView')),

    # path('home/', article_views.article_list, name='home'),

    # url(r'^admin/', admin.site.urls),
    # url(r'^articles/', include('articles.urls')),

    # url(r'^about/$', views.about),

    # path('accounts/', include('accounts.urls')),

    # url(r'^$', views.home),
    # path('about/', views.about, name='about'),
    # path('accounts/login/', views.login, name='login'),
    # path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/'}),
    # url(r'^accounts/login/$', views.login, name='login'),
    # url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns +=('articles.views', (r'^/articles/article_list/$', 'article_list'), #calls books.views.search
# )
# articles_patterns = ([
#     path('', views.PostListView.as_view(), name='post_list'),
#     path('<int:pk>/', views.article_list.as_view(), name='article_list'),
# ], 'articles', 'forum')

if settings.DEBUG:
    import debug_toolbar

    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    # urlpatterns += [
    #     url(r'^400/$', default_views.bad_request,
    #         kwargs={'exception': Exception("Bad Request!")}),
    #     url(r'^403/$', default_views.permission_denied,
    #         kwargs={'exception': Exception("Permission Denied")}),
    #     url(r'^404/$', default_views.page_not_found,
    #         kwargs={'exception': Exception("Page not Found")}),
    #     url(r'^500/$', default_views.server_error),
    # ]
