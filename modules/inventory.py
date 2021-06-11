from .customer import Customer
from .video import Video
import csv
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))
customers_path = os.path.join(my_path, "../data/customers.csv")
inventory_path = os.path.join(my_path, "../data/inventory.csv")

class Inventory:
    def __init__(self):
        self.inventory = self.load_videos()
        self.customers = self.load_customers()

    @classmethod
    def load_customers(cls):
        customers = []
        with open(customers_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))
                customers.append(Customer(**dict(row)))

        return customers

    @classmethod
    def load_videos(cls):
        videos = []
        with open(inventory_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))
                videos.append(Video(**dict(row)))
        return videos

    @classmethod
    def save_customers(cls):
        with open(customers_path, 'w') as csvfile:
            customers_csv = csv.writer(csvfile, delimiter=',')
            customers_csv.writerow(
                ["id, first_name, last_name, current_video_rentals"]
            )
            for customer in self.customers:
                customers_csv.writerow(
                    [customer.id,
                     customer.first_name,
                     customer.last_name,
                     customer.current_video_rentals]
                )
