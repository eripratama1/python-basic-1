# PROGRAM FOR LOOP MENGGUNAKAN TIPE DATA LIST DAN RANGE

jml_data = int(input("Masukkan jumlah data..?"))

nama = []
alamat = []
noHp = []

for i in range(0, jml_data):
    print(f"Data ke {i}")
    input_nama = input("Nama             :")
    input_alamat = input("Alamat         :")
    input_noHp = int(input("No.Handphone :"))

    nama.append(input_nama)
    alamat.append(input_alamat)
    noHp.append(input_noHp)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_alamat = alamat[i]
    data_hp = noHp[i]
    print(
        f"Nama Lengkap {data_nama} tempat tinggal {data_alamat} nomor handphone {data_hp}")
