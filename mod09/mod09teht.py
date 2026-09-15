# Tehtävä 1
'''
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus  # asetetaan kyseisen muuttujan arvoksi
        self.huippunopeus = huippunopeus # km/h
        self.nopeus = 0 # voisi laittaa parametrina sulkeitten sisään nopeus=0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", "142")
print(f"Uuden auton rekisteritunnus: {auto.rekisteritunnus}, \nhuippunopeus: {auto.huippunopeus},\ntämänhetkinen nopeus: {auto.nopeus} \nja kuljettu matka: {auto.kuljettu_matka}")

# Tehtävä 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus 
        self.huippunopeus = huippunopeus # km/h
        self.nopeus = 0 
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):   # jos ei self niin se kiihdyttää kaikkia autoja, nyt vain yhtä kerrallaan
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
    
auto = Auto("ABC-123", 142)

auto.kiihdytä(30)  # tänne kutsutaan tehtävässä olevia lukuja
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Auton nopeus kiihdytyksen jälkeen: ", auto.nopeus)
auto.kiihdytä(-200)
print("Auton nopeus jarrutuksen jälkeen: ", auto.nopeus)


# Tehtävä 3

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus 
        self.huippunopeus = huippunopeus # km/h
        self.nopeus = 0 
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):   # jos ei self niin se kiihdyttää kaikkia autoja, nyt vain yhtä kerrallaan
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        # self.kuljetty_matka = self.kuljettu_matka + self.nopeus * tuntimäärä
        self.kuljettu_matka += self.nopeus * tuntimäärä

    
auto = Auto("ABC-123", 142)

auto.kiihdytä(30)  # tänne kutsutaan tehtävässä olevia lukuja
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Auton nopeus kiihdytyksen jälkeen: ", auto.nopeus)
auto.kulje(1.5)
print("Kuljettu matka 1.5h jälkeen on:", auto.kuljettu_matka)
auto.kiihdytä(-200)
print("Auton nopeus jarrutuksen jälkeen: ", auto.nopeus)
'''
# Tehtävä 4
# käytä while looppia pääohjelmassa
# lista autoille


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus 
        self.huippunopeus = huippunopeus # km/h
        self.nopeus = 0 
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):   # jos ei self niin se kiihdyttää kaikkia autoja, nyt vain yhtä kerrallaan
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        # self.kuljetty_matka = self.kuljettu_matka + self.nopeus * tuntimäärä
        self.kuljettu_matka += self.nopeus * tuntimäärä

    
auto = Auto("ABC-123", 142)
autolista = []

auto.kiihdytä(30)  # tänne kutsutaan tehtävässä olevia lukuja
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Auton nopeus kiihdytyksen jälkeen: ", auto.nopeus)
auto.kulje(1.5)
print("Kuljettu matka 1.5h jälkeen on:", auto.kuljettu_matka)
auto.kiihdytä(-200)
print("Auton nopeus jarrutuksen jälkeen: ", auto.nopeus)

