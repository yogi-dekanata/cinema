class Seat:
    def __init__(self, label, number):
        self.code = f"{label}{number}"
        self.is_sold = False

    def book(self):
        self.is_sold = True

    def cancel(self):
        self.is_sold = False

    def status(self):
        return "Sold" if self.is_sold else "Free"
