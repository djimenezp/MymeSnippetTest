from rest_framework.reverse import reverse
from rest_framework.test import APITransactionTestCase


class BaseClass(APITransactionTestCase):
    def _create_warehouse(self, location: str = None, capacity: int = None):
        url = reverse('warehouse-list')
        data = {
            "location": location,
            "capacity": capacity
        }
        return self.client.post(url, data, follow=True, format='json')

    def _create_product(self, name: str = None, sku: str = None, ean: int = None, warehouse: int = None):
        url = reverse('product-list')
        data = {
            "name": name,
            "sku": sku,
            "ean": ean,
            "warehouse": warehouse
        }
        return self.client.post(url, data, follow=True, format='json')

    def _create_restock(self, restock_lines: list = None):
        url = reverse('restock-list')
        data = {
            "restock_lines": restock_lines
        }
        return self.client.post(url, data, follow=True, format='json')

    def _create_order(self, status: str = None, order_lines: list = None):
        url = reverse('order-list')
        data = {
            "status": status,
            "order_lines": order_lines
        }
        return self.client.post(url, data, follow=True, format='json')


# Create your tests here.
class Integration(BaseClass):

    def test_create_warehouse(self):
        location = 'loc1'
        warehouse_response = self._create_warehouse(location, 10)
        self.assertTrue(warehouse_response)
        self.assertEqual(warehouse_response.status_code, 201)
        warehouse = warehouse_response.json()
        self.assertTrue(warehouse)
        self.assertEqual(warehouse['location'], location)
        return warehouse

    def test_create_product(self):
        warehouse = self.test_create_warehouse()
        sku = 'sku1'
        product_response = self._create_product('name1', sku, 1, warehouse['id'])
        self.assertTrue(product_response)
        self.assertEqual(product_response.status_code, 201)
        product = product_response.json()
        self.assertTrue(product)
        self.assertEqual(product['sku'], sku)
        return product

    def test_create_restock(self):
        product = self.test_create_product()
        restock_lines = [{"product": product['sku'], "quantity": 1}]
        restock_response = self._create_restock(restock_lines)
        self.assertTrue(restock_response)
        self.assertEqual(restock_response.status_code, 201)
        restock = restock_response.json()
        self.assertTrue(restock)
        self.assertEqual(restock['restock_lines'][0]['product'], restock_lines[0]['product'])

    def test_create_order(self):
        product = self.test_create_product()
        restock_lines = [{"product": product['sku'], "quantity": 1}]
        restock_response = self._create_restock(restock_lines)
        self.assertTrue(restock_response)
        self.assertEqual(restock_response.status_code, 201)
        restock = restock_response.json()
        self.assertTrue(restock)
        self.assertEqual(restock['restock_lines'][0]['product'], restock_lines[0]['product'])
        order_lines = [{"product": product['sku'], "quantity": 1}]
        order_response = self._create_order('pending', order_lines)
        self.assertTrue(order_response)
        self.assertEqual(order_response.status_code, 201)
        order = order_response.json()
        self.assertTrue(order)
        self.assertEqual(order['order_lines'][0]['product'], order_lines[0]['product'])

    def test_no_stock(self):
        product = self.test_create_product()
        restock_lines = [{"product": product['sku'], "quantity": 1}]
        restock_response = self._create_restock(restock_lines)
        self.assertTrue(restock_response)
        self.assertEqual(restock_response.status_code, 201)
        restock = restock_response.json()
        self.assertTrue(restock)
        self.assertEqual(restock['restock_lines'][0]['product'], restock_lines[0]['product'])
        order_lines = [{"product": product['sku'], "quantity": 2}]
        order_response = self._create_order('pending', order_lines)
        self.assertTrue(order_response)
        self.assertEqual(order_response.status_code, 400)
        order = order_response.json()
        self.assertTrue(order)
        self.assertEqual(order['order_lines'][0]['non_field_errors'][0], 'No stock')

    def test_max_capacity(self):
        product = self.test_create_product()
        restock_lines = [{"product": product['sku'], "quantity": 12}]
        restock_response = self._create_restock(restock_lines)
        self.assertTrue(restock_response)
        self.assertEqual(restock_response.status_code, 400)
        restock = restock_response.json()
        self.assertTrue(restock)
        self.assertEqual(restock['restock_lines'][0]['non_field_errors'][0], 'Warehouse full')
