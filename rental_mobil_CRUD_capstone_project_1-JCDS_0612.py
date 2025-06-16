from tabulate import tabulate
from datetime import datetime, timedelta


input_terakhir = 7


mobil_list = [
    {
        "id_mobil" : "TA1",
        "merk" : "Toyota",
        "tipe" : "Avanza",
        "tahun" : "2020",
        "harga" : 350_000,
        "status": "tersedia",
        "penyewa": None,
        "tanggal_sewa": None,
        "tanggal_kembali": None,
        "total_harga": 0
    },
    {
        "id_mobil" : "HB2",
        "merk" : "Honda",
        "tipe" : "Brio",
        "tahun" : "2021",
        "harga" : 300_000,
        "status": "tersedia",
        "penyewa": None,
        "tanggal_sewa": None,
        "tanggal_kembali": None,
        "total_harga": 0
    },
    {
        "id_mobil" : "MB3",
        "merk" : "Mazda",
        "tipe" : "Biante",
        "tahun" : "2014",
        "harga" : 500_000,
        "status": "tersedia",
        "penyewa": None,
        "tanggal_sewa": None,
        "tanggal_kembali": None,
        "total_harga": 0
    },
    {
        "id_mobil" : "SE4",
        "merk" : "Suzuki",
        "tipe" : "Ertiga",
        "tahun" : "2016",
        "harga" : 350_000,
        "status": "tersedia",
        "penyewa": None,
        "tanggal_sewa": None,
        "tanggal_kembali": None,
        "total_harga": 0
    },    
    {
        "id_mobil" : "TV5",
        "merk" : "Toyota",
        "tipe" : "Vellfire",
        "tahun" : "2020",
        "harga" : 2_300_000,
        "status": "tersedia",
        "penyewa": None,
        "tanggal_sewa": None,
        "tanggal_kembali": None,
        "total_harga": 0
    }
]

pelanggan_list = [
    {
        "id_pelanggan" : "RI6PB",
        "nama" : "Ridwan Darmawan",
        "kelamin" : "Pria",
        "alamat" : "Bekasi"
    },
    {
        "id_pelanggan" : "DA7PM",
        "nama" : "Darmawan Afrizon",
        "kelamin" : "Pria",
        "alamat" : "Malang"
    }
]

riwayat_sewa = [{
                        "id_mobil": "TV5",
                        "merk": "Toyota",
                        "tipe": "Vellfire",
                        "id_pelanggan": "RI1PB",
                        "nama_pelanggan": "Ridwan Darmawan",
                        "tanggal_sewa": "2025-06-13",
                        "tanggal_kembali": "2025-06-15",
                        "lama_sewa": 2,
                        "total_harga": 4600000
                    }

]

def header(text):
    """
    Menampilkan teks sebagai header dengan garis pembatas atas dan bawah.

    Args:
        text (str): Teks yang ingin ditampilkan sebagai judul bagian.
    """
    print()
    print("="*len(text))
    print(text)
    print("="*len(text))
    print()

def input_angka(masukan, tipe=int):
    """
    Meminta input dari pengguna dan memastikan input bisa dikonversi ke tipe angka tertentu.

    Fungsi ini terus meminta input dari pengguna hingga input valid dapat dikonversi ke tipe data numerik tertentu (int, float, dll).

    Args:
        masukan (str): Teks yang ditampilkan sebagai prompt input.
        tipe (type, optional): Tipe data yang diinginkan (default: int).

    Returns:
        tipe: Nilai hasil konversi input.
    """
    while True:
        nilai = input(masukan)
        if nilai.isdigit():
            return tipe(nilai)
        else:
            print("Input Harus Berupa Angka. coba lagi")

def konfirmasi_ya_tidak(masukan):
    """
    Meminta input konfirmasi dari pengguna berupa 'y' atau 'n'.

    Args:
        masukan (str): Teks yang ditampilkan sebagai prompt input.

    Returns:
        str: 'y' atau 'n' dalam huruf kecil.
    """
    jawab = input(masukan).strip().lower()
    while jawab not in ["y", "n"]:
        print("Masukkan hanya 'y' atau 'n'!")
        jawab = input(masukan).strip().lower()
    return jawab

def display_all_data(masukan):
    """
    Menampilkan seluruh data unit mobil atau data pelanggan berdasarkan pilihan pengguna.

    Args:
        masukan (str): Pilihan data yang ingin ditampilkan ("1" untuk unit, "2" untuk pelanggan).
    """
    while True: 
        user_choice = masukan
        if user_choice == "1":
            if len(mobil_list) == 0:
                print("Tidak ada data unit, Masukkan data terlebih dahulu")
                input("Tekan 'enter' untuk kembali...\n")
                return
            
            else:
                print(tabulate(mobil_list, headers="keys",tablefmt="grid"))
                print()
                return

        elif user_choice == "2":
            if len(pelanggan_list) == 0:
                print("Belum ada data pelanggan yang direkam, silahkan isi data pelanggan terlebih dahulu".title())
                input("tekan 'enter' untuk kembali ke menu utama... ")
                return
        
            else:
                print(tabulate(pelanggan_list, headers="keys",tablefmt="grid"))
                print()
                return
        elif user_choice == "3":
            menu_display_data()

        else:
            print("Objek yang dipilih diluar dari menu yang sudah ditentukan.\n".title())
            user_choice = input("Coba lagi. Pilih 1 untuk unit, 2 untuk pelanggan: ").strip().lower()
            print()
            masukan = user_choice

def display_keyword_data(masukan):
    """
    Menampilkan data mobil atau pelanggan berdasarkan kata kunci pencarian.

    Args:
        masukan (str): Pilihan jenis data yang ingin dicari ("1" untuk mobil, "2" untuk pelanggan).
    """
    user_choice = masukan
    if user_choice == "1":
        data = []
        if len(mobil_list) == 0:
            print("Tidak ada data unit, Masukkan data terlebih dahulu")
            input("Tekan 'enter' untuk kembali...\n")
            return
        
        keyword = input("Masukkan kata kunci merk atau tipe atau tahun: ").strip().lower()
        print()
        for i in range(len(mobil_list)):
            mobil = mobil_list[i]
            if keyword in mobil["merk"].lower() or keyword in mobil["tipe"].lower() or keyword in mobil["tahun"]:
                data.append(mobil)

        if len(data) == 0:
            print(f"tidak ditemukan data dengan kata kunci '{keyword}'")
            menu_display_data()
                
        else:
            print(f"ditemukan {len(data)} data dengan kata kunci '{keyword}'\n")
            print(tabulate(data, headers="keys", tablefmt="grid"))
            print()

    elif user_choice == "2":
        data = []
        if len(pelanggan_list) == 0:
            print("Tidak ada data unit, Masukkan data terlebih dahulu")
            input("Tekan 'enter' untuk kembali...\n")
            return
        
        keyword = input("masukkan kata kunci Berdasarkan nama atau jenis kelamin atua alamat: ".title()).strip().lower()
        print()
        for i in range(len(pelanggan_list)):
            orang = pelanggan_list[i]
            if keyword in orang["nama"].lower() or keyword in orang["kelamin"].lower() or keyword in orang["alamat"].lower():
                data.append(orang)

        if len(data) == 0:
            print(f"tidak ditemukan data dengan kata kunci '{keyword}'")
            menu_display_data()

        else:
            print(f"ditemukan {len(data)} data dengan kata kunci '{keyword}'\n")
            print(tabulate(data, headers="keys", tablefmt="grid"))
            print()

    elif user_choice == "3":
        menu_display_data()
    
    else:
        print("\nobjek yang dipilih diluar dari menu yang sudah ditentukan. Kembali ke Menu sebelumnya!\n".title())
        user_choice = input("masukkan angka 1 untuk mencari data unit dan 2 untuk mencari data pelanggan ".title()).strip().lower()
        masukan = user_choice
        display_keyword_data(masukan)

def menu_tampil_semua():
    """
    Menampilkan menu untuk melihat seluruh data unit mobil atau seluruh data pelanggan 
    yang tersedia di sistem.
    """
    text = "---- Menampilkan semua data ----".title()
    header(text)
    print("1. Tampilkan semua data unit".title())
    print("2. Tampilkan semua data pelanggan".title())
    print("3. kembali ke menu sebelumnya\n".title())
    pilihan = input("Pilih Opsi 1 - 3: ").strip().lower()
    print()
    display_all_data(pilihan)

def menu_cari_data():
    """
    Menampilkan menu pencarian data untuk memilih pencarian data mobil atau pelanggan 
    berdasarkan kata kunci yang dimasukkan pengguna.
    """
    text = "---- Menampilkan data sesuai pencarian ----".title()
    header(text)
    print("1. Cari data unit".title())
    print("2. Cari data pelanggan".title())
    print("3. kembali ke menu sebelumnya\n".title())
    pilihan = input("Pilih Opsi 1 - 2: ").strip().lower()
    print()
    display_keyword_data(pilihan)

def menu_display_data():
    """
    Menampilkan menu utama untuk melihat semua data atau melakukan pencarian data berdasarkan kata kunci.
    """
    text = "---- data unit sewaan ----".title()
    header(text)
    print("1. Tampilkan semua data")
    print("2. Cari Berdasarkan katak kunci")
    print("3. Kembali ke Menu Utama\n")
    pilihan = input("Pilih Opsi 1 - 3: ").strip().lower()
    print()
    while not pilihan.isdigit():
        print("\nInput Harus Berupa Angka. coba lagi\n")
        pilihan = input("Pilih Opsi 1 - 3: ").strip().lower()
    if pilihan == "1":
        menu_tampil_semua()
    elif pilihan == "2":
        menu_cari_data()
    elif pilihan == "3":
        menu_utama()
    else:
        print("\nPilihan tidak valid. Kembali ke menu sebelumnya.\n")
        menu_display_data()
    
def tambah_data(masukan):
    """
    Menambahkan data baru ke dalam daftar mobil atau pelanggan berdasarkan pilihan pengguna.

    Args:
        masukan (str): Pilihan data yang ingin ditambahkan ("1" untuk mobil, "2" untuk pelanggan).
    """
    user_choice = masukan
    global input_terakhir
    if user_choice == "1":
        text = "----- tambah data mobil -----".title()
        header(text)
        merk = input("Masukkan merk mobil: ".title()).strip().lower()
        tipe = input("Masukkan tipe mobil: ".title()).strip().lower()
        tahun = input("Masukkan tahun mobil: ".title())
        harga = input_angka("Masukkan harga sewa unit per hari: ")
        if not merk or not tipe:
            print("❗ Merk dan tipe tidak boleh kosong.")
            return
        id_mobil = merk[0]+tipe[0]+str(input_terakhir)

        for i in range(len(mobil_list)):
            m = mobil_list[i]
            if (m["merk"].lower() == merk.lower()) and (m["tipe"].lower() == tipe.lower()) and (m["tahun"] == tahun) and (m["harga"] == harga):
                print("\n! data mobil dengan detail yang sama sudah ada. data tidak ditambahkan".title())
                input("tekan 'enter' untuk kembali ke menu utama")
                return
        input_terakhir += 1

        mobil = {
            "id_mobil" : id_mobil.upper(),
            "merk" : merk.title(),
            "tipe" : tipe.title(),
            "tahun" : tahun,
            "harga" : harga,
            "status": "tersedia",
            "penyewa": None,
            "tanggal_sewa": "",
            "tanggal_kembali": "",
            "total_harga": 0
        }

        konfirmasi = konfirmasi_ya_tidak("apakah anda ingin menginput data tersebut? y/n: ".title())
        if konfirmasi == "y":
            mobil_list.append(mobil)
            print("✅ data tersimpan".title())
            menu_utama() 
        else:
            print("Data tidak ditambahkan!".title())
            menu_tambah_data()

    elif user_choice == "2":
        text = "----- tambah data pelanggan -----".title()
        header(text)
        nama = input("Masukkan nama pelanggan: ".title()).strip().lower()
        kelamin = input("Masukkan jenis kelamin pelanggan: ".title()).strip().lower()
        alamat = input("Masukkan kota pelanggan: ".title()).strip().lower()
        if len(nama) < 2 or not kelamin or not alamat:
            print("❗ Nama harus minimal 2 huruf, dan kelamin serta alamat tidak boleh kosong.")
            return
        id_pelanggan = nama[:2].upper()+str(input_terakhir)+kelamin[0].upper()+alamat[0].upper()

        for i in range(len(pelanggan_list)):
            p = pelanggan_list[i]
            if (p["nama"].lower() == nama.lower()) and (p["kelamin"].lower() == kelamin.lower()) and (p["alamat"] == alamat.lower()):
                print("\n! data pelanggan dengan detail yang sama sudah ada. data tidak ditambahkan".title())
                input("tekan 'enter' untuk kembali ke menu utama")
                return
        input_terakhir += 1

        pelanggan =  {
        "id_pelanggan" : id_pelanggan.upper(),
        "nama" : nama.title(),
        "kelamin" : kelamin.title(),
        "alamat" : alamat.title()
        }
        konfirmasi = konfirmasi_ya_tidak("apakah anda ingin menginput data tersebut? y/n: ".title())
        if konfirmasi == "y":
            pelanggan_list.append(pelanggan)
            print("✅ data tersimpan".title())
            menu_utama()
        else:
            print("Data tidak ditambahkan!".title())
            menu_tambah_data()

    elif user_choice == "3":
        menu_tambah_data()
    else:
        print("\nobjek yang dipilih diluar dari menu yang sudah ditentukan. Kembali ke Menu sebelumnya!\n".title())
        user_choice = input("masukkan angka 1 untuk menambah data unit dan 2 untuk menambah data pelanggan ".title()).strip().lower()
        masukan = user_choice
        tambah_data(masukan)

def menu_tambah_data():
    """
    Menampilkan menu tambah data untuk memilih apakah ingin menambahkan data mobil atau pelanggan.
    """
    while True:
        text = "---- menu tambah data ----".title()
        header(text)
        print("1. Tambah Mobil")
        print("2. Tambah Pelanggan")
        print("3. Kembali ke Menu Utama\n")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_data("1")
        elif pilihan == "2":
            tambah_data("2")
        elif pilihan == "3":
            return  # ← kembali ke menu utama tanpa rekursi
        else:
            print("❌ Input tidak valid.")

def ubah_data(masukan):
    """
    Mengubah data mobil atau pelanggan berdasarkan ID yang dicari melalui kata kunci.

    Args:
        masukan (str): Pilihan jenis data yang ingin diubah ("1" untuk mobil, "2" untuk pelanggan, 3 untuk kembali ke menu sebelumnya).
    """
    user_choice = masukan
    if user_choice == "1":
        display_all_data(user_choice)
        pilihan = input("Masukkan ID yang ingin diubah: ").strip().lower()
        print()
        for i in range(len(mobil_list)):
            mobil = mobil_list[i]
            if pilihan == mobil["id_mobil"].lower():
                print("Masukkan data yang baru, kosongkan jika tidak ingin mengubah data")
                merk_baru = input(f"Merk saat ini ({mobil["merk"]}): ").strip().lower()
                tipe_baru = input(f"Tipe saat ini ({mobil["tipe"]}): ").strip().lower()
                tahun_input = input(f"Tahun saat ini ({mobil["tahun"]}): ").strip()
                harga_input = input(f"Harga saat ini ({mobil["harga"]}): ").strip()
                konfirmasi = konfirmasi_ya_tidak("apakah anda yakin ingin mengubah data tersebut? y/n: ".title())
                if konfirmasi == "y":
                    tahun_baru = int(tahun_input) if tahun_input.isdigit() else mobil["tahun"]
                    harga_baru = int(harga_input) if harga_input.isdigit() else mobil["harga"]
                    if merk_baru:
                        mobil["merk"] = merk_baru.title()
                    if tipe_baru:
                        mobil["tipe"] = tipe_baru.title()
                    mobil["tahun"] = tahun_baru
                    mobil ["harga"] = harga_baru
                    print("✅ data berhasil diubah".title())
                    menu_utama()
                else:
                    print("Data tidak diubah!".title())
                return menu_ubah_data()
            
        print("❌ ID tidak ditemukan!")


    elif user_choice == "2":
        display_all_data(user_choice)
        pilihan = input("Masukkan ID yang ingin diubah: ").strip().lower()
        for i in range(len(pelanggan_list)):
            pelanggan = pelanggan_list[i]
            if pilihan == pelanggan["id_pelanggan"].strip().lower():
                nama_baru = input(f"Nama ({pelanggan["nama"]}): ").strip().lower()
                kelamin_baru = input(f"Kelamin ({pelanggan["kelamin"]}): ").strip().lower()
                alamat_baru = input(f"Alamat ({pelanggan["alamat"]}): ").strip().lower()
                konfirmasi = konfirmasi_ya_tidak("apakah anda yakin ingin mengubah data tersebut? y/n: ".title())
                if konfirmasi == "y":
                    if nama_baru:
                        pelanggan["nama"] = nama_baru
                    if kelamin_baru:
                        pelanggan["kelamin"] = kelamin_baru
                    if alamat_baru:
                        pelanggan["alamat"] = alamat_baru
                    print("✅ data berhasil diubah".title())
                    return menu_ubah_data()
                else:
                    print("Data tidak diubah!".title())
                return menu_ubah_data()

        print("❌ ID tidak ditemukan!")

    elif user_choice == "3":
        menu_ubah_data()
    else:
        print("\nobjek yang dipilih diluar dari menu yang sudah ditentukan. Kembali ke Menu sebelumnya!\n".title())
        menu_ubah_data()

def menu_ubah_data():
    """
    Menampilkan menu untuk mengatur perubahan data unit mobil atau pelanggan.
    """
    text = "---- menu ubah data ----".title()
    header(text)
    print("1. Pilih data yang ingin diubah".title())
    print("2. Kembali ke Menu Utama\n")
    pilihan = input("Pilih Opsi 1 / 2: ").strip().lower()
    while not pilihan.isdigit():
        print("\nInput Harus Berupa Angka. coba lagi\n")
        pilihan = input("Pilih Opsi 1 / 2: ").strip().lower()
    if pilihan == "1":
        text = "----- ubah data mobil -----".title()
        header(text)
        print("1. ubah data unit".title())
        print("2. ubah data pelanggan".title())
        print("3. kembali ke menu sebelumnya\n".title())
        user_choice = input("Pilih Opsi 1 - 3: ").strip().lower()
        print()
        ubah_data(user_choice)
    elif pilihan == "2":
        menu_utama()
    else:
        print("\nobjek yang dipilih diluar dari menu yang sudah ditentukan. Kembali ke Menu sebelumnya!".title())
        menu_ubah_data()

def hapus_data(masukan):
    """
    Menghapus data dari daftar mobil atau pelanggan berdasarkan ID.

    Args:
        masukan (str): Pilihan jenis data yang ingin dihapus ("1" untuk mobil, "2" untuk pelanggan).
    """
    user_choice = masukan
    if user_choice == "1":
        display_all_data(user_choice)
        pilihan = input("Masukkan ID yang ingin diubah: ").strip().lower()
        for i in range(len(mobil_list)):
            mobil = mobil_list[i] 
            if pilihan in mobil["id_mobil"].lower():
                konfirmasi = konfirmasi_ya_tidak("apakah anda yakin ingin menghapus data tersebut? y/n: ".title())
                if konfirmasi == "y":
                    mobil_list.pop(i)
                    print("✅ data berhasil dihapus!".title())
                    break
                else:
                    print("Data tidak dihapus!".title())
                    return menu_hapus_data()
    
    elif user_choice == "2":
        display_all_data(user_choice)
        pilihan = input("Masukkan ID yang ingin diubah: ").strip().lower()
        for i in range(len(pelanggan_list)):
            pelanggan = pelanggan_list[i] 
            if pilihan in pelanggan["id_pelanggan"].lower():
                konfirmasi = konfirmasi_ya_tidak("apakah anda yakin ingin menghapus data tersebut? y/n: ".title())
                if konfirmasi == "y":
                    pelanggan_list.pop(i)
                    print("✅ data berhasil dihapus!".title())
                    break
                else:
                    print("Data tidak dihapus!".title())
                    return menu_hapus_data()

    elif user_choice == "3":
        menu_hapus_data()
    else:
        print("objek yang dipilih diluar dari menu yang sudah ditentukan. Kembali ke Menu sebelumnya!".title())
        return

def menu_hapus_data():
    """
    Menampilkan menu untuk memilih dan menghapus data unit mobil atau pelanggan.
    """
    text = "---- Hapus data tersimpan ----".title()
    header(text)
    print("1. pilih data yang ingin dihapus".title())
    print("2. Kembali ke Menu Utama\n")
    pilihan = input("Pilih Opsi 1 / 2: ").strip().lower()
    while not pilihan.isdigit():
        print("\nInput Harus Berupa Angka. coba lagi\n")
        pilihan = input("Pilih Opsi 1 / 2: ").strip()
    if pilihan == "1":
        text = "----- Hapus data tersimpan -----".title()
        header(text)
        print("1. hapus data unit".title())
        print("2. hapus data pelanggan".title())
        print("3. kembali ke menu sebelumnya\n".title())
        user_choice = input("Pilih Opsi 1 - 3: ").strip().lower()
        print()
        hapus_data(user_choice)
        menu_hapus_data()
    elif pilihan == "2":
        menu_utama()
    else:
        print("\nobjek yang dipilih diluar dari menu yang sudah ditentukan. Kembali ke Menu sebelumnya!\n".title())
        menu_hapus_data()

def menu_sewa_mobil():
    """
    Menyewa mobil berdasarkan ID mobil dan ID pelanggan yang valid.

    Fungsi ini akan mencatat tanggal sewa, tanggal kembali, dan total harga,
    serta menambahkan riwayat sewa.
    """
    text = "--- SEWA MOBIL ---".title()
    header(text)

    # Filter hanya mobil yang tersedia
    mobil_tersedia = [m for m in mobil_list if m.get("status") != "disewa"]
    if not mobil_tersedia:
        print("❌ Semua unit sedang disewa.")
        return

    print(tabulate(mobil_tersedia, headers="keys", tablefmt="grid"))
    id_mobil = input("\nMasukkan ID mobil yang ingin disewa: ".title()).strip().upper()
    for mobil in mobil_list:
        if mobil["id_mobil"].upper() == id_mobil:
            if mobil.get("status") == "disewa":
                print("❌ Mobil sedang disewa.")
                return

            while True:
                nama_pelanggan = input("Masukkan Nama Pelanggan: ").strip().lower()

                for pelanggan in pelanggan_list:
                    if nama_pelanggan in pelanggan["nama"].lower():
                        print(f"✅ Pelanggan ditemukan: {pelanggan['nama']} (ID: {pelanggan['id_pelanggan']})")

                        # Lanjutkan proses (misal: sewa, ubah, dll)
                        lama_sewa = input_angka("Berapa hari sewa: ")
                        while lama_sewa > 30:
                            print("maksimal peminjaman adalah 30 hari, masukkan 30 atau dibawahnya".title())
                            lama_sewa = input_angka("Berapa hari sewa: ")
                        hari_ini = datetime.today()
                        tanggal_kembali = hari_ini + timedelta(days=lama_sewa)
                        total = mobil["harga"] * lama_sewa

                        mobil["status"] = "disewa"
                        mobil["penyewa"] = pelanggan["nama"].title()
                        mobil["tanggal_sewa"] = hari_ini.strftime("%Y-%m-%d")
                        mobil["tanggal_kembali"] = tanggal_kembali.strftime("%Y-%m-%d")
                        mobil["total_harga"] = total

                        riwayat_sewa.append({
                            "id_mobil": mobil["id_mobil"],
                            "merk": mobil["merk"],
                            "tipe": mobil["tipe"],
                            "id_pelanggan": pelanggan["id_pelanggan"],
                            "nama_pelanggan": pelanggan["nama"],
                            "tanggal_sewa": hari_ini.strftime("%Y-%m-%d"),
                            "tanggal_kembali": tanggal_kembali.strftime("%Y-%m-%d"),
                            "lama_sewa": lama_sewa,
                            "total_harga": total
                        })

                        print(f"\n✅ Mobil berhasil disewa oleh {pelanggan['nama']}")
                        print(f"Tanggal kembali: {mobil['tanggal_kembali']}")
                        print(f"Total harga: Rp{total}")
                        return

                print("\n❌ ID pelanggan tidak ditemukan. Coba Lagi.\n")
                user_input = konfirmasi_ya_tidak("apakah anda ingin melanjutkan? y/n ")
                if user_input == "y":
                    print()
                else: 
                    menu_utama()
                

    print("\n❌ ID mobil tidak ditemukan.")

def menu_pengembalian_mobil():
    """
    Memproses pengembalian mobil yang sedang disewa dan mengubah status mobil kembali menjadi tersedia.
    """
    text = "--- PENGEMBALIAN MOBIL ---"
    header(text)

    # Filter mobil yang sedang disewa
    mobil_disewa = [m for m in mobil_list if m.get("status") == "disewa"]
    if not mobil_disewa:
        print("❌ Tidak ada mobil yang sedang disewa.")
        return

    print(tabulate(mobil_disewa, headers="keys", tablefmt="grid"))
    id_mobil = input("\nMasukkan ID mobil yang dikembalikan: ").strip().upper()

    for mobil in mobil_list:
        if mobil["id_mobil"].upper() == id_mobil and mobil.get("status") == "disewa":
            penyewa_id = mobil.get("penyewa")
            nama_pelanggan = "-"
            for p in pelanggan_list:
                if p["nama"] == penyewa_id:
                    nama_pelanggan = p["nama"]
                    break        

            print(f"\n🔁 Pengembalian oleh: {nama_pelanggan}")
            print(f"Total biaya sewa: Rp{mobil.get('total_harga')}")
            konfirmasi = konfirmasi_ya_tidak("Konfirmasi pengembalian? (y/n): ")
            if konfirmasi == "y":
                mobil["status"] = "tersedia"
                mobil["penyewa"] = None
                mobil["tanggal_sewa"] = None
                mobil["tanggal_kembali"] = None
                mobil["total_harga"] = 0
                print("✅ Mobil berhasil dikembalikan.")
            else:
                print("❌ Pengembalian dibatalkan.")
            return

    print("\n❌ Mobil tidak ditemukan atau tidak sedang disewa.")

def menu_riwayat_sewa():
    """
    Menampilkan riwayat sewa mobil yang tersimpan dalam daftar riwayat.
    """
    text = "--- RIWAYAT SEWA MOBIL ---".title()
    header(text)
    if len(riwayat_sewa) == 0:
        print("❌ Belum ada riwayat sewa.")
        return

    print(tabulate(riwayat_sewa, headers="keys", tablefmt="grid"))

def menu_utama():
    """
    Menampilkan menu utama program rental mobil dan menangani navigasi ke fitur-fitur lain.
    """
    while True:
        text = "---- rental mobil - menu utama ----".upper()
        header(text)
        print("1. Lihat Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Sewa Mobil")
        print("6. Pengembalian Mobil")
        print("7. Lihat Riwayat Sewa")
        print("8. Keluar")
        print()
        pilihan = input("Pilih Menu 1 - 8: ").strip().lower()

        if pilihan == "1":
            menu_display_data()

        elif pilihan == "2":
            menu_tambah_data()

        elif pilihan == "3":
            menu_ubah_data()

        elif pilihan == "4":
            menu_hapus_data()

        elif pilihan == "5":
            menu_sewa_mobil()

        elif pilihan == "6":
            menu_pengembalian_mobil()

        elif pilihan == "7":
            menu_riwayat_sewa()

        elif pilihan == "8":
            print("\nterima kasih sudah menggunakan program pendataan rental mobil... program dihentikan!\n".title())
            exit()
        
        else:
            print("\nMasukkan hanya angka 1 - 8") 
            continue  

menu_utama()
