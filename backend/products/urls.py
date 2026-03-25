from django.urls import path
from .views import ListProducts, ProductDetails

urlpatterns = [
    path("api/v1/products/", ListProducts.as_view()),
    path("api/v1/products/<int:pk>/", ProductDetails.as_view()),
]

