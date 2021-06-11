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

    # getters
    def view_video_inventory(self):
        for video in self.inventory:
            print(video)

    def view_customer_rented_videos(self, id):
        

    @classmethod
    def load_customers(cls):
        customers = []
        with open(customers_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customer(**dict(row)))
        print("Loaded customers.")
        return customers

    @classmethod
    def load_videos(cls):
        videos = []
        with open(inventory_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                videos.append(Video(**dict(row)))
        print("Loaded videos.")
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
        print("Customers updated.")

    @classmethod
    def save_videos(cls):
        with open(inventory_path, 'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter=',')
            inventory_csv.writerow(
                ["id, title, rating, copies_available"]
            )
            for video in self.inventory:
                inventory_csv.writerow(
                    [video.id,
                     video.title,
                     video.rating,
                     video.copies_available]
                )
        print("Videos updated.")