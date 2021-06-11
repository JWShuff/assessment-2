from .customer import Customer
from .inventory import Inventory



class Interface:
    def __init__(self) -> None:
        self.inventory = Inventory()


