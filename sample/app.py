import function

# list of dictionary
data_kontak = []

# data dummy
data_kontak.append({
    "nama": "Eri Pratama",
    "email": "pratama@email.test",
    "telepon": "123456654321"
})

# Menu program
while True:
    print(" # Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar program")

    menu = input("Pilih Menu :")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(data_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        data_kontak.append(kontak)
    elif menu == "3":
        function.delete_kontak(data_kontak)
    elif menu == "4":
        function.search_kontak(data_kontak)
    else:
        print("Menu tidak tersedia")
print("Program ditutup")
