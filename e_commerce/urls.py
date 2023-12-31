from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cart.urls')),
    path('users/', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
    path("accounts/", include("allauth.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
