# Mengurutkan Nama Buku-Insertion Sort 

array = []

def totalBuku():
    total = int(input("Masukkan Total Buku : "))
    for i in range(total):
        judul = input('Masukkan Judul Buku ke-{} : ' .format(i + 1))
        array.append(judul)

    while(True):
        total = total - 1
        if(total < 0):
            break

# Insertion Ascending
def ascending(data):
    for i in range(1, len(data)):
        item = data [i]
        j = i - 1

        while j >= 0 and data[j] > item:
            data[j +1] = data[j]
            j -= 1

        data[j + 1] = item
    
    print("\nSorting Buku Secara Ascending")
    print()
    for x in range(len(data)):
        print(f"Judul Buku ke-{x + 1} : " ,data[x])
    
    return data

# Insertion Descending
def descending(data):
    for i in range(1, len(data)):
        item = data [i]
        j = i - 1

        while j >= 0 and data[j] < item:
            data[j +1] = data[j]
            j -= 1

        data[j + 1] = item
    
    print("\nSorting Buku Secara Descending") 
    print()
    for x in range(len(data)):
        print(f"Judul Buku ke-{x + 1} : " ,data[x])
    
    return data
    
# Menu / Tampilan Utama Program
totalBuku()
print("\n<====== Urutkan ? =======>")
print("1. Insertion Ascending")
print("2. Insertion Descending")

pilih = int(input("Pilih : "))
if(pilih == 1):
    ascending(array)
elif(pilih == 2):
    descending(array)
else:
    print("Pilihan Tidak Ada")


