from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'BoardExtractor.views.default_board', name='default_board'),
    url(r'^original$', 'BoardExtractor.views.original_board', name='original_board'),
    url(r'^(?P<size>[\d]+)/(?P<bounds>[\d,]+)$', 'BoardExtractor.views.board', name='board'),

    url(r'^admin/', include(admin.site.urls)),
)
