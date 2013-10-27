# coding: utf-8


from django.conf.urls import patterns, include, url


urlpatterns = patterns('eventex.subscriptions.view',
    url(r'^$', 'subscribe', name='subscrbe'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)
