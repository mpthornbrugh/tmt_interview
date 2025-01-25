# Create a test for the InventoryAfterDateListView view
class TestInventoryAfterDateListView(TestCase):
    def setUp(self):
        self.view = InventoryAfterDateListView()
        self.view.queryset = Inventory.objects.all()
        self.view.serializer_class = InventorySerializer
        self.view.request = RequestFactory().get('/')
        self.view.kwargs = {'date': '2022-01-01'}

        Inventory.objects.create(date='2022-01-01', name='Item 1', quantity=10)
        Inventory.objects.create(date='2022-01-02', name='Item 2', quantity=20)

    def test_get_queryset(self):
        queryset = self.view.get_queryset(date='2022-01-01')
        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().name, 'Item 1')

    def test_get(self):
        response = self.view.get(self.view.request, *[], **self.view.kwargs)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Item 1')

    def test_get_invalid_date(self):
        self.view.kwargs['date'] = 'Bad Date'
        response = self.view.get(self.view.request, *[], **self.view.kwargs)
        self.assertEqual(response.status_code, 404)
