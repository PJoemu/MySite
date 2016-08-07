from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.portal, name='portal'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
                       url(r'^home/$', views.home, name='home'),
                       )
