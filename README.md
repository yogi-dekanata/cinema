
---

# CinemaXXI Layout - Software Kasir Bioskop

## Deskripsi

Software ini digunakan untuk mengelola penjualan tiket bioskop. Fungsi yang disediakan meliputi pemesanan kursi, pembatalan kursi, laporan status denah, dan laporan transaksi penjualan tiket.

## Prasyarat

- Python 3.x

## Struktur Direktori

```
project/
|-- controller/
|   |-- __init__.py
|   |-- cinema_controller_file.py
|-- model/
|   |-- seat.py
|   |-- transaction.py
|-- view/
|   |-- display.py
|-- tests/
|   |--test_cinema_controller.py
|-- main.py
|-- README.md
```

## Instalasi dan Penggunaan

### Instalasi

1. Clone atau download repositori ini.
2. Buka terminal dan arahkan ke direktori proyek.

### Menjalankan Aplikasi

1. Jalankan `main.py` melalui terminal dengan perintah:
    ```
    python main.py
    ```

2. Ikuti instruksi yang diberikan oleh aplikasi untuk memasukkan label kursi dan jumlah kursi.
    ```
    $ Masukkan Label Kursi: A
    $ Masukkan Jumlah Kursi: 5
    ```

3. Pilih salah satu dari opsi berikut:
    - A) Pemesanan Kursi —> book_seat {seat_code}
    - B) Batalkan Kursi —> cancel_seat {seat_code}
    - C) Laporan Denah —> seats_status
    - D) Laporan Transaksi —> transaction_status

4. Untuk keluar dari aplikasi, masukkan 'Exit'.

### Menjalankan Tes (Opsional)

(Anda bisa menambahkan instruksi untuk menjalankan unit test jika ada)

## Fitur

- Pemesanan kursi
- Pembatalan kursi
- Laporan status denah
- Laporan transaksi dengan waktu penjualan

## Lisensi

GPL lisensi
---

