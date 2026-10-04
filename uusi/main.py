# Tämä on ohjelman päätiedosto

from peli import Roska, MetsanOsa, Pelaaja

# Luodaan roskat
roska1 = Roska("purkka", 0.01)
roska2 = Roska("Karkkipaperi", 0.05)
roska3 = Roska("Tupakantumppi", 0.01)
roska4 = Roska("Makkarapaketti", 0.03)
roska5 = Roska("Maitotölkki", 0.025)
roska6 = Roska("Kertakäyttögrilli", 0.5)
roska7 = Roska("Limsatölkki", 0.04)
roska8 = Roska("Muovipussi", 0.02)
roska9 = Roska("Autonrengas", 3.0)
roska10 = Roska("Sukka", 0.2)

# Luodaan metsänosat
lammenranta = MetsanOsa("Lammen ranta")
aukio = MetsanOsa("Aukio")
harju = MetsanOsa("Harju")
puro = MetsanOsa("Puro")

# Lisätään roskia metsän osiin
lammenranta.lisaa_roska(roska1)
lammenranta.lisaa_roska(roska2)
lammenranta.lisaa_roska(roska3)
aukio.lisaa_roska(roska4)
aukio.lisaa_roska(roska5)
harju.lisaa_roska(roska6)
harju.lisaa_roska(roska7)
puro.lisaa_roska(roska8)
puro.lisaa_roska(roska9)
puro.lisaa_roska(roska10)

metsanosat = [lammenranta, aukio, harju, puro]

# Ensin kysytään pelaajan ikä, jotta varmistetaan ettei 
# hän ole liian nuori
ika = int(input("Kuinka vanha olet?: "))

if ika < 12:
    print("Olet alaikäinen")

else:
    print(f"Tervetuloa Aamuruskon lehto peliin!")
    nimi = input("Mikä on pelaajanimesi?: ")

    pelaaja = Pelaaja(nimi, lammenranta)

    print(f"Hei {pelaaja.nimi}!")

    # Tässä on pelin esittelyteksti
    with open("uusi/peli/introteksti.txt") as intro_file:
        print(intro_file.read())