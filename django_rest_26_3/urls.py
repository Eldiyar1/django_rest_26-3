from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main_app.urls')),
    path('api/v1/users/', include('users.urls'))
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += swagger.urlpatterns