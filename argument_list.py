# ARGUMENT LIST

def number(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")


number(9, 5)
