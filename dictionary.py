# TIPE DATA DICTIONARY

customer = {"Name": "Pratama", "Age": 31, "Address": "Kaltim"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "P-Dev"  # menambah
customer["Name"] = "Eri Pratama"  # mengubah

del customer["Age"]  # MENGHAPUS

for key, value in customer.items():
    print(f"{key}:{value}")
