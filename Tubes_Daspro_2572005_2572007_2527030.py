# File : Tubes_Daspro_2572005_2572007_2527030.py
# Penulis : Vicki Ferdinand, Nathan E E Tampilang, Claresta Jesslyn Lokanata
# Tujuan Program : Sistem Manajemen Laundry

# Kamus Data Lokal
# user : var param username input
# pw : var param password input
# username : var list penyimpan daftar username 
# password : var list penyimpan daftar password 
# auth : var boolean penanda status login 
# i : var iterasi loop
def login(user, pw):
    username = ["admin", "kasir", "owner"]
    password = [123, 321, 111]
    auth = False
    
    for i in range(len(username)):
        if user == username[i]:
            if pw == password[i]:
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

# Kamus Data Lokal
# lanjut_menu : var boolean penanda kelangsungan menu admin
# A : var list penyimpan teks pilihan menu admin
# i : var iterasi loop
# choice_input : var string input pilihan
# choice : var int hasil konversi pilihan
def menu_admin():
    lanjut_menu = True
    while lanjut_menu == True:
        print("Welcome, admin!")
        print("            ===MENU===            ")
        A = ["Update Status", "Hapus Data", "Lihat Semua Data", "Registrasi Member Baru", "Logout"]
        for i in range(len(A)):
            print(f"{i+1}. {A[i]}")
            
        choice_input = input("Pilih menu (1-5): ")
        choice = int(choice_input)
        
        if choice == 1:
            stat_update()
        elif choice == 2:
            hapus_data()
        elif choice == 3:
            lihat_data("admin")
        elif choice == 4:
            tambah_member()
        elif choice == 5:
            lanjut_menu = False
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Data Lokal
# lanjut_menu : var boolean penanda kelangsungan menu kasir
# A : var list penyimpan teks pilihan menu kasir
# i : var iterasi loop
# choice_input : var string input pilihan
# choice : var int hasil konversi pilihan
def menu_kasir():
    lanjut_menu = True
    while lanjut_menu == True:
        print("Welcome, kasir!")
        print("            ===MENU===            ")
        A = ["Tambah Data Laundry", "Lihat Data Laundry", "Cetak Struk", "Logout"]
        for i in range(len(A)):
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

# Kamus Data Lokal
# lanjut_menu : var boolean penanda kelangsungan menu owner
# A : var list penyimpan teks pilihan menu owner
# i : var iterasi loop
# choice_input : var string input pilihan
# choice : var int hasil konversi pilihan
def menu_owner():
    print("Welcome, owner!")
    lanjut_menu = True
    while lanjut_menu == True:
        print("            ===MENU===            ")
        A = ["Total Pendapatan", "Jumlah Transaksi", "Cucian Belum Selesai", "Logout"]
        for i in range(len(A)):
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

# Kamus Data Lokal
# berat : var param input berat
# layanan : var param input layanan
# member : var param status member
# tarif : var int harga dasar per kilogram
# total_sementara : var float perhitungan sebelum diskon
# potongan : var float perhitungan nilai diskon
def hitung_harga(berat, layanan, member):
    tarif = 0
    if layanan == "Reguler":
        tarif = 5000
    if layanan == "Express":
        tarif = 10000
        
    total_sementara = berat * tarif
    
    if member == 1:
        potongan = total_sementara * 10 / 100
        total_sementara = total_sementara - potongan
        
    return total_sementara

# Kamus Data Lokal
# data_ada : var boolean cek ketersediaan data 
# kebawah : var iterasi untuk pencarian baris data
# no_input : var string input nomor data 
# no : var int nomor indeks target pembaruan
# pilih_input : var string input pilihan status 
# pilih : var int pilihan status konversi
def stat_update():
    global matriks_laundry
    
    data_ada = False
    kebawah = 0
    
    while kebawah < len(matriks_laundry) and data_ada == False:
        if matriks_laundry[kebawah][0] != None:
            data_ada = True
        kebawah += 1

    if data_ada == False:
        print("Belum ada data laundry.")
    else:
        print("\n===Update Status Laundry===")
        for kebawah in range(len(matriks_laundry)):
            if matriks_laundry[kebawah][0] != None:
                print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Status: {matriks_laundry[kebawah][4]}")
                
        no_input = input("\nMasukkan nomor urut data (No) yang ingin diupdate: ")
        no = int(no_input) - 1
        
        if no >= 0 and no < len(matriks_laundry):
            if matriks_laundry[no][0] != None:
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
        else:
            print("Data tidak ditemukan atau nomor urut salah.")
    return

# Kamus Data Lokal
# data_ada : var boolean cek ketersediaan data
# kebawah : var iterasi baris
# kesamping : var iterasi kolom untuk proses penghapusan
# no_input : var string input nomor hapus
# no : var int nomor indeks target
# konfirmasi : var string penampung jawaban konfirmasi
def hapus_data():
    global matriks_laundry
    
    data_ada = False
    kebawah = 0
    while kebawah < len(matriks_laundry) and data_ada == False:
        if matriks_laundry[kebawah][0] != None:
            data_ada = True
        kebawah += 1

    if data_ada == False:
        print("Belum ada data laundry.")
    else:
        print("\n===Hapus Data Laundry===")
        for kebawah in range(len(matriks_laundry)):
            if matriks_laundry[kebawah][0] != None:
                print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Status: {matriks_laundry[kebawah][4]}")

        no_input = input("\nMasukkan nomor urut data yang ingin dihapus: ")
        no = int(no_input) - 1

        if no >= 0 and no < len(matriks_laundry):
            if matriks_laundry[no][0] != None:
                konfirmasi = input("Yakin ingin menghapus data? (y/n): ")
                if konfirmasi == 'y':
                    for kesamping in range(7):
                        matriks_laundry[no][kesamping] = None
                    print("Data berhasil dihapus.")
                elif konfirmasi == 'Y':
                    for kesamping in range(7):
                        matriks_laundry[no][kesamping] = None
                    print("Data berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Data tidak ditemukan atau nomor urut salah.")
        else:
            print("Data tidak ditemukan atau nomor urut salah.")
    return

# Kamus Data Lokal
# role : var param cek role pegawai
# data_ada : var boolean penanda data
# kebawah : var iterasi loop baris
def lihat_data(role):
    global matriks_laundry

    data_ada = False
    kebawah = 0
    while kebawah < len(matriks_laundry) and data_ada == False:
        if matriks_laundry[kebawah][0] != None:
            data_ada = True
        kebawah += 1

    if data_ada == False:
        print("Belum ada data laundry.")
    else:
        print("\n===Data Laundry===")
        for kebawah in range(len(matriks_laundry)):
            if matriks_laundry[kebawah][0] != None:
                if role == "admin":
                    print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Berat: {matriks_laundry[kebawah][1]}kg | Layanan: {matriks_laundry[kebawah][2]} | Harga: Rp{matriks_laundry[kebawah][3]} | Status: {matriks_laundry[kebawah][4]}")
                else: 
                    print(f"No.{kebawah+1} | Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Berat: {matriks_laundry[kebawah][1]}kg | Layanan: {matriks_laundry[kebawah][2]} | Harga: Rp{matriks_laundry[kebawah][3]}")
        print()
    return

# Kamus Data Lokal
# member_baru : var string input nama member baru 
# i : var iterasi sequential search array
# sudah_ada : var boolean penanda validasi pendaftaran
# indeks_kosong : var int indeks memori kosong
def tambah_member():
    global list_member
    print("\n===Registrasi Member Baru===")
    member_baru = input("Masukkan nama member baru: ")
    
    sudah_ada = False
    indeks_kosong = -1
    
    i = 0
    while i < len(list_member):
        if list_member[i] == member_baru:
            sudah_ada = True
            
        if list_member[i] == None:
            if indeks_kosong == -1:
                indeks_kosong = i
                
        i += 1
        
    if sudah_ada == True:
        print("Nama tersebut sudah terdaftar sebagai member.")
    if sudah_ada == False:
        if indeks_kosong != -1:
            list_member[indeks_kosong] = member_baru
            print(f"Berhasil! {member_baru} sekarang resmi menjadi member Indigo Laundry.")
        else:
            print("Mohon maaf, kapasitas database member sudah penuh.")
    print()
    return

# Kamus Data Lokal
# idx : var int indeks memori kosong matriks
# ketemu_kosong : var boolean flag pencarian
# kebawah : var iterasi baris matriks
# nomor : var int penampung kalkulasi nomor invoice 
# nama_input : var string input nama
# berat_input : var string input mentah berat
# nilai_berat : var float hasil convert berat
# input_layanan_valid : var boolean cek kondisi layanan
# pilih_input : var string input pilihan
# layanan_pilih : var string hasil simpanan pilihan
# i : var iterasi seq search member
# cek_member : var boolean flag pencarian member
# member : var int stat multiplier potongan
def tambah_data():
    global matriks_laundry
    global list_member
    
    idx = -1
    ketemu_kosong = False
    kebawah = 0
    while kebawah < len(matriks_laundry) and ketemu_kosong == False:
        if matriks_laundry[kebawah][0] == None:
            idx = kebawah
            ketemu_kosong = True
        kebawah += 1
            
    if idx == -1:
        print("Data penuh, tidak bisa menambah data baru.")
    else:
        nomor = 1
        for kebawah in range(len(matriks_laundry)):
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
            if pilih_input == "1":
                layanan_pilih = "Reguler"
                input_layanan_valid = True
            else:
                if pilih_input == "2":
                    layanan_pilih = "Express"
                    input_layanan_valid = True
                else:
                    print("Pilihan salah, coba lagi.")
            
        cek_member = False
        i = 0
        while i < len(list_member) and cek_member == False:
            if list_member[i] == nama_input:
                cek_member = True
            i += 1

        if cek_member == True:
            member = 1
            print(f"Sistem mendeteksi: {nama_input} adalah Member. Diskon 10% otomatis diterapkan!")
            
        if cek_member == False:
            member = 0
            print(f"Sistem mendeteksi: {nama_input} bukan Member.")

        matriks_laundry[idx][0] = nama_input
        matriks_laundry[idx][1] = nilai_berat
        matriks_laundry[idx][2] = layanan_pilih
        matriks_laundry[idx][3] = hitung_harga(nilai_berat, layanan_pilih, member)
        matriks_laundry[idx][4] = "Proses"
        matriks_laundry[idx][5] = nomor
        matriks_laundry[idx][6] = member

        print("Data berhasil dimasukkan")
    return

# Kamus Data Lokal
# no_inv_input : var string mentah nomor invoice
# no_inv : var int konversi invoice
# idx : var int indeks data yang dicari
# ketemu_invoice : var boolean flag kesesuaian
# kebawah : var iterasi pencarian baris
def cetak_struk():
    global matriks_laundry

    print("\n===Cetak Struk===")
    no_inv_input = input("Nomor Invoice: ")
    no_inv = int(no_inv_input)
    
    idx = -1
    ketemu_invoice = False
    kebawah = 0
    while kebawah < len(matriks_laundry) and ketemu_invoice == False:
        if matriks_laundry[kebawah][5] == no_inv:
            idx = kebawah
            ketemu_invoice = True
        kebawah += 1

    if idx == -1:
        print("Invoice tidak ditemukan.")
    else:
        print("\n========================================")
        print("            INDIGO LAUNDRY           ")
        print("========================================")
        print(f"Invoice  : {matriks_laundry[idx][5]}")
        if matriks_laundry[idx][6] == 1:
            print(f"Nama     : {matriks_laundry[idx][0]} (Member)")
        if matriks_laundry[idx][6] == 0:
            print(f"Nama     : {matriks_laundry[idx][0]} (Non-Member)")
            
        print(f"Berat    : {matriks_laundry[idx][1]} kg")
        print(f"Layanan  : {matriks_laundry[idx][2]}")
        print(f"Status   : {matriks_laundry[idx][4]}")
        print("----------------------------------------")
        print(f"Total    : Rp {matriks_laundry[idx][3]}")
        print("========================================")
        print()
    return

# Kamus Data Lokal
# total : var float akumulasi total pendapatan
# kebawah : var iterasi loop penelusuran baris
def pendapatan():
    global matriks_laundry

    total = 0
    for kebawah in range(len(matriks_laundry)):
        if matriks_laundry[kebawah][3] != None:
            total += matriks_laundry[kebawah][3]

    print("\n===Total Pendapatan===")
    print(f"Total Pendapatan: Rp {total}")
    print()
    return

# Kamus Data Lokal
# jumlah : var int total jumlah pesanan
# kebawah : var iterasi baris penelusuran
def jumlah_transaksi():
    global matriks_laundry

    jumlah = 0
    for kebawah in range(len(matriks_laundry)):
        if matriks_laundry[kebawah][0] != None:
            jumlah += 1

    print("\n===Jumlah Transaksi===")
    print(f"Total Transaksi: {jumlah} transaksi")
    print()
    return

# Kamus Data Lokal
# data_ada : var boolean cek if status belum diambil
# kebawah : var iterasi telusur baris
def cucian_belum_selesai():
    global matriks_laundry
    
    print("\n===Cucian Belum Selesai===")
    data_ada = False
    for kebawah in range(len(matriks_laundry)):
        if matriks_laundry[kebawah][0] != None:
            if matriks_laundry[kebawah][4] == "Proses":
                data_ada = True
                print(f"Inv: {matriks_laundry[kebawah][5]} | Nama: {matriks_laundry[kebawah][0]} | Status: {matriks_laundry[kebawah][4]}")
    
    if data_ada == False:
        print("Mantap! Semua cucian sudah selesai dan diambil.")
    print()
    return

# Kamus Data Lokal
# no_inv_input : var string input awal inv
# no_inv : var int konversi ke integer
# idx : var int penampung indeks target
# ketemu_invoice : var boolean flag pencarian
# kebawah : var iterasi penelusuran baris
def lacak_pelanggan():
    global matriks_laundry
    
    print("\n===Lacak Status Cucian===")
    no_inv_input = input("Masukkan Nomor Invoice Anda: ")
    no_inv = int(no_inv_input)
    
    idx = -1
    ketemu_invoice = False
    kebawah = 0
    while kebawah < len(matriks_laundry) and ketemu_invoice == False:
        if matriks_laundry[kebawah][5] == no_inv:
            idx = kebawah
            ketemu_invoice = True
        else:
            kebawah += 1

    if idx == -1:
        print("Maaf, data tidak ditemukan. Pastikan invoice benar.")
    else:
        print(f"\nHalo {matriks_laundry[idx][0]}, status cucian Anda saat ini: [{matriks_laundry[idx][4]}]")
    print()
    return

# Kamus Data Lokal
# program_jalan : var boolean loop program uatama
# pilih : var string menu yg dimasukkan user
# username : var string nama pengguna yang dicoba login
# password_input : var string mentah sandi
# password : var int konversi sandi
def main():
# Perintah Input
    program_jalan = True
    
# Perintah Proses
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
    # Kamus Data Global
    # NMAX : var int jumlah fix array 
    # matriks_laundry : var matriks penyimpan log
    # kebawah : var iterasi penyiapan array kosong
    # list_member : var array 1D data member
    
    NMAX = 1000
    matriks_laundry = [None] * NMAX
    for kebawah in range(NMAX):
        matriks_laundry[kebawah] = [None] * 7
        
    list_member = [None] * NMAX

    main()