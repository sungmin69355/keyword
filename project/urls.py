
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import feeds.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feeds.views.home, name="home"),
    path('result/', feeds.views.result, name="result"),
    path('stock/', feeds.views.stock, name="stock"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
