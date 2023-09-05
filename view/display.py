class Display:
    @staticmethod
    def welcome_message():
        return "=================== Selamat Datang di Cinema XXI, Silahkan masukkan konfigurasi denah studio ==================="

    @staticmethod
    def main_menu(label, num_seats):
        return (f"=================== Aplikasi Cinema XXI Layout (kursi tersedia {label}-{num_seats}) ===================\n"
                "=================== Pilih salah satu menu di bawah ini ===================\n"
                "A) Pemesanan Kursi —> book_seat {seat_code}\n"
                "B) Batalkan Kursi —> cancel_seat {seat_code}\n"
                "C) Laporan Denah —> seats_status\n"
                "D) Laporan Transaksi —> transaction_status\n"
                "Masukkan 'Exit' untuk keluar.\n"
                "$ Masukkan:")
