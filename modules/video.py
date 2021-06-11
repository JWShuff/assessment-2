class Video():
    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available

    def __str__(self):
        return (f"""
        ---
        Video Title: {self.title}
        Rating: {self.rating}
        Copies Available: {self.copies_available}
        ---""")

