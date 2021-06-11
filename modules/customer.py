import csv
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/customers.csv")

class Customer():
    def __init__(self, id, first_name, last_name, current_video_rentals = ""):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    def __str__(self):
        return f"ID: {self.id}\nName: {self.get_name()}\nRentals: {self.get_current_video_rentals()}"

    # getters
    def get_id(self):
        return self.id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    # Use when full name is desired in interpolated strings
    def get_name(self):
        name = ""
        name += self.get_first_name() + " " + self.get_last_name()
        return name
    def get_current_video_rentals(self):
        return self.current_video_rentals

    # setters
    def set_id(self, id):
        self.id = id
    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_current_video_rentals(self, updated_current_video_rentals):
        self.current_video_rentals = updated_current_video_rentals
    def set_rental_limit(self, updated_rental_limit):
        self.rental_limit = updated_rental_limit

