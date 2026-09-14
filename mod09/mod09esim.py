
# Olio-ohjelmointi
'''
koira1_rotu = "Mastiffi"
koira1_nimi = "Wuffe"
koira1_syntymävuosi = 2022

koira2_rotu = "Bokseri"
koira2_nimi = "Sisu"
koira2_syntymävuosi = 2025

koira3_rotu = "Labradori"
koira3_nimi = "Lissu"
koira3_syntymävuosi = 2020

# pelissä eri paikat voi olla olioita
# vois kirjottaa myös sulkeilla, vähän niinku funktio, saa kirjottaa isolla kirjaimella
class Koira:
    pass

# luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö
# funktio kutsu

koira = Koira()
koira2 = Koira()

koira.nimi = "Wuffe"
koira.rotu ="Mastiffi"

koira2.nimi = "Sisu"
koira2.rotu ="Bokseri"

print("Ensimmäisen koiran nimi:", koira.nimi)
print("Ensimmäisen koiran rotu:", koira.rotu)

print("Toisen koiran nimi:", koira2.nimi)
print("Toisen koiran rotu:", koira2.rotu)

# teimme juuri luokan Koira ilman ominaisuuksia
# tämän jälkeen määrittelimme ominaisuudet yksi kerrallaan == työlästä!!!

# näin teemme oikeasti:
# Oliossa määritellään ns. tieto ja toiminta

# Koira:

# Koiran ominaisuudet
# -nimi
# -rotu
# -syntymävuosi

# Koiran toiminnot
# -hauku
# -syö
# -nuku

class Koira: # voisi olla sulkeet() vieressä, sinne sisään ei kirjoiteta parametreja

    # luokkamuuttuja
    tehty = 0

    def __init__(self,nimi,rotu,syntymävuosi, haukahdus= "Vuuh-vuuh"): # def __init__ on konstruktori
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus ="nisäkäs" # yhteinen kaikille olioille
        Koira.tehty += 1

    def hauku(self, kerrat): # luokan sisällä def ei ole funktio vaan metodi? vai funktio
        print(f"{self.nimi} tervehtii sinua")
        for i in range(kerrat):
            print(self.haukahdus)
            # ei tarvitse käyttää return
    

koira = Koira("Lissu", "Bokseri", 2020, "hau, hau")  # pitää olla samassa järj. kuin initissä
koira2 = Koira("Wuffe", "Mastiffi", 2025, "vuh, vuh") # sulkeitten sis. olevat on argumentteja
koira3 = Koira("Fifi", "Puudeli", 2015)

print(f"Koiria on nyt {Koira.tehty}.")

# matodin kutsu
koira.hauku(2)
print()
koira2.hauku(3)
print()
koira3.hauku(4)
print()

print(f"1. koiran nimi on {koira.nimi}, rotu {koira.rotu} ja syntymävuosi {koira.syntymävuosi}")
print(f"2. koiran nimi on {koira2.nimi}, rotu on {koira2.rotu} ja syntymävuosi {koira2.syntymävuosi}")

# print(koira) viittaus olioon, ei muuttuja. Ei mitään printattavaa
'''

# palyers = [
#    {
#        "name": "Player1",
#        "skill_level": 10,
#        "inventory": {"map", "knife"}
#    },
#    {
#        "name": "Player2",
#        "skill_level": 20,
#        "inventory": {"axe"}
#    }
#]

# for player in players:
#   (f"Pelaajan (player["name"]) taitotaso on (player["skill_level"]), hallussa:")
#   for item in player["inventory"]:
#       print("- (item)")

### miten tämä edellinen voitaisiin kuvata luokkana
### Esim. PELAAJA
print('---------')
info = "pelaajan tiedot"

class Player:
    def __init__(self, name, skill_level, inventory):
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory

    def show_info(self):
        print(info)
        print("Pelaajan nimi: ", self.name)
        print("Taso: ", self.skill_level)
        print("Inventaario:")
        for item in self.inventory:     #tällä saa printattua listan, joukon jne., tämä käy läpi koko listan
            print(">", item)
        print('---------')

    def add_item(self, item):
        self.inventory.add(item)
        

player1 = Player("Ulla", 10, {"map", "knife"})
player2 = Player("Matti", 20, {"axe"})

player1.show_info()
# player2.show_info()

player1.add_item("Key")
player1.show_info()

# pelaajan tiedot
# print(f"Pelaajan 1 nimi on {player1.name} ja taso on {player1.skill_level}")

# mitä ominaisuuksia pelaajan täytyy tietää? esim. paikka, invis (peliä varten) koneen ei tartte tietää noita