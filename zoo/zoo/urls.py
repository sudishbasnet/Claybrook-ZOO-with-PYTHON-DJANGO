from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from ClaybrookZoo import views

urlpatterns = [
    path('',include('ClaybrookZoo.urls')),
    path('admin/', admin.site.urls),
    path('Claybrook-Zoo/', include('ClaybrookZoo.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('auth/password_change/done /',include('ClaybrookZoo.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('auth/', include('django.contrib.auth.urls')),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

