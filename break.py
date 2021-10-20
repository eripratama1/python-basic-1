# BREAK

for i in range(1, 1000):
    if i % 50 == 0:
        break
    print(i)

while True:
    data = input("Data :")
    if data == "x":
        break
    print(data)
