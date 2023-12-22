import os
from datetime import datetime, timedelta

# Definisi kelas Buku
class Buku:
    def __init__(self, judul, harga, informasi):
        self.judul = judul
        self.harga = harga
        self.penulis = informasi[judul]["penulis"]
        self.penerbit = informasi[judul]["penerbit"]
        self.tahun_terbit = informasi[judul]["tahun_terbit"]
        self.edisi_terbaru = informasi[judul]["edisi_terbaru"]

    def informasi_buku(self):
        return f"\nJudul: {self.judul}\nPenulis: {self.penulis}\nPenerbit: {self.penerbit}\nTahun Terbit: {self.tahun_terbit}\nHarga: {self.harga} IDR\n"

    def beli_buku(self, jumlah):
        return f"\nPembelian Berhasil!\nJumlah buku yang dibeli: {jumlah}\nTotal biaya: {self.harga * jumlah} IDR\n"

    def pinjam_buku(self, tanggal_pinjam, durasi_pinjam):
        tanggal_kembali = tanggal_pinjam + timedelta(days=durasi_pinjam)
        return f"\nPeminjaman Berhasil!\nTanggal Pinjam: {tanggal_pinjam.strftime('%Y-%m-%d %H:%M:%S')}\nDurasi Pinjam: {durasi_pinjam} hari\nTanggal Kembali: {tanggal_kembali.strftime('%Y-%m-%d %H:%M:%S')}\n"

# Fungsi untuk menampilkan daftar buku dan harganya
def tampilkan_daftar_buku(daftar_harga):
    print("----|-----------------------------|------------|")
    print("No. | Judul Buku                  | Harga")
    print("----|-----------------------------|------------|")

    for i, (judul, harga) in enumerate(daftar_harga.items(), start=1):
        print(f"{i:<4}| {judul:<28}| {harga:>7} IDR")
        print("----|-----------------------------|------------|")

def input_nomor_telepon():
    while True:
        try:
            nomor_telepon = int(input("Masukkan nomor telepon Anda: "))
            return nomor_telepon
        except ValueError:
            print("Input tidak valid. Masukkan nomor telepon dengan benar.")

def input_nominal_pembayaran():
    while True:
        try:
            nominal_pembayaran = int(input("Masukkan jumlah uang yang ingin Anda bayarkan: "))
            return nominal_pembayaran
        except ValueError:
            print("Input tidak valid. Masukkan jumlah uang dengan benar.")

# Program utama
print("=== Perpustakaan Digital Pinjam dan Beli Buku ===")

# Meminta informasi pemesan
nama_pemesan = input("Masukkan nama Anda: ")
nomor_telepon = input_nomor_telepon()

# Daftar buku dan harganya
daftar_harga = {
    "Python for Beginners": 150000,
    "Data Science Essentials": 200000,
    "The Art of Programming": 180000,
    "Introduction to AI": 250000,
    "Web Development Unleashed": 170000,
    "Deep Learning Basics": 220000,
    "JavaScript Mastery": 160000,
    "Networking Fundamentals": 190000,
    "Django Framework Guide": 210000,
    "Machine Learning Algorithms": 230000,
    "Cybersecurity Basics": 200000
}

# Informasi tambahan untuk setiap buku
informasi_buku = {
    "Python for Beginners": {"penulis": "John Smith", "penerbit": "Tech Books", "tahun_terbit": "2021", "edisi_terbaru": "Edisi Ketiga"},
    "Data Science Essentials": {"penulis": "Jane Doe", "penerbit": "Data Publications", "tahun_terbit": "2020", "edisi_terbaru": "Edisi Keempat"},
    "The Art of Programming": {"penulis": "Alan Johnson", "penerbit": "Code House", "tahun_terbit": "2019", "edisi_terbaru": "Edisi Kedua"},
    "Introduction to AI": {"penulis": "Eva Williams", "penerbit": "AI Press", "tahun_terbit": "2022", "edisi_terbaru": "Edisi Pertama"},
    "Web Development Unleashed": {"penulis": "Michael Brown", "penerbit": "Web Books", "tahun_terbit": "2023", "edisi_terbaru": "Edisi Kelima"},
    "Deep Learning Basics": {"penulis": "Sophie Turner", "penerbit": "DeepMind Publications", "tahun_terbit": "2021", "edisi_terbaru": "Edisi Ketiga"},
    "JavaScript Mastery": {"penulis": "Daniel White", "penerbit": "JS Publishing", "tahun_terbit": "2022", "edisi_terbaru": "Edisi Pertama"},
    "Networking Fundamentals": {"penulis": "Olivia Garcia", "penerbit": "Network Press", "tahun_terbit": "2020", "edisi_terbaru": "Edisi Keempat"},
    "Django Framework Guide": {"penulis": "William Johnson", "penerbit": "Django Books", "tahun_terbit": "2018", "edisi_terbaru": "Edisi Kedua"},
    "Machine Learning Algorithms": {"penulis": "Emma Davis", "penerbit": "ML Press", "tahun_terbit": "2022", "edisi_terbaru": "Edisi Pertama"},
    "Cybersecurity Basics": {"penulis": "Christopher Lee", "penerbit": "Secure Publications", "tahun_terbit": "2019", "edisi_terbaru": "Edisi Ketiga"}
}

total_biaya = 0  # Menyimpan total biaya selama pembelian
lanjut_pembelian = 'y'

while lanjut_pembelian.lower() == 'y':
    tampilkan_daftar_buku(daftar_harga)

    try:
        kode_buku = int(input("\nMasukkan kode buku yang ingin Anda pinjam atau beli: "))
        judul_buku = list(daftar_harga.keys())[kode_buku - 1]

        if judul_buku in daftar_harga:
            buku = Buku(judul_buku, daftar_harga[judul_buku], informasi_buku)
            print(buku.informasi_buku())

            pilihan = input("\nApakah Anda ingin Pinjam atau Beli buku ini? (P/B): ")

            if pilihan.lower() == 'p':
                tanggal_pinjam = datetime.now()
                durasi_pinjam = int(input("Berapa hari Anda ingin meminjam buku ini: "))
                print(buku.pinjam_buku(tanggal_pinjam, durasi_pinjam))
                print("Terimakasih telah meminjam buku di perpustakaan digital. Diharapkan segera mengembalikan buku tepat waktu.")
            elif pilihan.lower() == 'b':
                jumlah_beli = int(input(f"\nBerapa banyak buku '{judul_buku}' yang ingin Anda beli: "))
                total_biaya += buku.harga * jumlah_beli
                print(buku.beli_buku(jumlah_beli))
            else:
                print("Pilihan tidak valid. Silakan pilih 'P' untuk Pinjam atau 'B' untuk Beli.")

            lanjut_pembelian = input("\nApakah ingin meminjam/beli buku lain? (Y/N): ")
        else:
            print("\nMaaf, kode buku tidak valid. Silakan pilih buku dari daftar.")
    except (ValueError, IndexError):
        print("\nInput tidak valid. Masukkan kode buku yang benar.")

# Menampilkan informasi pemesan dan total biaya
print(f"\nTerima kasih, {nama_pemesan}! Transaksi Anda sedang diproses.")
print(f"Total biaya transaksi Anda: {total_biaya} IDR.")

# Proses pembayaran
if total_biaya > 0:
    nominal_pembayaran = input_nominal_pembayaran()

    # Mengecek kelebihan atau kekurangan pembayaran
    kembalian = nominal_pembayaran - total_biaya

    if kembalian >= 0:
        print(f"\nTerima kasih atas pembayaran Anda. Kembalian Anda: {kembalian} IDR.")
    else:
        print(f"\nMaaf, uang Anda kurang. Silakan bayar kekurangan sebesar {-kembalian} IDR.")
else:
    print("\nTidak ada transaksi untuk pembayaran.")

print(f"Kami akan menghubungi Anda di nomor {nomor_telepon} jika diperlukan.")

# Menampilkan stok semua buku setelah selesai pembelian
tampilkan_daftar_buku(daftar_harga)

# Konfirmasi pembelian
konfirmasi_pembelian = input("\nApakah transaksi Anda sesuai? (Y/N): ")

while konfirmasi_pembelian.lower() != 'y':
    print("\nMaaf, transaksi Anda tidak sesuai. Silakan ulang transaksi Anda.")
    lanjut_pembelian = input("\nApakah ingin meminjam/beli buku lain? (Y/N): ")

    if lanjut_pembelian.lower() == 'y':
        tampilkan_daftar_buku(daftar_harga)

        try:
            kode_buku = int(input("\nMasukkan kode buku yang ingin Anda pinjam atau beli: "))
            judul_buku = list(daftar_harga.keys())[kode_buku - 1]

            if judul_buku in daftar_harga:
                buku = Buku(judul_buku, daftar_harga[judul_buku], informasi_buku)
                print(buku.informasi_buku())

                pilihan = input("\nApakah Anda ingin Pinjam atau Beli buku ini? (P/B): ")

                if pilihan.lower() == 'p':
                    tanggal_pinjam = datetime.now()
                    durasi_pinjam = int(input("Berapa hari Anda ingin meminjam buku ini: "))
                    print(buku.pinjam_buku(tanggal_pinjam, durasi_pinjam))
                    print("Terimakasih telah meminjam buku di perpustakaan digital. Diharapkan segera mengembalikan buku tepat waktu.")
                elif pilihan.lower() == 'b':
                    jumlah_beli = int(input(f"\nBerapa banyak buku '{judul_buku}' yang ingin Anda beli: "))
                    total_biaya += buku.harga * jumlah_beli
                    print(buku.beli_buku(jumlah_beli))
                else:
                    print("Pilihan tidak valid. Silakan pilih 'P' untuk Pinjam atau 'B' untuk Beli.")
            else:
                print("\nMaaf, kode buku tidak valid. Silakan pilih buku dari daftar.")
        except (ValueError, IndexError):
            print("\nInput tidak valid. Masukkan kode buku yang benar.")

        konfirmasi_pembelian = input("\nApakah transaksi Anda sesuai? (Y/N): ")
    else:
        print("Terima kasih. Sampai jumpa!")

# Menampilkan informasi tambahan setelah konfirmasi transaksi
print("\nTerima kasih atas transaksinya! Transaksi Anda sudah dikonfirmasi.")
print(f"Informasi Tambahan:")
print(f"Nama Penerbit: {buku.penerbit}")
print(f"Tahun Terbit: {buku.tahun_terbit}")
print(f"Edisi Terbaru: {buku.edisi_terbaru}")

# Menampilkan nama pemesan dan nomor telepon
print(f"\nDetail Pemesan:")
print(f"Nama Pemesan: {nama_pemesan}")
print(f"Nomor Telepon: {nomor_telepon}")