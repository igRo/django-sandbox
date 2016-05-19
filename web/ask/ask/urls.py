from django.conf.urls import url
from django.contrib import admin

from qa.views import test

urlpatterns = [
    url(r'^$', test, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<id>\d+)/', test, name='question'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new')
]
