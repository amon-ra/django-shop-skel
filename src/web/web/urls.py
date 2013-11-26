from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
#from shop import urls as shop_urls 
import cms.urls

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r'^checkout/confirm/$', MyOrderConfirmView.as_view(), name='checkout_shipping'),
    url(r'^shop/discount/', include('discount.urls')),
    url(r'^shop/cart/', include('shop_simplevariations.urls')),
    url(r'^shop/catalog/', include('shop_categories.urls')),
    url(r'^shop/', include('shop.urls')),   
    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore')),
)

if settings.DEBUG:
    urlpatterns = i18n_patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
