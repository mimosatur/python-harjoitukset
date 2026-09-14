# Tehtävä 1
import random

arpakuutio_lkm = int(input("Anna arpakuutioiden lukumäärä: "))

for heitto in range(arpakuutio_lkm):
    heitto = random.randint(1,6)
    print(heitto)
    
# Tehtävä 2

numbers = []

while True:
    input_number = input("Anna luku: ")
    if input_number == "":
        break
    numbers.append(int(input_number))
numbers.sort(reverse = True)

for num in range(5):
    print(numbers[num])

# Tehtävä 3

kokonaisluku = int(input("Anna kokonaisluku: "))

if kokonaisluku % 1 == 0:
    print("Luku on alkuluku")
elif kokonaisluku % kokonaisluku == 0:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")