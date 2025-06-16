# 🚗 Aplikasi Rental Mobil - Versi Terminal (Python CLI)

Halo! Ini adalah aplikasi sederhana yang saya buat untuk mengelola sistem rental mobil langsung dari terminal (CLI) menggunakan Python.  
Aplikasi ini dibangun sebagai bagian dari latihan Capstone Project dan cocok buat kamu yang lagi belajar CRUD, pengelolaan data, dan logika program interaktif.

---

## ✨ Fitur Utama

- 🔍 **Lihat Data**  
  Tampilkan semua unit mobil dan pelanggan yang terdaftar.

- ➕ **Tambah Data**  
  Masukkan data mobil atau pelanggan baru, dengan pengecekan duplikat biar gak double.

- ✏️ **Ubah Data**  
  Edit informasi mobil atau pelanggan berdasarkan ID.

- ❌ **Hapus Data**  
  Hapus data tertentu dengan konfirmasi supaya gak kehapus tanpa sengaja.

- 🧾 **Sewa Mobil**  
  Catat proses penyewaan: siapa yang sewa, berapa hari, dan berapa total biaya.

- 🔁 **Pengembalian Mobil**  
  Tandai mobil yang sudah dikembalikan agar bisa disewa lagi.

- 📖 **Riwayat Sewa**  
  Lihat semua transaksi penyewaan yang pernah dicatat.

- ✅ **Validasi Input**  
  Program akan bantu pastikan input dari user bener: angka, pilihan menu, sampai konfirmasi `y/n`.

---

## 🛠 Teknologi & Modul yang Dipakai

| Modul        | Keterangan                          |
|--------------|--------------------------------------|
| Python 3     | Bahasa utama                        |
| `tabulate`   | Untuk tampilan data yang rapi       |
| `datetime`   | Mengatur tanggal sewa & pengembalian |

---

## ▶️ Cara Menjalankan

```bash
python rental_mobil_CRUD_capstone_project_1-JCDS_0612.py
```

📌 Jangan lupa install modul `tabulate` dulu:
```bash
pip install tabulate
```

---

## 🧾 Contoh Tampilan Tabel

```
+------------+--------+---------+-------+---------------------+
| ID Mobil   | Merk   | Tipe    | Tahun | Harga Sewa / Hari   |
+------------+--------+---------+-------+---------------------+
| TM001      | Toyota | Avanza  | 2020  | Rp 350.000          |
+------------+--------+---------+-------+---------------------+
```

---

## 📂 Struktur Proyek

```text
rental_mobil_CRUD_capstone_project_1-JCDS_0612.py       # File utama program
README.md                                               # Deskripsi ini
```

---

## 💡 Apa yang Bisa Dipelajari dari Proyek Ini?

- Cara pakai `while`, `break`, `return`, dan `continue` dengan bijak
- Validasi input dari pengguna
- Modularisasi fungsi untuk CRUD
- Menangani data yang saling berkaitan (mobil dan pelanggan)

---

## 🌱 Rencana Pengembangan Lanjutan

- 🔐 Tambah fitur login admin
- 💾 Simpan & muat data ke/dari file JSON
- 📅 Tambah fitur denda kalau pengembalian telat

---

## 🙋‍♂️ Tentang Proyek Ini

Dibuat oleh **Ridwan Darmawan**
Sebagai bagian dari Capstone Project 1 - Purwadhika JCDS 0612 
Tahun 2025

---

## 📄 Lisensi

Bebas digunakan untuk pembelajaran dan latihan pribadi. Jangan lupa kasih credit kalau kamu fork ya :)
