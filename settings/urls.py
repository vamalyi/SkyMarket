from django.conf.urls import include, url
from django.contrib import admin

from webmarket.views import (IndexView, ClientProfileView, PilotProfileView, PilotsCatalogueView,
                            OrderView, OrdersCatalogueView)

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^categories/$', CategoryEditListView.as_view(), name='category-list'),
    url(r'^categories/create/$', CategoryCreateView.as_view(), name='category-create'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetailEditListView.as_view(), name='category-detail'),
    url(r'^categories/(?P<pk>\d+)/update/$', CategoryUpdateView.as_view(), name='category-update'),
]
