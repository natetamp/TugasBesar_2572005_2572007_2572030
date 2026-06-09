# Nama File : Tubes_Daspro_2572005_2572007_2527030.py
# Program Sistem Manajemen Laundry
# Penulis : Vicki Ferdinand, Nathan E E Tampilang, Claresta Jesslyn Lokanata
# Kamus Data
# matriks_laundry : var list penyimpan data utama laundry (matriks of string/integer/float)
# kebawah : var int penyimpan indeks baris pengulangan utama (integer)

matriks_laundry = [None] * 1000
for kebawah in range(0, 1000, 1):
    matriks_laundry[kebawah] = [None] * 7

# Kamus Lokal
# username : var list penyimpan daftar nama pengguna yang valid (list of string)
# password : var list penyimpan daftar kata sandi yang valid (list of integer)
# auth : var boolean penanda status login berhasil atau tidak (boolean)
# i : var int penyimpan indeks pengulangan untuk mengecek data login (integer)
def login(user, pw):
    username = ["admin", "kasir", "owner"]
    password = [123, 321, 111]
    auth = False
    
    for i in range(0, 3, 1):
        if user == username[i] and pw == password[i]:
            user = username[i]
            auth = True
            
    if auth == True:
        print("\nLogin Berhasil!\n")
        if user == "admin":
            menu_admin()
        elif user == "kasir":
            menu_kasir()
        elif user == "owner":
            menu_owner()
    else:
        print("\nLogin Gagal! Username atau password salah.\n")
    return auth

# Kamus Lokal
# lanjut_menu : var boolean penanda kelangsungan pengulangan menu admin (boolean)
# A : var list penyimpan teks pilihan menu admin (list of string)
# i : var int penyimpan indeks pengulangan untuk mencetak menu (integer)
# choice_input : var string penyimpan input mentah dari pengguna (string)
# choice : var int penyimpan pilihan menu yang sudah diubah ke angka (integer)
def menu_admin():
    lanjut_menu = True
    while lanjut_menu == True:
        print("Welcome, admin!")
        print("            ===MENU===            ")
        A = ["Update Status", "Hapus Data", "Lihat Semua Data", "Logout"]
        for i in range(0, 4, 1):
            print(f"{i+1}. {A[i]}")
            
        choice_input = input("Pilih menu (1-4): ")
        choice = int(choice_input)
        
        if choice == 1:
            stat_update()
        elif choice == 2:
            hapus_data()
        elif choice == 3:
            lihat_data("admin")
        elif choice == 4:
            lanjut_menu = False
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Lokal
# lanjut_menu : var boolean penanda kelangsungan pengulangan menu kasir (boolean)
# A : var list penyimpan teks pilihan menu kasir (list of string)
# i : var int penyimpan indeks pengulangan untuk mencetak menu (integer)
# choice_input : var string penyimpan input mentah dari pengguna (string)
# choice : var int penyimpan pilihan menu yang sudah diubah ke angka (integer)
def menu_kasir():
    lanjut_menu = True
    while lanjut_menu == True:
        print("Welcome, kasir!")
        print("            ===MENU===            ")
        A = ["Tambah Data Laundry", "Lihat Data Laundry", "Cetak Struk", "Logout"]
        for i in range(0, 4, 1):
            print(f"{i+1}. {A[i]}")
            
        choice_input = input("Pilih menu (1-4): ")
        choice = int(choice_input)
        
        if choice == 1:
            tambah_data()
        elif choice == 2:
            lihat_data("kasir")
        elif choice == 3:
            cetak_struk()
        elif choice == 4:
            lanjut_menu = False
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Lokal
# lanjut_menu : var boolean penanda kelangsungan pengulangan menu owner (boolean)
# A : var list penyimpan teks pilihan menu owner (list of string)
# i : var int penyimpan indeks pengulangan untuk mencetak menu (integer)
# choice_input : var string penyimpan input mentah dari pengguna (string)
# choice : var int penyimpan pilihan menu yang sudah diubah ke angka (integer)
def menu_owner():
    print("Welcome, owner!")
    lanjut_menu = True
    while lanjut_menu == True:
        print("            ===MENU===            ")
        A = ["Total Pendapatan", "Jumlah Transaksi", "Cucian Belum Selesai", "Logout"]
        for i in range(0, 4, 1):
            print(f"{i+1}. {A[i]}")
            
        choice_input = input("Pilih menu (1-4): ")
        choice = int(choice_input)
        
        if choice == 1:
            pendapatan()
        elif choice == 2:
            jumlah_transaksi()
        elif choice == 3:
            cucian_belum_selesai()
        elif choice == 4:
            lanjut_menu = False
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Lokal
# tarif : var int penyimpan harga dasar per kilogram (integer)
# total_sementara : var float penyimpan perhitungan harga sebelum diskon (float)
# potongan : var float penyimpan nilai diskon (float)
def hitung_harga(berat, layanan, member):
    if layanan == "Reguler":
        tarif = 5000
    else: 
        tarif = 10000
        
    total_sementara = berat * tarif
    
    if member == 1:
        potongan = total_sementara * 0.10
        total_sementara = total_sementara - potongan
        
    return total_sementara

# Kamus Lokal
# data_ada : var boolean penanda apakah ada data di dalam matriks (boolean)
# kebawah : var int penyimpan indeks baris saat pencarian data (integer)
# no_input : var string penyimpan input nomor data yang ingin diubah (string)
# no : var int penyimpan nomor indeks target pembaruan (integer)
# pilih_input : var string penyimpan input pilihan status baru (string)
# pilih : var int penyimpan pilihan status yang sudah diubah ke angka (integer)
def stat_update():
    global matriks_laundry
    
    data_ada = False
    kebawah = 0
    while kebawah < 1000 and data_ada == False:
        if matriks_laundry[kebawah][0] != None:
            data_ada = True
        kebawah = kebawah + 1

    if data_ada == False:
        print("Belum ada data laundry.")
    else:
        print("\n===Update Status Laundry===")
        for kebawah in range(0, 1000, 1):
            if matriks_laundry[kebawah][0] != None:
                print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Status: {matriks_laundry[kebawah][4]}")
                
        no_input = input("\nMasukkan nomor urut data (No) yang ingin diupdate: ")
        no = int(no_input) - 1
        
        if no >= 0 and no < 1000 and matriks_laundry[no][0] != None:
            print("Pilih status baru:")
            print("1. Proses")
            print("2. Selesai")
            print("3. Diambil")
            pilih_input = input("Pilih (1-3): ")
            pilih = int(pilih_input)
            
            if pilih == 1:
                matriks_laundry[no][4] = "Proses"
                print("Status berhasil diupdate.")
            elif pilih == 2:
                matriks_laundry[no][4] = "Selesai"
                print("Status berhasil diupdate.")
            elif pilih == 3:
                matriks_laundry[no][4] = "Diambil"
                print("Status berhasil diupdate.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Data tidak ditemukan atau nomor urut salah.")

# Kamus Lokal
# data_ada : var boolean penanda apakah ada data di dalam matriks (boolean)
# kebawah : var int penyimpan indeks baris saat pencarian data (integer)
# kesamping : var int penyimpan indeks kolom saat proses penghapusan (integer)
# no_input : var string penyimpan input nomor data yang ingin dihapus (string)
# no : var int penyimpan nomor indeks target penghapusan (integer)
# konfirmasi : var string penyimpan jawaban persetujuan menghapus data (string)
def hapus_data():
    global matriks_laundry
    
    data_ada = False
    kebawah = 0
    while kebawah < 1000 and data_ada == False:
        if matriks_laundry[kebawah][0] != None:
            data_ada = True
        kebawah = kebawah + 1

    if data_ada == False:
        print("Belum ada data laundry.")
    else:
        print("\n===Hapus Data Laundry===")
        for kebawah in range(0, 1000, 1):
            if matriks_laundry[kebawah][0] != None:
                print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Status: {matriks_laundry[kebawah][4]}")

        no_input = input("\nMasukkan nomor urut data yang ingin dihapus: ")
        no = int(no_input) - 1

        if no >= 0 and no < 1000 and matriks_laundry[no][0] != None:
            konfirmasi = input("Yakin ingin menghapus data? (y/n): ")
            if konfirmasi == 'y' or konfirmasi == 'Y':
                for kesamping in range(0, 7, 1):
                    matriks_laundry[no][kesamping] = None
                print("Data berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Data tidak ditemukan atau nomor urut salah.")

# Kamus Lokal
# data_ada : var boolean penanda apakah ada data di dalam matriks (boolean)
# kebawah : var int penyimpan indeks baris pengulangan (integer)
def lihat_data(role):
    global matriks_laundry

    data_ada = False
    kebawah = 0
    while kebawah < 1000 and data_ada == False:
        if matriks_laundry[kebawah][0] != None:
            data_ada = True
        kebawah = kebawah + 1

    if data_ada == False:
        print("Belum ada data laundry.")
    else:
        print("\n===Data Laundry===")
        for kebawah in range(0, 1000, 1):
            if matriks_laundry[kebawah][0] != None:
                if role == "admin":
                    print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Berat: {matriks_laundry[kebawah][1]}kg | Layanan: {matriks_laundry[kebawah][2]} | Harga: Rp{matriks_laundry[kebawah][3]} | Status: {matriks_laundry[kebawah][4]}")
                else: 
                    print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Berat: {matriks_laundry[kebawah][1]}kg | Layanan: {matriks_laundry[kebawah][2]} | Harga: Rp{matriks_laundry[kebawah][3]}")
        print()

# Kamus Lokal
# idx : var int penyimpan indeks array yang masih kosong (integer)
# ketemu_kosong : var boolean penanda apakah sudah menemukan tempat kosong (boolean)
# kebawah : var int penyimpan indeks baris pengulangan (integer)
# nomor : var int penyimpan nomor invoice otomatis (integer)
# nama_input : var string penyimpan nama pelanggan (string)
# berat_input : var string penyimpan input mentah berat cucian (string)
# nilai_berat : var float penyimpan berat cucian dalam bentuk desimal (float)
# input_layanan_valid : var boolean penanda input layanan benar (boolean)
# pilih_input : var string penyimpan input mentah pilihan layanan (string)
# pilih : var int penyimpan pilihan layanan yang sudah diubah ke angka (integer)
# layanan_pilih : var string penyimpan nama layanan hasil pilihan (string)
# input_member_valid : var boolean penanda input member benar (boolean)
# member_input : var string penyimpan input mentah status member (string)
# member : var int penyimpan status member yang diubah ke angka (integer)
def tambah_data():
    global matriks_laundry
    
    idx = -1
    ketemu_kosong = False
    kebawah = 0
    while kebawah < 1000 and ketemu_kosong == False:
        if matriks_laundry[kebawah][0] == None:
            idx = kebawah
            ketemu_kosong = True
        kebawah = kebawah + 1
            
    if idx == -1:
        print("Data penuh, tidak bisa menambah data baru.")
    else:
        nomor = 1
        for kebawah in range(0, 1000, 1):
            if matriks_laundry[kebawah][5] != None:
                nomor = matriks_laundry[kebawah][5] + 1

        nama_input = input("Nama Pelanggan : ")
        berat_input = input("Berat Cucian (kg): ")
        nilai_berat = float(berat_input)
            
        print("===Pilihan Layanan===")
        print("   1. Reguler   ")
        print("   2. Express   ")
        
        input_layanan_valid = False
        while input_layanan_valid == False:
            pilih_input = input("Pilih layanan (1/2): ")
            if pilih_input == "1" or pilih_input == "2":
                input_layanan_valid = True
            else:
                print("Pilihan salah, coba lagi.")
                
        pilih = int(pilih_input)
        if pilih == 1:
            layanan_pilih = "Reguler"
        else:
            layanan_pilih = "Express"
            
        print("Apakah pelanggan punya Member? (Diskon 10%)")
        print("1. Ya\n2. Tidak")
        
        input_member_valid = False
        while input_member_valid == False:
            member_input = input("Pilih (1/2): ")
            if member_input == "1" or member_input == "2":
                input_member_valid = True
            else:
                print("Pilihan salah, coba lagi.")
                
        member = int(member_input)

        matriks_laundry[idx][0] = nama_input
        matriks_laundry[idx][1] = nilai_berat
        matriks_laundry[idx][2] = layanan_pilih
        matriks_laundry[idx][3] = hitung_harga(nilai_berat, layanan_pilih, member)
        matriks_laundry[idx][4] = "Proses"
        matriks_laundry[idx][5] = nomor
        if member == 1:
            matriks_laundry[idx][6] = 1
        else:
            matriks_laundry[idx][6] = 0

        print("Data berhasil dimasukkan")

# Kamus Lokal
# no_inv_input : var string penyimpan input mentah nomor invoice (string)
# no_inv : var int penyimpan nomor invoice yang dicari (integer)
# idx : var int penyimpan indeks array jika invoice ditemukan (integer)
# ketemu_invoice : var boolean penanda apakah invoice cocok (boolean)
# kebawah : var int penyimpan indeks baris pencarian (integer)
def cetak_struk():
    global matriks_laundry

    print("\n===Cetak Struk===")
    no_inv_input = input("Nomor Invoice: ")
    no_inv = int(no_inv_input)
    
    idx = -1
    ketemu_invoice = False
    kebawah = 0
    while kebawah < 1000 and ketemu_invoice == False:
        if matriks_laundry[kebawah][5] == no_inv:
            idx = kebawah
            ketemu_invoice = True
        kebawah = kebawah + 1

    if idx == -1:
        print("Invoice tidak ditemukan.")
    else:
        print("\n========================================")
        print("            INDIGO LAUNDRY           ")
        print("========================================")
        print(f"Invoice  : {matriks_laundry[idx][5]}")
        if matriks_laundry[idx][6] == 1:
            print(f"Nama     : {matriks_laundry[idx][0]} (Member)")
        else:
            print(f"Nama     : {matriks_laundry[idx][0]} (Non-Member)")
        print(f"Berat    : {matriks_laundry[idx][1]} kg")
        print(f"Layanan  : {matriks_laundry[idx][2]}")
        print(f"Status   : {matriks_laundry[idx][4]}")
        print("----------------------------------------")
        print(f"Total    : Rp {matriks_laundry[idx][3]}")
        print("========================================")
        print()

# Kamus Lokal
# total : var float penyimpan total akumulasi seluruh pendapatan (float)
# kebawah : var int penyimpan indeks baris pengulangan (integer)
def pendapatan():
    global matriks_laundry

    total = 0
    for kebawah in range(0, 1000, 1):
        if matriks_laundry[kebawah][3] != None:
            total = total + matriks_laundry[kebawah][3]

    print("\n===Total Pendapatan===")
    print(f"Total Pendapatan: Rp {total}")
    print()

# Kamus Lokal
# jumlah : var int penyimpan angka total pesanan yang masuk (integer)
# kebawah : var int penyimpan indeks baris pengulangan (integer)
def jumlah_transaksi():
    global matriks_laundry

    jumlah = 0
    for kebawah in range(0, 1000, 1):
        if matriks_laundry[kebawah][0] != None:
            jumlah = jumlah + 1

    print("\n===Jumlah Transaksi===")
    print(f"Total Transaksi: {jumlah} transaksi")
    print()

# Kamus Lokal
# data_ada : var boolean penanda ada tidaknya cucian yang berstatus selain Diambil (boolean)
# kebawah : var int penyimpan indeks baris pengulangan (integer)
def cucian_belum_selesai():
    global matriks_laundry
    
    print("\n===Cucian Belum Selesai===")
    data_ada = False
    for kebawah in range(0, 1000, 1):
        if matriks_laundry[kebawah][0] != None:
            if matriks_laundry[kebawah][4] != "Diambil":
                data_ada = True
                print(f"Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Status: {matriks_laundry[kebawah][4]}")
    
    if data_ada == False:
        print("Mantap! Semua cucian sudah selesai dan diambil.")
    print()

# Kamus Lokal
# no_inv_input : var string penyimpan input mentah invoice pelanggan (string)
# no_inv : var int penyimpan nomor invoice pelanggan yang dicari (integer)
# idx : var int penyimpan letak baris matriks dari pelanggan terkait (integer)
# ketemu_invoice : var boolean penanda apakah invoice ditemukan di sistem (boolean)
# kebawah : var int penyimpan indeks baris pencarian (integer)
def lacak_pelanggan():
    global matriks_laundry
    
    print("\n===Lacak Status Cucian===")
    no_inv_input = input("Masukkan Nomor Invoice Anda: ")
    no_inv = int(no_inv_input)
    
    idx = -1
    ketemu_invoice = False
    kebawah = 0
    while kebawah < 1000 and ketemu_invoice == False:
        if matriks_laundry[kebawah][5] == no_inv:
            idx = kebawah
            ketemu_invoice = True
        kebawah = kebawah + 1

    if idx == -1:
        print("Maaf, data tidak ditemukan. Pastikan invoice benar.")
    else:
        print(f"\nHalo {matriks_laundry[idx][0]}, status cucian Anda saat ini: [{matriks_laundry[idx][4]}]")
    print()

# Kamus Lokal
# program_jalan : var boolean penentu program utama terus berputar atau berhenti (boolean)
# pilih : var string penyimpan input pilihan menu login/lacak/keluar (string)
# username : var string penyimpan input nama pengguna dari pegawai (string)
# password_input : var string penyimpan input mentah sandi pegawai (string)
# password : var int penyimpan angka kata sandi pegawai (integer)
def main():
    program_jalan = True
    while program_jalan == True:
        print("======================================")
        print("  SISTEM MANAJEMEN LAUNDRY UTAMA    ")
        print("======================================")
        print("1. Login Pegawai (Admin/Kasir/Owner)")
        print("2. Lacak Cucian (Menu Pelanggan)")
        print("3. Keluar Program")
        pilih = input("Pilih menu (1/2/3): ")
        
        if pilih == "1":
            username = str(input("\nMasukkan username: "))
            password_input = input("Masukkan password: ")
            password = int(password_input)
            login(username, password)
        elif pilih == "2":
            lacak_pelanggan()
        elif pilih == "3":
            print("Sampai jumpa!")
            program_jalan = False
        else:
            print("Pilihan salah.")

if __name__ == '__main__':
    main()