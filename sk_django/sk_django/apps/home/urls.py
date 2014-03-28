from django.conf.urls import patterns, include, url

urlpatterns = patterns('sk_django.apps.home.views',
    url(r'^$','home_view',name='go_home'),

)