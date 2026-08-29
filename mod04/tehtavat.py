# Tehtävä 1

kuhanpituus = float(input("Anna kuhan pituus senttimetreinä: "))
if kuhanpituus < 37:
    print(f"Kuha on {37 - kuhanpituus} cm alamittainen. Laske se takaisin järveen.")


# tehtävä 2

hyttiluokka = str(input("Anna laivan hyttiluokka: "))
if hyttiluokka == "LUX":
    print(f"{hyttiluokka} on parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print(f"{hyttiluokka} on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print(f"{hyttiluokka} on ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print(f"{hyttiluokka} on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")


# tehtävä 3

sukupuoli = str(input("Anna biologinen sukupuolesi: "))
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen" and hemoglobiini < 117:
    print ("Hemoglobiini arvo on alhainen")
if sukupuoli == "nainen" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiini on normaali")
if sukupuoli == "nainen" and hemoglobiini >= 176:
    print("Hemoglobiini on korkea")
if sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiini on alhainen")
if sukupuoli == "mies" and 134 <= hemoglobiini < 195:
    print("Hemoglobiini on normaali")
if sukupuoli == "mies" and hemoglobiini >= 195:
    print("Hemoglobiini on korkea")

# tehtävä 4

vuosiluku = int(input("Anna vuosiluku: "))

if vuosiluku % 4 == 0 and (vuosiluku % 100 != 0 or vuosiluku % 400 == 0):
    print(f"{vuosiluku} on karkausvuosi")
