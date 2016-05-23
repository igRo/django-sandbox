from django.conf.urls import patterns, url

from qa.views import index, popular, question

urlpatterns = patterns('qa.views',
                       url(r'^$', index, name='index'),
                       url(r'^popular/$', popular, name='popular'),
                       url(r'^question/(?P<slug>\w+)/$', question, name='question'),
                       # url(r'^ask/$', 'ask', name='ask'),
                       # url(r'^answer/$', 'answer', name='answer'),
                       # url(r'^signup/$', 'signup', name='signup'),
                       # url(r'^login/$', 'login', name='login'),
                       )
