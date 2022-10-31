from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<int:id>/', views.event, name="address_edit"),

]