from os import remove
from .customer import Customer
from .video import Video
import csv
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))
# File paths for the two csv:
customers_path = os.path.join(my_path, "../data/customers.csv") 
inventory_path = os.path.join(my_path, "../data/inventory.csv")

class Inventory:
    def __init__(self):
        self.customers = self.load_customers()
        self.inventory = self.load_videos()

    # Menu functions:
    def view_video_inventory(self):
        video_inventory = "-----\n"
        for video in self.inventory:
            video_inventory += str(video)
            video_inventory += "-----\n"
        return video_inventory

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

    def check_video_in_inventory(self, video_title):
        for video in self.inventory:
            if video.get_title() == video_title:
                return video
        raise Exception("""
            *****
            Video not found, check spelling, or confirm inventory with manager.
            *****
            """)

    def video_in_stock(self, video):
        if video.get_copies_available() > 0:
            return True
        raise Exception("""
            *****
            No copies available to rent!
            *****
            """)

    def customer_lookup_by_id(self, query_id):
        for customer in self.customers:
            if customer.get_id() == query_id:
                return customer
        raise Exception("""
            *****
            Customer not found!
            *****
            """)
    def customer_has_rented(self,customer, video_title):
        if video_title not in customer.get_current_video_rentals():
            raise Exception("""
            *****
            Customer hasn't rented this video!
            *****
            """)
        return True
            

    def rent_video(self):
        video_title = str(input("---\nEnter the video title: "))
        customer_id = int(input("---\nEnter the Customer's ID: "))
        video = self.check_video_in_inventory(video_title)
        if self.video_in_stock(video):
            video.increment_copies_available(-1)
            customer = self.customer_lookup_by_id(customer_id)
            current_videos = customer.get_current_video_rentals()
            # Count "/" to determine # of rentals and check for max:
            rental_count = current_videos.count("/")
            # This digit could be variable
            if rental_count >= 3: 
                raise Exception("""
                *****
                Customer has reached their maximum rentals.
                *****
                """)
            # Add new video with proper string formatting (/)
            current_videos += f"/{video_title}"
            # Set the customer object with updated rented videos:
            customer.set_current_video_rentals(current_videos)
            #Save changes:
            self.save_customers()
            self.save_videos()
            print(f"""
            Success!
            {customer.get_name()} rented {video_title}!
            """)
            return customer
        #Last chance exception for unexpected errors:
        raise Exception("Something very unexpected has occurred while renting a video.")

    def return_video(self):
        video_title = str(input("---\nEnter the video title: "))
        customer_id = int(input("---\nEnter the Customer's ID: "))
        video = self.check_video_in_inventory(video_title)
        video.increment_copies_available(1)
        customer = self.customer_lookup_by_id(customer_id)
        remove_str = "/" + video_title
        current_videos = customer.get_current_video_rentals()
        # Confirm customer has the video rented.
        if self.customer_has_rented(customer, remove_str):                
            # Logic to update customer's video rentals, replace with blank.
            updated_videos = current_videos.replace(remove_str, "")
            # Update the customer object
            customer.set_current_video_rentals(updated_videos)
            # Save the updated files, print success and return to main.
            self.save_customers()
            self.save_videos()
            print("Success!")
            return customer
        #Last chance exception for unexpected errors:
        raise Exception("Something very unexpected has occurred while returning a video.")

    def add_customer(self):
        # this logic gets the highest id in the loaded list of customers, and increments it by one.
        # it _*REQUIRES*_ the customers.csv to be sorted ascending by ID else ID# collision possible.
        new_id = self.customers[(len(self.customers)-1)].get_id()+1
        new_first_name = input("Enter Customer's first name: ")
        new_last_name = input("Enter Customer's last name: ")
        print("Adding customer...\n---\n---")
        self.customers.append(Customer(new_id, new_first_name, new_last_name))
        self.save_customers()
        print("Customer Added and Saved!")
    
    # Saves customers to .csv use after any transaction involving customer info changing.
    def save_customers(self):
        with open(customers_path, 'w') as csvfile:
            header = ["id","first_name","last_name","current_video_rentals"]
            customers_csv = csv.writer(csvfile, delimiter=',')
            customers_csv.writerow([field for field in header])
            for customer in self.customers:
                customers_csv.writerow(
                    [customer.get_id(),
                     customer.get_first_name(),
                     customer.get_last_name(),
                     customer.get_current_video_rentals()])
            print("Customers updated.")
            return None

    # Saves videos, use after any rent/return transaction to ensure up to date inventory.
    def save_videos(self):
        with open(inventory_path, 'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter=',')
            header = ["id", "title", "rating", "copies_available"] 
            inventory_csv.writerow([field for field in header])
            for video in self.inventory:
                inventory_csv.writerow(
                    [video.get_id(),
                     video.get_title(),
                     video.get_rating(),
                     video.get_copies_available()]
                )
        print("Videos updated.")
        return None

    @classmethod
    # Loads all customers and videos from respective .csv files (pathed in import statements)
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
        print("Loaded inventory.")
        return videos

