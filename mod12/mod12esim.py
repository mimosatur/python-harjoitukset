class Koira:                            # luokka määrittelee luokan ominaisuudet ja toiminnallisuudet
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu

    def hauku(self):
        print(f"{self.nimi} haukkuu: Vuh vuh!")

class Kissa:
    def __init__(self, nimi, vari):
        self.nimi = nimi
        self.vari = vari

    def miau(self):
        print(f"{self.nimi} sanoo: Miau!")

class Ihminen:
    def __init__(self, nimi, kotimaa):
        self.nimi = nimi
        self.kotimaa = kotimaa

    def hauku(self):
        print(f"[{self.nimi}]: Oot tyhäm!")

koira1 = Koira("Rekku", "Labradori")    # tässä luodaan koira
kissa1 = Kissa("Misu", "Musta")
ihminen1 = Ihminen("Joa", "suomalainen")
ihminen2 = Ihminen("Jada", "suomalainen")

