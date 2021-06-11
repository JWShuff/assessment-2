from os import remove
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
            if video.get_title() == video_title:
                if video.get_copies_available() == 0: #Check for inventory
                    print ("No copies available to rent!")
                    return None
                video.increment_copies_available(-1)
                for customer in self.customers:
                    if customer_id == customer.get_id():
                        # Get current list of rented vids:
                        current_videos = customer.get_current_video_rentals()
                        # Count "/" to determine # of rentals and check for max:
                        rental_count = current_videos.count("/")
                        # This digit could be variable
                        if rental_count >= 3: 
                            print ("Customer has reached their maximum rentals.")
                            return None
                        # Add new video with proper string formatting (/)
                        current_videos += f"/{video_title}"
                        # Set the customer object with updated rented videos:
                        customer.set_current_video_rentals(current_videos)
                        #Save changes:
                        self.save_customers()
                        self.save_videos()
                        print(f"""
                        {customer.get_name()} rented {video_title}!
                        """)
                        return None
                    print("Customer not found!")
                    return None

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
                            print("Customer hasn't rented this video!")
                            return
                        # Logic to update customer's video rentals, replace /VidTitle with blank.
                        updated_videos = current_videos.replace(remove_str, "")
                        # Update the customer object
                        customer.set_current_video_rentals(updated_videos)
                        # Save the updated files, print success and return to main.
                        self.save_customers()
                        self.save_videos()
                        print("Success!") 
                        return
                print ("Customer not found!")
        print("Video not found!")

    def add_customer(self):
        new_customer = {}
        # this logic gets the highest id in the loaded list of customers, and increments it by one.
        new_customer['id'] = self.customers[(len(self.customers)-1)].get_id()+1
        print(new_customer)
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
