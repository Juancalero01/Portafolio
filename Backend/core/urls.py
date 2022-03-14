from django.contrib import admin
from django.urls import path
from portfolio import views as vw
from django.conf import settings

urlpatterns = [
    path('', vw.index, name="index"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
