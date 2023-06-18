
# Urutan IPS - Bubble Sort
# DESCENDING = Besar - Kecil
print("Indeks Prestasi Semester (IPS)")
def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array) -i -1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

data = [3.8, 2.9, 3.3, 4.0, 2.7]
print(f"List sebelum diurutkan : {data}")

bubble_sort(data)
print(f"List setelah diurutkan : {data}")

