from django.urls import path
from . import views

urlpatterns = [
    path('general_menu/', views.GeneralMenuView.as_view(), name='general_menu'),

]