from interview.inventory.models import Inventory, InventoryType, InventoryLanguage
from interview.order.models import Order, OrderTag
from interview.order.views import OrderTagsView
from rest_framework.test import APITestCase


class TestOrderTagsView(APITestCase):
    def setUp(self):
        self.view = OrderTagsView()
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
        for i in range(3):
            OrderTag.objects.create(
                name=f"Tag {i}",
                order=self.order,
            )

    def test_get_queryset(self):
        self.view.kwargs = {"order_id": self.order.id}
        queryset = self.view.get_queryset()

        self.assertEqual(queryset.count(), 3)
        self.assertEqual(queryset.first().name, "Tag 0")
        self.assertEqual(queryset.last().name, "Tag 2")
