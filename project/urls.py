
from django.contrib import admin
from django.urls import path
import feeds.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feeds.views.home, name="home"),
    path('result/', feeds.views.result, name="result"),
]
