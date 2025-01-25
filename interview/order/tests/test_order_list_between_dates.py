from interview.inventory.models import Inventory, InventoryType, InventoryLanguage
from interview.order.models import Order
from interview.order.views import OrderListBetweenDatesView
from rest_framework.test import APITestCase


class TestOrderListBetweenDatesView(APITestCase):
    def setUp(self):
        self.view = OrderListBetweenDatesView()
        Order.objects.create(
            inventory=Inventory.objects.create(
                name="Test Inventory",
                type=InventoryType.objects.create(name="Test Type"),
                language=InventoryLanguage.objects.create(name="Test Language"),
                metadata={"key": "value"},
            ),
            start_date="2022-01-01",
            embargo_date="2022-02-02",
        )
        Order.objects.create(
            inventory=Inventory.objects.create(
                name="Test Inventory 2",
                type=InventoryType.objects.create(name="Test Type 2"),
                language=InventoryLanguage.objects.create(name="Test Language 2"),
                metadata={"key": "value"},
            ),
            start_date="2022-02-02",
            embargo_date="2022-03-03",
        )

    def test_get_queryset(self):
        self.view.request = self.client.get(
            "/order/between-dates/?start_date=2022-01-01&embargo_date=2022-02-02"
        )
        queryset = self.view.get_queryset()
        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().inventory.name, "Test Inventory")
        self.assertEqual(queryset.first().start_date, "2022-01-01")
        self.assertEqual(queryset.first().embargo_date, "2022-02-02")

        self.view.request = self.client.get(
            "/order/between-dates/?start_date=2022-02-02&embargo_date=2022-03-03"
        )
        queryset = self.view.get_queryset()
        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().inventory.name, "Test Inventory 2")
        self.assertEqual(queryset.first().start_date, "2022-02-02")
        self.assertEqual(queryset.first().embargo_date, "2022-03-03")

        self.view.request = self.client.get(
            "/order/between-dates/?start_date=2022-01-01&embargo_date=2022-03-03"
        )
        queryset = self.view.get_queryset()
        self.assertEqual(queryset.count(), 2)
        self.assertEqual(queryset.first().inventory.name, "Test Inventory")
        self.assertEqual(queryset.first().start_date, "2022-01-01")
        self.assertEqual(queryset.first().embargo_date, "2022-02-02")
        self.assertEqual(queryset.last().inventory.name, "Test Inventory 2")
        self.assertEqual(queryset.last().start_date, "2022-02-02")
        self.assertEqual(queryset.last().embargo_date, "2022-03-03")

        self.view.request = self.client.get(
            "/order/between-dates/?start_date=2022-03-03&embargo_date=2022-04-04"
        )
        queryset = self.view.get_queryset()
        self.assertEqual(queryset.count(), 0)

        self.view.request = self.client.get(
            "/order/between-dates/?start_date=2022-01-01&embargo_date=2022-01-01"
        )
        queryset = self.view.get_queryset()
        self.assertEqual(queryset.count(), 0)

