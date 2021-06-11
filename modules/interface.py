class Interface:
    def __init__(self) -> None:
        self.inventory = Inventory()
    @classmethod
    def save_customers(cls):
        with open(path, 'w') as csvfile:
            customers_csv = csv.writer(csvfile, delimiter=',')
            customers_csv.writerow([
                "id, first_name, last_name, current_video_rentals, rental_limit"
            ])
            for customer in self.customers:
                customers_csv.writerow(
                    [customer.id, customer.first_name, customer.last_name, customer.current_video_rentals, customer.rental_limit])
