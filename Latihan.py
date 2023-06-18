# Menambah Data Mahasiswa
def addMahasiswa():
    jumlah = int(input("Jumlah Mahasiswa : "))
    mahasiswa = []
    while (jumlah > 0):
        nama = input("Nama Mahasiswa : ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah < 0):
            break

# Hapus Data Mahasiswa
def removeMahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    print("Data Mahasiswa %s" %arraymahasiswa)
    mahasiswa.remove(input("Hapus Mahasiswa : "))
    print("Data Mahasiswa %s" %mahasiswa)
    panggil(mahasiswa)

# Urutkan Data Mahasiswa
def ascMahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(arraymahasiswa)

# Lihat Data Mahasiswa
def viewMahasiswa (arrayMahasiswa): 
    mahasiswa = arrayMahasiswa
    for x in mahasiswa: 
        print("Nama Mahasiswa : %s" %x)
    panggil (arrayMahasiswa)

# Menu / Tampilan Utama Program
def panggil(arraymahasiswa):
    print("\n<====== Data Mahasiswa =======>")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("\nPilih : "))
    if(pilih==1):
        addMahasiswa()
    elif(pilih==2):
        removeMahasiswa(arraymahasiswa)
    elif(pilih==3):
        ascMahasiswa(arraymahasiswa)
    elif(pilih==4):
        viewMahasiswa(arraymahasiswa)
    elif(pilih==5):
        print("Selesai")
    else:
        print("Selesai")

# Memanggil fungsi
arraymahasiswa = []
panggil (arraymahasiswa)




