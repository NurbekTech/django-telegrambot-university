from django.urls import path
from .views import MenuListAPIView

urlpatterns = [
    path("menu/", MenuListAPIView.as_view()),
]
