""" this document defines the project urls """

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('users.urls')),
    (r'^name/new/', 'randomizer.views.name_new'),
    (r'^$', 'base.views.index'),
)


urlpatterns += patterns('',
                        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                        'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))
