
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderListByTagView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('tags/<str:tag_name>/', OrderListByTagView.as_view(), name='order-list-by-tag')
]