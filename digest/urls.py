from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<str:id>/', views.event, name="address_edit"),

]