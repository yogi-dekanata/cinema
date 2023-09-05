from model.seat import Seat
from model.transaction import Transaction
from view.display import Display

class CinemaController:
    def __init__(self):
        self.seats = []
        self.transactions = []
        self.label = ""
        self.num_seats = 0

    def initialize_seats(self, label, num_seats):
        self.label = label
        self.num_seats = num_seats
        self.seats = [Seat(label, i + 1) for i in range(num_seats)]

    def book_seat(self, seat_code):
        seat = next((s for s in self.seats if s.code == seat_code), None)
        if seat and not seat.is_sold:
            seat.book()
            self.transactions.append(Transaction(seat))
        else:
            print("Kursi tidak ditemukan atau sudah dipesan.")

    def cancel_seat(self, seat_code):
        seat = next((s for s in self.seats if s.code == seat_code), None)
        if seat and seat.is_sold:
            seat.cancel()
            self.transactions = [t for t in self.transactions if t.seat.code != seat_code]
        else:
            print("Kursi tidak ditemukan atau belum dipesan.")

    def display_seats_status(self):
        print("=================== Denah Status ===================")
        for seat in self.seats:
            print(f"{seat.code} - {seat.status()}")

    def display_transaction_status(self):
        print("=================== Laporan Transaksi ===================")
        for trans in self.transactions:
            print(f"{trans.get_details()[0]}, {trans.get_details()[1]}")

    def run(self):
        print(Display.welcome_message())
        self.label = input("$ Masukkan Label Kursi: ")
        self.num_seats = int(input("$ Masukkan Jumlah Kursi (maksimal 20): "))
        if self.num_seats > 20:
            print("Jumlah kursi tidak boleh lebih dari 20.")
            return

        self.initialize_seats(self.label, self.num_seats)

        while True:
            print(Display.main_menu(self.label, self.num_seats))
            choice = input().strip().lower()

            if choice.startswith("book_seat"):
                _, seat_code = choice.split()
                self.book_seat(seat_code.upper())
            elif choice.startswith("cancel_seat"):
                _, seat_code = choice.split()
                self.cancel_seat(seat_code.upper())
            elif choice == "seats_status":
                self.display_seats_status()
            elif choice == "transaction_status":
                self.display_transaction_status()
            elif choice == "exit":
                break