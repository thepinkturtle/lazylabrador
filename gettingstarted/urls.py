from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
#    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
#    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
#    url(r'^signup/$', hello.views.signup, name='signup'),
    url(r'^$', hello.views.login, name='login'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^index', hello.views.index name='index')
    path('admin/', admin.site.urls),
]
