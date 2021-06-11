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
        self.assertTrue(self.test_customer.get_current_video_rentals() == "")

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
        self.test_video = Video(11, "A Nightmare on Elm Street", "R", 10)
        self.test_customer = Customer(3, "Jack", "Shuff")

    """
    Test assumes .csv is standardized to the backed up version.
    """
    def test_inventory_loads_customers(self):
        self.assertTrue(self.inventory.customers[0].get_name() == "Jon Young")

    def test_inventory_loads_videos(self):
        self.assertTrue(self.inventory.inventory[3].get_title(), "Sing")

    def test_view_inventory_returns_str(self):
        self.assertIsInstance(self.inventory.view_video_inventory(), str)

    def test_view_customer_rented_videos(self):
        # User input not in scope of testing.
        # To do: Research "mock" objects to fake user input.
        # with self.assertRaises(Exception) as context:
        #     self.inventory.view_customer_rented_videos()
        pass

    def test_helper_methods(self):
        """Video in stock returns true if in stock:"""
        self.assertTrue(self.inventory.video_in_stock(self.test_video), True)

        """Customer has rented throws exception if no title match: """
        with self.assertRaises(Exception) as context:
            self.inventory.customer_has_rented(self.test_customer, "101 Dalmations")
        self.assertTrue("hasn't rented" in str(context.exception))

        """Customer object is returned with successful id lookup: """
        self.assertIsInstance(self.inventory.customer_lookup_by_id(1), type(self.test_customer))

class TestInterface(unittest.TestCase):
    """Confirm interface creates succesfully."""
    def test_interface_instantiation(self):
        self.interface = Interface()
        self.assertIsInstance(self.interface, type(Interface()))

if __name__ == '__main__':
    unittest.main()
