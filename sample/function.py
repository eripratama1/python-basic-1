def display_kontak(data_kontak):
    for kontak in data_kontak:
        print("====================================")
        print(f"Nama      :{kontak['nama']}")
        print(f"Email     :{kontak['email']}")
        print(f"No Telpon :{kontak['telepon']}")


def new_kontak():
    nama = input("Nama      : ")
    email = input("Email     : ")
    telepon = input("Telepon   :")
    kontak = {
        "nama": nama,
        "email": email,
        "telepon": telepon
    }
    return kontak


def delete_kontak(data_kontak):
    telepon = input("No Telepon yang akan dihapus : ")

    index = -1

    for i in range(0, len(data_kontak)):
        kontak = data_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("Data tidak ditemukan")
    else:
        del data_kontak[index]
        print("Data berhasil dihapus")


def search_kontak(data_kontak):
    searchnama = input("Nama yang dicari :")

    for kontak in data_kontak:
        nama = kontak["nama"]
        if nama.lower().find(searchnama.lower()) != -1:
            print("====================================")
            print(f"Nama      :{kontak['nama']}")
            print(f"Email     :{kontak['email']}")
            print(f"No Telpon :{kontak['telepon']}")
