from unittest import TestCase

from interview.inventory.models import Inventory, InventoryType, InventoryLanguage
from interview.order.models import Order
from interview.order.views import DeactivateOrderView


class TestDeactivateOrderView(TestCase):
    def setUp(self):
        self.view = DeactivateOrderView()
        self.order = Order.objects.create(
            inventory=Inventory.objects.create(
                name="Test Inventory",
                type=InventoryType.objects.create(name="Test Type"),
                language=InventoryLanguage.objects.create(name="Test Language"),
                metadata={"key": "value"},
            ),
            start_date="2022-01-01",
            embargo_date="2022-01-02",
        )

    def test_deactivate_order(self):
        response = self.view.patch(None, id=self.order.id)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Order.objects.get(id=self.order.id).is_active)

    def test_deactivate_order_not_found(self):
        response = self.view.patch(None, id=999)

        self.assertEqual(response.status_code, 404)
