from django.urls import path
from catalog_app import views

urlpatterns = [

    path("", views.ProductListView.as_view(), name="product_list"),
    path("catalog_app/<int:id>/", views.ProductDetailView.as_view()),
]
