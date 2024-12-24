from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('blogs/', views.blogs_page_view, name="list"),
    path('alkckjlbdvelrbrkbevbrltjerblbjr/', views.contact_page_view, name="contact"),
]