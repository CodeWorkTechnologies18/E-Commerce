from django.urls import path
from .views import ListOrder, CreateOrderView, OrderDetails

urlpatterns = [
    path("api/v1/get_orders/", ListOrder.as_view()),
    path("api/v1/get_order/<int:pk>/", OrderDetails.as_view()),
    path("api/v1/create_order/", CreateOrderView.as_view()),
]
