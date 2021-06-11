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
            if video.get_title() == video_title:
                if video.get_copies_available() == 0: #Check for inventory
                    raise Exception("""
                    *****
                    No copies available to rent!
                    *****
                    """)
                video.increment_copies_available(-1)
                for customer in self.customers:
                    if customer_id == customer.get_id():
                        # Get current list of rented vids:
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
                    raise Exception("""
                    *****
                    Customer not found!
                    *****
                    """)


    def return_video(self):
        # Collect the title and ID:
        video_title = str(input("---\nEnter the video title: "))
        customer_id = int(input("---\nEnter the Customer's ID: "))
        for video in self.inventory:
            # Confirm title is a video in inventory
            if video.get_title() == video_title:
                # Add 1 to available copies for next use.
                video.increment_copies_available(1)
                for customer in self.customers:
                    # Look up customer
                    if customer_id == customer.get_id():
                        # Building the replace str:
                        remove_str = "/" + video_title
                        current_videos = customer.get_current_video_rentals()
                        # Confirm customer has the video rented.
                        if remove_str not in current_videos:
                            raise Exception("""
                            *****
                            Customer hasn't rented this video!
                            *****
                            """)
                        # Logic to update customer's video rentals, replace with blank.
                        updated_videos = current_videos.replace(remove_str, "")
                        # Update the customer object
                        customer.set_current_video_rentals(updated_videos)
                        # Save the updated files, print success and return to main.
                        self.save_customers()
                        self.save_videos()
                        print("Success!") 
                        return customer
                raise Exception("""
                *****
                Customer not found, check ID #
                *****
                """)
        raise Exception("""
        *****
        Video not found, check spelling, or confirm inventory with manager.
        *****
        """)

    def add_customer(self):
        # this logic gets the highest id in the loaded list of customers, and increments it by one.
        # it _*REQUIRES*_ the customers.csv to be sorted ascending by ID else ID# collision possible.
        new_id = self.customers[(len(self.customers)-1)].get_id()+1
        new_first_name = input("Enter Customer's first name: ")
        new_last_name = input("Enter Customer's last name: ")
        print("Adding customer...\n---\n---")
        self.customers.append(Customer(new_id, new_first_name, new_last_name))
        self.save_customers
        print("Customer Added and Saved!")
    
    # Saves customers to .csv use after any transaction involving customer info changing.
    def save_customers(self):
        with open(customers_path, 'w') as csvfile:
            header = ["id","first_name","last_name","current_video_rentals"]
            customers_csv = csv.writer(csvfile, delimiter=',')
            customers_csv.writerow([field for field in header])
            for customer in self.customers:
                customers_csv.writerow(
                    [customer.id,
                     customer.first_name,
                     customer.last_name,
                     customer.current_video_rentals]
                )
            print("Customers updated.")

    # Saves videos, use after any rent/return transaction to ensure up to date inventory.
    def save_videos(self):
        with open(inventory_path, 'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter=',')
            header = ["id","title","rating","copies_available"]
            inventory_csv.writerow([field for field in header])
            for video in self.inventory:
                inventory_csv.writerow(
                    [video.id,
                     video.title,
                     video.rating,
                     video.copies_available]
                )
        print("Videos updated.")

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

