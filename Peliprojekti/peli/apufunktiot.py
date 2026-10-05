
class Apufunktiot:

    def tulosta_paavalikko():

        print("--------------")
        print("Päävalikko")
        print("1. Aloita peli")
        print("2. Jatka")
        print("3. Lopeta")
        print("--------------")

    # Ensimmäinen tehtävä jossa pelaaja kerää huoneessa olevat roskat
    def keraa_roska(huone):  

        if len(huone.esineet) == 0:
            print("Hienoa keräsit kaikki roskat!")
            return None

        huone.tulosta_sisalto()
        valinta = input("Anna kerättävän roskan numero: ")

        if valinta.isdigit:
            numero = int(valinta)

            if numero >= 1 and numero <= len(huone.esineet):
                return huone.esineet[numero - 1]

        print("Virheellinen valinta.")
        return None

    # Tämä tulostetaan jos pelaajan syöttämä sana tai kirjaine on väärin
    def virhe():
        print("Virheellinen valinta. Yritä uudelleen.")

    # Suunnan länsi polku
    def suunta_lansi():
        print("Saavut akiolle josta on kaadettu kaikki puut")
        print("Missään ei näy yhtään eläintä")
        print("Kuuluu vain tuulen ujellus")
        print("--------------")
        print("Oikealla puolellasi on puinen kirstu")
        print("Vasemmalla näkyy iso kivenlohkare")
        print("Kumpaan suuntaan haluat mennä? (O vai V)")
        while True:

            mene = input("Anna komento: ")
            mene = mene.upper()
        
            if mene == "O":
                print(f"Valitsit suunnan oikea")
                print("--------------")
                print("Kirstu on tehty tummasta puusta") 
                print("ja siinä on metalliset yksityiskohdat")
                print("Avataksesi kirstun syötä: avaa")
                while True:
                    komento1 = input("Anna komento> ")
                    komento1 = komento1.lower()

                    if komento1 == "avaa":
                        print("--------------")
                        print("Kannen auetessa sisältä pöllähtää kimaltavaa pölyä")
                        print("Tämä saa sinut yskimään")
                        print("Yskän puuskan laannuttua katsot ympärillesi ja huomaat, että")
                        print("Metsä on maagisesti kasvanut takaisin ja eläimet ovat palanneet koteihinsa")
                        print("--------------")
                        print("Käännät katseesi kirstuun ja huomat sen pohjalla taitetun paperin")
                        print("Otat sen käteesi")
                        print("Nähdäksesi mitä paerissa lukee syötä: avaa")
                        input("Anna komento> ")
                        print("--------------")
                        print("Onneksi olkoon kirstun siällä oleva muinainen taikapöly palautti")
                        print("elämän aamuruskon lehtoon!")
                        print("Peli loppui :)")
                        break
                    else:
                        Apufunktiot.virhe()
                        break

            elif mene == "V":
                print(f"Valitsit suunnan vasen")
                print("--------------")
                print("Kivenlohkare on sammaleen peittämä")
                print("Sen takaa kuuluu outoa muminaa")
                print("Kurkistaaksesi lohkareen taakse syötä: kurkista")

                while True:

                    komento = input("Anna komento> ")
                    komento = komento.lower()

                    if komento == "kurkista":

                        print("--------------")
                        print("Lohkareen takaa paljastuu kolme ikeää oliota jotka kääntävät katseensa sinuun")
                        print("He hymyilevät ja sanovat: 'Ai katsos sieltä saapui pikkuinen ihminen'")
                        print("'Juuri sopiva syötäväksi'")
                        print("Koitat juosta karkuun, mutta ilkeät oliot saavat sinut kiinii")
                        print("Ja syövät sinut")
                        print("Peli loppui :(")

                    else:
                        Apufunktiot.virhe()
                        break

            else:
                Apufunktiot.virhe()
                break

        



