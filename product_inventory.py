
class ProductInventory:

    def __init__(self, inventory):
        self.inventory = inventory

    def new_item(self, item, quantity):
        if item in self.inventory:
            raise Exception("{} already in the inventory".format(item))
        self.inventory[item] = quantity

    def reduce_inventory(self, item, quantity):
        if item not in self.inventory:
            raise Exception("{} not in the inventory".format(item))
        if self.inventory[item] < quantity:
            quantity_sold = self.inventory[item]
            self.inventory[item] = 0
            return quantity_sold

        self.inventory[item] -= quantity
        return quantity

    def increase_inventory(self, item, quantity):
        if item not in self.inventory:
            raise Exception("{} not in the inventory".format(item))
        self.inventory[item] += quantity

    def get_quantity(self, item):
        if item not in self.inventory:
            raise Exception("{} not in the inventory".format(item))
        return self.inventory[item]

    def is_product(self, item):
        return item in self.inventory

    def get_product_list(self):
        return self.inventory.keys()