from datetime import datetime

# kode Rincian toko
toko_nama = "===== Chicken Geprek Slepet 🗿 ====="
toko_alamat = "Dibawa Angin"
toko_nomor_telepon = "08234729518"

# Daftar menu
daftar_menu = [
    {"nama": "Ayam Geprek Slepet + Nasi", "harga": 15000},
    {"nama": "Ayam Bakar Slepet + Nasi", "harga": 19000},
    {"nama": "Paket Geprek Slepet Hemat 1", "harga": 17000},
    {"nama": "Paket Geprek Slepet Hemat 2", "harga": 23000},
    {"nama": "Minuman Air Mineral", "harga": 3000},
    {"nama": "Teh Manis Dingin", "harga": 5000},
]

# Tampilkan rincian toko
print("# Nama toko")
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 29)

# Tampilkan daftar menu
print("Daftar Menu:")
for i, menu in enumerate(daftar_menu, start=1):
    print(f"{i}. {menu['nama']} ({menu['harga']} IDR)")

# Input pesanan
pesanan = {}
total_harga = 0

while True:
    pilihan = input("Pilih menu (1-5) atau ketik 'done' untuk mengakhiri pesanan: ")
    if pilihan.lower() == 'done':
        break
    elif not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(daftar_menu):
        print("Pilihan tidak valid.")
    else:
        indeks_menu = int(pilihan) - 1
        menu_terpilih = daftar_menu[indeks_menu]
        jumlah = input(f"Jumlah {menu_terpilih['nama']} yang dipesan: ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah tidak valid. Harap masukkan angka positif.")
            jumlah = input(f"Jumlah {menu_terpilih['nama']} yang dipesan: ")
        jumlah = int(jumlah)
        total_harga += menu_terpilih['harga'] * jumlah
        pesanan[menu_terpilih['nama']] = jumlah

# Diskon 20% jika total harga lebih dari 100rb
diskon = 0
if total_harga > 100000:
    diskon = 0.2 * total_harga

# Input uang dari pelanggan
uang_pelanggan = float(input("Input uang: "))

# Tampilkan struk
print("# Nama toko")
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 29)
print("=" * 29)
print("Menu yang dipesan:")
for item, jumlah in pesanan.items():
    print(f"{item}: {jumlah}")
print("Total: ", total_harga)
if diskon > 0:
    print(f"Diskon: {diskon}")
print("Uang: ", uang_pelanggan)
print("Kembalian: ", uang_pelanggan - total_harga)
print("=" * 29)
print("Barang yang sudah dibeli tidak dapat dikembalikan")
print("=" * 29)
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))