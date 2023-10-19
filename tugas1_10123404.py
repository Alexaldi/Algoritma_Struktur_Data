# Algoritma Mengkonversi durasi waktu
print("Algoritma Mengkonversi durasi waktu".center(60, '-')) # Center Untuk membuat tulisan output ditengah
print()

durasi = int(input("Masukkan Detik: "))
Hari = durasi // 86400
sisaHari = durasi % 86400
Jam = sisaHari // 3600
sisaJam = sisaHari % 3600
Menit = sisaJam // 60
Detik = sisaJam % 60

print(f"Hasil Konversi:")
print(f"{int(Hari):<4} Hari, {int(Jam):<3} Jam, {int(Menit):<3} Menit, {int(Detik):<3} Detik") # f untuk format string dan :<4 untuk mengatur lebar field di output
print()

# Algoritma Mengkonversi durasi proyek
print("Algoritma Mengkonversi durasi proyek".center(60, '-')) # Center Untuk membuat tulisan output ditengah
print()

ttl_hari = int(input("Masukkan Total Hari: "))
Tahun = ttl_hari // 365
sisa_tahun = ttl_hari % 365
Bulan = sisa_tahun // 30
Hari = sisa_tahun % 30

print(f"Hasil Konversi:")
print(f"{Tahun:<4} Tahun, {Bulan:<3} Bulan, {Hari:<3} Hari") # f untuk format string dan :<4 untuk mengatur lebar field di output
print()

# Algoritma menghitung berat badan ideal
print("Algoritma menghitung berat badan ideal".center(60, '-')) # Center Untuk membuat tulisan output ditengah
print()

tinggi_badan = int(input("Input tinggi badan: "))
berat_badan = tinggi_badan - 100
berat_badan_ideal = berat_badan - (10/100 * berat_badan)

print(f"Berat Badan Ideal: {berat_badan_ideal:.2f} kg") # .:2f untuk mengatur output float 2 angka dibelakang koma 
print()

print("Terima kasih telah menggunakan program ini!".center(60, '-')) # Center Untuk membuat tulisan output ditengah
