from interview.inventory.models import Inventory, InventoryType, InventoryLanguage
from interview.order.models import Order, OrderTag
from interview.order.views import OrderListByTagView
from rest_framework.test import APITestCase


class TestOrderListByTagView(APITestCase):
    def setUp(self):
        self.view = OrderListByTagView()
        self.order = Order.objects.create(
            inventory=Inventory.objects.create(
                name="Test Inventory",
                type=InventoryType.objects.create(name="Test Type"),
                language=InventoryLanguage.objects.create(name="Test Language"),
                metadata={"key": "value"},
            ),
            start_date="2022-02-22",
            embargo_date="2022-02-22",
        )
        self.order_2 = Order.objects.create(
            inventory=Inventory.objects.create(
                name="Test Inventory 2",
                type=InventoryType.objects.create(name="Test Type 2"),
                language=InventoryLanguage.objects.create(name="Test Language 2"),
                metadata={"key": "value"},
            ),
            start_date="2022-02-22",
            embargo_date="2022-02-22",
        )
        for i in range(3):
            OrderTag.objects.create(
                name=f"Tag {i}",
                order=self.order,
            )
            OrderTag.objects.create(
                name=f"Tag {i}",
                order=self.order_2,
            )

    def test_get_queryset(self):
        self.view.kwargs = {"tag_name": "Tag 0"}
        queryset = self.view.get_queryset()
        self.assertEqual(queryset.count(), 2)
        self.assertEqual(queryset.first(), self.order)
        self.assertEqual(queryset.last(), self.order_2)
