from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GuessWho.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       
    url(r'^$', 'game.views.home', name='home'),
    url(r'^GuessWho/$', 'game.views.GuessWho', name='GuessWho'),
    url(r'^AddCharacter/','game.views.addCharacter',name='AddCharacter'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
