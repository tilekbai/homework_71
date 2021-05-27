from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView



HOMEPAGE_URL = 'products/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.urls')),
    path('products/', include('accounts.urls')),
    path('', include('api.urls')),
    path('', RedirectView.as_view(url=HOMEPAGE_URL, permanent=False))
]