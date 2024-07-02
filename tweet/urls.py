from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/tweet/', permanent=True)),  # Redirect root URL to /tweet/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
