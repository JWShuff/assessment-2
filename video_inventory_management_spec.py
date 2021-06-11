import unittest
from modules.customer import Customer
from modules.video import Video
from modules.inventory import Inventory
from modules.interface import Interface

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.test_customer = Customer(3, "Jack", "Shuff")

    def test_customer_name(self):
        self.assertTrue(self.test_customer.get_name() == "Jack Shuff")

    def test_customer_rentals(self):
        self.assertTrue(self.test_customer.get_current_video_rentals() == None)

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.test_video = Video(11, "A Nightmare on Elm Street", "R", 10)

    def test_title(self):
        self.assertTrue(self.test_video.get_title(), "A Nightmare on Elm Street")

    def test_titles_available(self):
        self.assertTrue(self.test_video.get_copies_available(), 10)

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_inventory_loads_customers(self):
        pass

class TestInterface(unittest.TestCase):
    """Confirm interface creates succesfully."""
    def test_interface_instantiation(self):
        self.interface = Interface()
        self.assertIsInstance(self.interface, type(Interface()))

if __name__ == '__main__':
    unittest.main()
