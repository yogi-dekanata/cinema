import datetime

class Transaction:
    def __init__(self, seat):
        self.seat = seat
        self.time = datetime.datetime.now()

    def get_details(self):
        return self.seat.code, self.time.strftime("%d-%B-%Y %H:%M:%S")
