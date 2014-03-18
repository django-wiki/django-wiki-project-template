# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Following is the url configuration for django-wiki. It puts the wiki in / so
# it’s important that it is the last entry in urlpatterns. You can also put it
# in /wiki by putting '^wiki/' as the pattern.

urlpatterns += patterns('',
    url(r'^notify/', get_notify_pattern()),
    url(r'', get_wiki_pattern())
)
