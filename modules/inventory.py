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

    # Menu functions:
    def view_video_inventory(self):
        for video in self.inventory:
            print(video)

    def view_customer_rented_videos(self):
        id = int(input("Enter Customer ID to look up their rented videos: "))
        for customer in self.customers:
            if id == customer.get_id():
                print(f"""
                {customer.get_name()} has rented the following videos:
                -----
                {customer.get_current_video_rentals()}
                -----
                """)
                return customer.get_current_video_rentals()
            raise Exception("""
            *****
            Customer not found, check entered ID?
            *****
            """)

    def rent_video(self):
        video_title = str(input("---\nEnter the video title: "))
        customer_id = int(input("---\nEnter the Customer's ID: "))
        for video in self.inventory:
            if video.get_title().lower() == video_title.lower():
                if video.get_copies_available() == 0: #Check for inventory
                    print ("No copies available to rent!")        
                video.increment_copies_available(-1)
                for customer in self.customers:
                    if customer_id == customer.get_id():
                        print("Lookup Customer Success")
                        current_videos = customer.get_current_video_rentals()
                        current_videos += f"/{video_title}"
                        customer.set_current_video_rentals(current_videos)
                        Inventory.save_customers()
                        Inventory.save_videos()
                        print(f"""
                        {customer.get_name()} rented {video_title}!
                        """)
                        return

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

    
    def save_customers(self):
        with open(customers_path, 'w') as csvfile:
            customers_csv = csv.writer(csvfile, delimiter=',')
            customers_csv.writerow(
                ["id,first_name,last_name,current_video_rentals"]
            )
            for customer in self.customers:
                customers_csv.writerow(
                    [customer.id,
                     customer.first_name,
                     customer.last_name,
                     customer.current_video_rentals]
                )
            print("Customers updated.")

    
    def save_videos(self):
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
