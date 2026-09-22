# Tehtävä 1

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_kirja(self):
        print(f"Kirjan nimi: {self.nimi}\nkirjailija: {self.kirjailija}\nsivumäärä {self.sivumaara} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_lehti(self):
        print(f"Lehden nimi: {self.nimi}\npäätoimittaja: {self.paatoimittaja}")

kirja = Kirja("Hytti n:o 6","Rosa Liksom",200)
print()
kirja.tulosta_kirja()
print()
lehti = Lehti("Aku Ankka", "Aki Hyppä")
lehti.tulosta_lehti()
print()


# Tehtävä 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rakisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):   
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        # self.kuljetty_matka = self.kuljettu_matka + self.nopeus * tuntimäärä
        self.kuljettu_matka += self.nopeus * tuntimäärä

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)


sahkoauto = ("ABC-15", 180, 52.5)
sahkoauto.nopeus = 60
sahkoauto.kulje(3)
print(f"Matkamittarilukema: {sahkoauto.kuljettu_matka}")
polttomoottoriauto = ("ACD-123", 165, 32.3)
polttomoottoriauto.nopeus = 60
polttomoottoriauto.kulje(3)