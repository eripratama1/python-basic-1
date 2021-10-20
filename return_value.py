# ARGUMENT LIST & RETURN VALUE

def number(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)


list_angka, total = number(10, 10, 20, 25)
print(f"Total {list_angka}= {total}")
