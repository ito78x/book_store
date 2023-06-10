from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:pk>", views.book_detail, name="book-detail")
]