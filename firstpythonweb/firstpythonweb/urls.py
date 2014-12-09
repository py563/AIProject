from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'guessWho.views.home',name='home'),
    url(r'^startgame/$', 'guessWho.views.startgame', name='startgame'),
    url(r'^AddCharacter/','guessWho.views.addCharacter',name='AddCharacter'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
