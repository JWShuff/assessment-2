from .inventory import Inventory

class Interface:
    def __init__(self):
        self.inventory = Inventory()
        
    def run(self):
        while True:
            input = self.start_menu()
            if input == 1:
                self.view_inventory()
            elif input == 2:
                self.view_customer_rented_videos()
            elif input == 3:
                self.rent_video()
            elif input == 4:
                self.return_video()
            elif input == 5:
                self.add_new_customer()
            elif input == 6:
                break


    def start_menu(self):
        return int(input("""
        Welcome to Code Platoon Video!
        1. View video inventory
        2. View customer's rented videos
        3. Rent video
        4. Return video
        5. Add new customer
        6. Exit
        """))

    def view_inventory(self):
        self.inventory.view_video_inventory()

    def view_customer_rented_videos(self):
        pass

    def rent_video(self):
        pass

    def return_video(self):
        pass

    def add_new_customer(self):
        pass
