from django.urls import path

from ordering import views

urlpatterns = [
    path('', views.index)
]
