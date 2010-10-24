from django.conf.urls.defaults import *
from core.views import *

urlpatterns = patterns('',
        (r'^$', homepage)
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'media(?P<path>.*)$',
'django.views.static.serve',
                { 'document_root': settings.MEDIA_ROOT }),
            )
