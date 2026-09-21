# Assosiaatio, jatkoa edellisestä
class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi  # parametrina saatu nimi tallennetaan olion ominaisuudeksi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)

class Hoitola:

    def __init__(self):
        # tässä assosiaatio listan avulla
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)  # tällä ei lisätä koiraa listaan vaan luodaan viittaus siihen
        # pääsee nyt käsiksi koirien (olion) ominaisuuksiin
        print(koira.nimi + " Kirjattu sisään")
        # hoitola pääsee nyt kutsumaan koiran metodeja
        # tämäkin on assosiaatio eli hoitola "tuntee" toisen olion
        print(koira.hauku(2)) # ilman print none poistuu


# pääohjelma

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()
hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)

koira2 = koira1 # Sijoitetaan aina oikealta vasemmalle. Viitaus ensimmäiseen koiraan poistuu ja kummatkin muuttujat viittaavat samaan olioon
print()
koira2.hauku(2)

# Luodaan kolmas koira ja sijoitetaan suoraan hoitolaan
hoitola.koira_sisään(Koira("Bella", 2016, "hau, hau"))

# olion ominaisuuksiin voidaan viitata Pythonissa myös suoraan. Näin ei voi tehdä kaikissa kielissä
hoitola.koirat[0].hauku(2)


## Lista on myös olio ja siihen viitataan muuttujilla
'''
def muokkaa_listaa(muokkaa_listaa):
    muokkaa_listaa.append(6)

lista = [1,5,8]
print(lista)
muokkaa_listaa(lista)
print(lista)
'''