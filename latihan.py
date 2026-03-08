"""
Nama File: latihan.py
Tujuan: Menghitung rata-rata nilai dari sebuah list angka.
Fitur Utama: Validasi data kosong dan kalkulasi rata-rata.
Penulis: Faiz Hisyam Rasyid Harahap
NPM: 25782068
Tanggal Pembaruan: 8 Maret 2026
"""
def avg(data):
    total = 0
    for d in data:
        total += d
    return total / len(data)


print(avg([10, 20, 30]))
