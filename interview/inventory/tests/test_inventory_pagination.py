
from rest_framework.test import APITestCase

from interview.inventory.models import Inventory, InventoryType, InventoryLanguage
from interview.inventory.views import InventoryListCreateView


class TestInventoryListCreateView(APITestCase):
    def setUp(self):
        self.view = InventoryListCreateView()
        for i in range(10):
            Inventory.objects.create(
                name=f"Test Inventory {i}",
                type=InventoryType.objects.create(name=f"Test Type {i}"),
                language=InventoryLanguage.objects.create(name=f"Test Language {i}"),
                metadata={"key": "value"},
            )

    def test_get_with_pagination(self):
        response = self.client.get("/inventories/?offset=0&limit=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        response = self.client.get("/inventories/?offset=3&limit=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        response = self.client.get("/inventories/?offset=12&limit=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
