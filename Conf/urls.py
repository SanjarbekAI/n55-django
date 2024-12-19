from django.contrib import admin
from django.urls import path

from blogs.views import home_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', home_page_view)
]
