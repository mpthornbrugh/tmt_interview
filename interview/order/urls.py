
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagsView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('tags/<int:order_id>/', OrderTagsView.as_view(), name='order-tags'),
]