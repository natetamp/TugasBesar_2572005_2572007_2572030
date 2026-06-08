import getpass
# File : TUBES.py
# Program Sistem Manajemen Laundry

# Kamus Lokal
# user : Menyimpan input username yang dimasukkan pengguna untuk login (string)
# pw : Menyimpan input password yang dimasukkan pengguna untuk login (integer)
# username : List pilihan username yang valid, yaitu "admin", "kasir", dan "owner" (string)
# password : List pilihan password yang valid, sesuai dengan urutan indeks username (integer)
# auth : Status penanda apakah login berhasil/valid atau tidak (boolean)
# i : Variabel pencatat indeks perulangan untuk memeriksa data username dan password (integer)
def login(user, pw):
    username = ["admin", "kasir", "owner"]
    password = [123, 321, 111]
    auth = False
    for i in range(0, len(username), 1):
        if user == username[i] and pw == password[i]:
            user = username[i]
            auth = True
    if auth == True:
        print("Login Berhasil")
        print()
        if user == "admin":
            menu_admin()
        elif user == "kasir":
            menu_kasir()
        elif user == "owner":
            menu_owner()
    else:
        print("Login Gagal")
    return auth

# Kamus Lokal
# A : List berisi daftar teks pilihan menu khusus untuk role admin (list of string)
# i : Variabel pencatat indeks perulangan untuk menampilkan daftar menu admin ke layar (integer)
# choice : Menyimpan angka pilihan menu yang diinput oleh admin (integer)
def menu_admin():
    while True:
        print("Welcome, admin!")
        print("            ===MENU===            ")
        A = ["Update Status", "Hapus Data", "Lihat Semua Data", "Logout"]
        for i in range(0, len(A), 1):
            print(f"{i+1}. {A[i]}")
        choice = int(input("Pilih menu (1-4): "))
        if choice == 1:
            stat_update()
        elif choice == 2:
            hapus_data()
        elif choice == 3:
            lihat_data("admin")
        elif choice == 4:
            lanjut_login()
            break
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Lokal
# A : List berisi daftar teks pilihan menu khusus untuk role admin (list of string)
# i : Variabel pencatat indeks perulangan untuk menampilkan daftar menu admin ke layar (integer)
# choice : Menyimpan angka pilihan menu yang diinput oleh admin (integer)
def menu_kasir():
    while True:
        print("Welcome, kasir!")
        print("            ===MENU===            ")
        A = ["Tambah Data Laundry", "Lihat Data Laundry", "Cetak Struk", "Logout"]
        for i in range(0, len(A), 1):
            print(f"{i+1}. {A[i]}")
        choice = int(input("Pilih menu (1-4): "))
        if choice == 1:
            tambah_data()
        elif choice == 2:
            lihat_data("kasir")
        elif choice == 3:
            cetak_struk()
        elif choice == 4:
            lanjut_login()
            break
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Lokal
# A : List berisi daftar teks pilihan menu khusus untuk role admin (list of string)
# i : Variabel pencatat indeks perulangan untuk menampilkan daftar menu admin ke layar (integer)
# choice : Menyimpan angka pilihan menu yang diinput oleh admin (integer)
def menu_owner():
    print("Welcome, owner!")
    while True:
        print("            ===MENU===            ")
        A = ["Total Pendapatan", "Jumlah Transaksi", "Logout"]
        for i in range(0, len(A), 1):
            print(f"{i+1}. {A[i]}")
        choice = int(input("Pilih menu (1-3): "))
        if choice == 1:
            pendapatan()
        elif choice == 2:
            jumlah_transaksi()
        elif choice == 3:
            lanjut_login()
            break
        else:
            print("Menu tidak tersedia")
    return choice

# Kamus Lokal
# berat : Menyimpan nilai berat cucian yang dikirim dari fungsi pemanggil (float)
# layanan : Menyimpan jenis layanan ("Reguler"/"Express") yang dikirim dari fungsi pemanggil (string)
# tarif : Nilai harga per kilogram berdasarkan jenis layanan yang dipilih (integer)
def hitung_harga(berat, layanan):
    if layanan == "Reguler":
        tarif = 5000
    else: 
        tarif = 10000
    return berat * tarif

# Kamus Lokal
# data_ada : Status penanda apakah ada data transaksi yang tersimpan di dalam list/array (boolean)
# i : Variabel pencatat indeks perulangan untuk mengecek keberadaan data dan menampilkan tabel (integer)
# no : Menyimpan nomor urut data laundry pilihan user yang diubah ke bentuk indeks dengan dikurangi 1 (integer)
# pilih : Menyimpan angka pilihan status baru (1-3) yang diinput oleh pengguna (integer)
def stat_update():
    global nama, status, invoice
    
    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Update Status Laundry===")
    print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Status':<15}")
    print("-" * 55)
    for i in range(len(nama)):
        if nama[i] is not None:
            print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(status[i]):<15}")
    no = int(input("\nMasukkan nomor urut data yang ingin diupdate: ")) - 1
    
    if 0 <= no < len(nama) and nama[no] is not None:
        print("Pilih status baru:")
        print("1. Proses")
        print("2. Selesai")
        print("3. Diambil")
        pilih = int(input("Pilih (1-3): "))
        
        if pilih == 1:
            status[no] = "Proses"
        elif pilih == 2:
            status[no] = "Selesai"
        elif pilih == 3:
            status[no] = "Diambil"
        else:
            print("Pilihan tidak valid.")
            return
            
        print(f"Status {nama[no]} berhasil diupdate menjadi {status[no]}.")
    else:
        print("Data tidak ditemukan atau nomor urut salah.")
    return

# Kamus Lokal
# data_ada : Status penanda apakah ada data transaksi yang tersimpan di dalam list/array (boolean)
# i : Variabel pencatat indeks perulangan untuk mengecek keberadaan data dan menampilkan tabel (integer)
# no : Menyimpan nomor urut data laundry pilihan user yang diubah ke bentuk indeks dengan dikurangi 1 (integer)
# konfirmasi : Menyimpan input jawaban ('y'=yes atau 'n'=no) untuk mengonfirmasi proses penghapusan data (string)
def hapus_data():
    global nama, berat, layanan, harga, status, invoice
    
    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Hapus Data Laundry===")
    print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Status':<15}")
    print("-" * 55)
    for i in range(len(nama)):
        if nama[i] is not None:
            print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(status[i]):<15}")

    no = int(input("\nMasukkan nomor urut data yang ingin dihapus: ")) - 1

    if 0 <= no < len(nama) and nama[no] is not None:
        konfirmasi = input(f"Yakin ingin menghapus data atas nama {nama[no]}? (y/n): ")
        if konfirmasi.lower() == 'y':
            nama[no] = None
            berat[no] = None
            layanan[no] = None
            harga[no] = None
            status[no] = None
            invoice[no] = None
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Data tidak ditemukan atau nomor urut salah.")
    return

# Kamus Lokal
# role : Parameter pembawa teks role pengguna ("admin"/"kasir") untuk menentukan format kolom tabel (string)
# data_ada : Status penanda apakah ada data transaksi yang valid untuk ditampilkan (boolean)
# i : Variabel pencatat indeks perulangan untuk memeriksa data dan mencetak baris data laundry (integer)
def lihat_data(role):
    global nama, berat, layanan, harga, status, invoice

    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Data Laundry===")
    if role == "admin":
        print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Berat':>8} {'Layanan':<12} {'Harga':>12} {'Status':<12}")
        print("-" * 85)
        for i in range(len(nama)):
            if nama[i] is not None:
                print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(berat[i]):>7}kg {layanan[i]:<12} Rp{harga[i]:>10,.0f} {str(status[i]):<12}")
    else: 
        print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Berat':>8} {'Layanan':<12} {'Harga':>12}")
        print("-" * 75)
        for i in range(len(nama)):
            if nama[i] is not None:
                print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(berat[i]):>7}kg {layanan[i]:<12} Rp{harga[i]:>10,.0f}")
    print()
    return

# Kamus Lokal
# pelanggan_input : Menyimpan input mentah jumlah pelanggan dari user sebelum divalidasi angka (string)
# pelanggan : Menyimpan jumlah pelanggan yang diinput setelah berhasil diubah menjadi angka (integer)
# i : Variabel pencatat indeks perulangan untuk memproses input data sebanyak jumlah pelanggan (integer)
# idx : Menyimpan posisi indeks kosong yang ditemukan di dalam array (integer)
# pilih_input : Menyimpan input mentah pilihan layanan sebelum divalidasi angka (string)
# pilih : Menyimpan angka pilihan jenis layanan (1 untuk Reguler, 2 untuk Express) (integer)
def tambah_data():
    global nama, berat, layanan, harga, status, invoice
    # Kamus Lokal
    # i : Variabel pencatat indeks perulangan untuk mencari elemen array yang masih bernilai None (integer)
    def cari_indeks_kosong():
        for i in range(len(nama)):
            if nama[i] is None:
                return i
        return -1

    # Kamus Lokal
    # nomor : Variabel pencatat nomor invoice terbaru yang nilainya terus bertambah di setiap perulangan (integer)
    # i : Variabel pencatat indeks perulangan untuk mengecek seluruh isi list invoice yang sudah terisi (integer)
    def invoice_baru():
        nomor = 1
        for i in range(len(invoice)):
            if invoice[i] is not None:
                nomor = invoice[i] + 1
        return nomor

    while True:
        idx = cari_indeks_kosong()
        if idx == -1:
            print("Data penuh, tidak bisa menambah data baru.")
            return

        nama[idx] = str(input("Nama  : "))
        
        if nama[idx] == "":
            print("Input tidak boleh kosong!")
            continue
        
        while True:
            berat_input = input("Berat Cucian (kg): ").strip()
                
            if berat_input == "":
                print("Input tidak boleh kosong!")
                continue
            
            if berat_input.isalpha():
                print("Input tidak valid.")
                continue
                
            nilai_berat = float(berat_input)
                
            if nilai_berat <= 0:
                    print("Berat harus lebih dari 0.")
                    continue
                    
            berat[idx] = nilai_berat
                
            print("===Pilihan Layanan===")
            print("   1. Reguler   ")
            print("   2. Express   ")
            print("===Input Laundry===")
                
            while True:
                pilih_input = input("Pilih layanan (1/2): ").strip()
                if pilih_input.isdigit():
                    pilih = int(pilih_input)
                    if pilih == 1:
                        layanan[idx] = "Reguler"
                        break
                    elif pilih == 2:
                        layanan[idx] = "Express"
                        break
                    else:
                        print("Layanan tidak valid. Pilih 1 atau 2.")
                else:
                    print("Input tidak valid. Masukkan angka 1 atau 2!")

            harga[idx] = hitung_harga(berat[idx], layanan[idx])
            status[idx] = "Proses"
            invoice[idx] = invoice_baru()

            print("Data berhasil dimasukkan")
            break
        return

# Kamus Lokal
# data_ada : Status penanda apakah ada data transaksi yang tersimpan di dalam list (boolean)
# i : Variabel pencatat indeks perulangan untuk memeriksa data awal dan mencari nomor invoice (integer)
# no_inv_input : Menyimpan input mentah nomor invoice dari user sebelum divalidasi angka (string)
# no_inv : Menyimpan nomor invoice yang dicari setelah berhasil diubah menjadi angka (integer)
# idx : Menyimpan posisi indeks dari nomor invoice yang cocok, bernilai -1 jika tidak ketemu (integer)
def cetak_struk():
    global nama, berat, layanan, harga, status, invoice

    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Cetak Struk===")
    print("Masukkan nomor invoice yang ingin dicetak struknya.")

    print(f"{'No':<5} {'Invoice':<12} {'Nama':<20}")
    print("-" * 40)
    for i in range(len(nama)):
        if nama[i] is not None:
            print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20}")

    no_inv_input = input("\nNomor Invoice: ").strip()

    if no_inv_input.isdigit():
        no_inv = int(no_inv_input)
        
        idx = -1
        for i in range(len(invoice)):
            if invoice[i] == no_inv:
                idx = i
                break

        if idx == -1:
            print("Invoice tidak ditemukan.")
            return

        print()
        print("=" * 40)
        print("         NGORTIS LAUNDRY          ")
        print("=" * 40)
        print(f"Invoice  : {invoice[idx]}")
        print(f"Nama     : {nama[idx]}")
        print(f"Berat    : {berat[idx]} kg")
        print(f"Layanan  : {layanan[idx]}")
        print(f"Status   : {status[idx]}")
        print("-" * 40)
        print(f"Total    : Rp {harga[idx]:,.0f}")
        print("=" * 40)
        print("      Terima kasih sudah mencuci   ")
        print("         di Ngortis Laundry!     ")
        print("=" * 40)
        print()
    else:
        print("Input tidak valid. Masukkan nomor invoice dalam bentuk angka!")

# Kamus Lokal
# total : Variabel penampung hasil penjumlahan seluruh harga transaksi laundry yang valid (integer)
# i : Variabel pencatat indeks perulangan untuk menelusuri data harga di dalam list (integer)
def pendapatan():
    global harga, status

    total = 0
    for i in range(len(harga)):
        if harga[i] is not None:
            total += harga[i]

    print("\n===Total Pendapatan===")
    print(f"Total Pendapatan (semua transaksi): Rp {total:,.0f}")
    print()
    return

# Kamus Lokal
# jumlah : Variabel penghitung total banyaknya transaksi laundry yang aktif/tidak kosong (integer)
# i : Variabel pencatat indeks perulangan untuk mengecek elemen list nama yang tidak kosong (integer)
def jumlah_transaksi():
    global nama

    jumlah = 0
    for i in range(len(nama)):
        if nama[i] is not None:
            jumlah += 1

    print("\n===Jumlah Transaksi===")
    print(f"Total Transaksi: {jumlah} transaksi")
    print()
    return

# Kamus Lokal
# pilih : Menyimpan teks input pilihan konfirmasi dari user, diubah ke huruf kecil dan dihapus spasinya (string)
def logout():
    print("Logout berhasil, apakah ingin melanjutkan? (ketik 1 untuk login kembali)")
    pilih = input("Pilihan: ").strip()
    if pilih == "1":
        return True
    else:
        print("Apakah anda yakin ingin menyelesaikan pendataan? (y/n)")
        pilih = input("Pilihan: ").lower()
        if pilih == "n":
            return True
        else:
            print("Terima kasih telah menggunakan Ngortis Laundry. Sampai jumpa!")
            return False

# Kamus Data
# username : Menyimpan teks input nama pengguna untuk proses login (string)
# password : Menyimpan input angka kata sandi untuk proses login (integer)
def main():
    while True:
        print("             NGORTIS LAUNDRY           ")
        print("            ===LOGIN PAGE===           ")
        username = str(input("Masukkan username: ")).lower()
        password_input = getpass.getpass("Masukkan password: ")
        if password_input.isdigit():
            password = int(password_input)
        else:
            password = 0
        if login(username, password):
            break
    return


def lanjut_login():
    if logout():
        main()


if __name__ == '__main__':
    invoice = 1000 * [None]
    nama = 1000 * [None]
    layanan = 1000 * [None]
    berat = 1000 * [None]
    harga = 1000 * [None]
    status = 1000 * [None]
    main()