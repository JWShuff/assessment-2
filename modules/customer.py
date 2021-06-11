import csv
import os.path

class Customer():
    def __init__(self, id, first_name, last_name, current_video_rentals = "", rental_limit = 3):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        self.rental_limit = rental_limit

    def __str__(self):
        return f"ID: {self.id}\nName: {self.get_name()}\nRentals: {self.get_current_video_rentals()}"

    # getters
    def get_id(self):
        return self.id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_name(self):
        name = ""
        name += self.get_first_name() + " " + self.get_last_name()
        return name

    def get_current_video_rentals(self):
        if len(self.current_video_rentals) > 0:
            return self.current_video_rentals
        return None
    def get_rental_limit(self):
        return self.rental_limit

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
    
    @classmethod
    def objects(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))
                customers.append(Customer(**dict(row)))

        return customers


test = Customer(1, "Jack", "Shuff")
print(Customer.objects()[4])
