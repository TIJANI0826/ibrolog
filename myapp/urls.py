from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path(r'weblog/', include('zinnia.urls')),
    path(r'comments/', include('django_comments.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

