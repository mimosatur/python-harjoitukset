# virheiden käsittely
import json
class Player:
    def __init__(self, age):
        self.age = age
        self.pisteet = 0

    def go_forward(self):
        print("Pelaaja etenee ja saa yhden pisteen.")
        self.pisteet += 1
        print(f"pisteitä kasassa nyt {self.points}")

    def info(self):
        print(f"Pelaajan ikä on {age}")

    ## Pelitilanteen lataus ja tallennus
    def save_game(self):
        try:
            with open("mod13/save.txt", "w") as file:
                data = {"age": player.age, "points": player.pointa}
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe")

    def load_game(self):
        try:
            with open("mod13/save.txt", "w") as file:
                data = json.load(file)
                # print("Ladattu tallennusdata:", data)

                self.age = data["age"]
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe")

## main loop

def start_game():
    game_running = True
    while game_running:
        command = input("Anna komento >")
        if command == "tallenna":
            player.save_game()
        elif command == "lataa":
            player.load_game()
        elif command == "etene":
            player.go_forward()
        elif command == "lopeta":
            game_running = False
        else:
            print("Virheellinen komento")


print("Peli alkaa")
age = 0
while True:
    try:
        age = int(input("Anna pelaajan ikä: "))
        break
    except ValueError: # pelkkä except on geneerinen ja ei hyvä käytäntö. halutaan tietty
        print("Virhe: antamasi ikä ei ole kokonaisluku")
# except voi olla useampia samassa silmukassa
print(f"Pelaajan ikä on: {age}")


if age > 11:
    player = Player(11)
    start_game()

else:
    print("Pelaaja liian nuori!")


print("Ohjelman suoritus loppui")






# try lohkossa käsitellään vain asioita jotka voivat mennä pieleen
#try:
    #age = int(input("Anna pelaajan ikä: "))
#except:
    #print("Virhe: antamasi ikä ei ole kokonaisluku")

#print(f"Pelaajan ikä on: {age}")
#print("Ohjelman suoritus loppui")

