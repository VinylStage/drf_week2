from django.urls import path
from articles import views
urlpatterns = [
    path("index/", views.index, name="index")
]
