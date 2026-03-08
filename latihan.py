"""
Nama File: latihan.py
Tujuan: Menghitung rata-rata nilai dari sebuah list angka.
Fitur Utama: Validasi data kosong dan kalkulasi rata-rata.
Penulis: Faiz Hisyam Rasyid Harahap
NPM: 25782068
Tanggal Pembaruan: 8 Maret 2026
"""
def avg(data):
    """
    Hitung nilai rata-rata dari list data yang diberikan.

    Args:
        data (list): List berisi angka (int atau float).

    Returns:
        float: Hasil rata-rata, atau 0.0 jika list kosong.

    Example:
        >>> avg([10, 20, 30])
        20.0
    """
    total = 0
    for d in data:
        total += d
    return total / len(data)


print(avg([10, 20, 30]))
