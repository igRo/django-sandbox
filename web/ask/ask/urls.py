from django.conf.urls import url
from django.contrib import admin

from qa.views import index, popular, question

urlpatterns = [
    url(r'^$', index, name='home'),
    # url(r'^admin/$', admin.site.urls),
    # url(r'^login/$', test, name='login'),
    # url(r'^signup/$', test, name='signup'),
    url(r'^question/(?P<id>\d+)/$', question, name='question'),
    # url(r'^ask/$', test, name='ask'),
    url(r'^popular/$', popular, name='popular'),
    # url(r'^new/$', test, name='new')
]
