import redis
import threading


class ProductInventory:

    def __init__(self, inventory):
        self.r = redis.Redis()
        self.lock = threading.RLock()

    def new_item(self, item, quantity):
        with self.lock:
            if self.is_product(item):
                raise Exception("{} already in the inventory".format(item))
            self.r.set(item, quantity)

    def reduce_inventory(self, item, quantity):
        with self.lock:
            if not self.is_product(item):
                raise Exception("{} not in the inventory".format(item))
            if self.get_quantity(item) < quantity:
                quantity_sold = self.get_quantity(item)
                self.r.set(item, 0)
                return quantity_sold

            self.r.set(item, self.get_quantity(item) - quantity)
            return quantity

    def increase_inventory(self, item, quantity):
        with self.lock:
            if not self.is_product(item):
                raise Exception("{} not in the inventory".format(item))
            self.r.set(item, self.get_quantity(item ) + quantity)

    def get_quantity(self, item):
        with self.lock:
            if not self.is_product(item):
                raise Exception("{} not in the inventory".format(item))
            return self.r.get(item)

    def is_product(self, item):
        products = self.r.keys(item)
        str_products = [product.decode() for product in products]
        return item in str_products

    def get_product_list(self):
        return self.r.keys()
