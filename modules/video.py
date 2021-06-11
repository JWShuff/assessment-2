class Video():
    def __init__(self, id, title, rating, copies_available):
        self.id = int(id)
        self.title = title
        self.rating = rating
        self.copies_available = int(copies_available)

    def __str__(self):
        return (f"""
        ---
        Video Title: {self.title}
        Rating: {self.rating}
        Copies Available: {self.copies_available}
        ---""")
        
    def get_title(self):
        return self.title
    def get_copies_available(self):
        return self.copies_available

    # Used to increment or decrement (with negative int) the copies available of a given video.
    def increment_copies_available(self, increment):
        self.copies_available += increment


