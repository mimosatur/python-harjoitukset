
class Apufunktiot:


    def inventaario():
        reppu = []
        esine = input("Anna esine: ")
        reppu.append(esine)
        return

    def tulosta():
        return print(reppu)

    def lopetus():
        return print("Nähdään ensikerralla!")


    def tulosta_paavalikko():
        print("--------------")
        print("Päävalikko")
        print("1. Aloita peli")
        print("2. Jatka")
        print("3. Lopeta")
        print("--------------")


    def suunta_lansi():
        print("--------------")
        print("Saavut akiolle josta on kaadettu kaikki puut")
        print("Missään ei näy yhtään eläintä")
        print("Kuuluu vain tuulen ujellus")
        print("--------------")
        print("Oikealla puolellasi on puinen kirstu")
        print("Vasemmalla näkyy iso kivenlohkare")
        print("Kumpaan suuntaan haluat mennä?")
        mene = input("Anna komento> ")
        print(f"Valitsit suunnan {mene}")
        if mene == "oikea":
            print("--------------")
            print("Kirstu on tehty tummasta puusta") 
            print("ja siinä on metalliset yksityiskohdat")
            print("Avataksesi kirstun syötä: avaa")
            while True:
                komento1 = input("Anna komento> ")

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
                    print("Virheellinen vastaus. Yritä uudelleen.")

        elif mene == "vasen":
            print("--------------")
            print("Kivenlohkare on sammaleen peittämä")
            print("Sen takaa kuuluu outoa muminaa")
            print("Kurkistaaksesi lohkareen taakse syötä: kurkista")
            input("Anna komento> ")
            print("--------------")
            print("Lohkareen takaa paljastuu kolme ikeää oliota jotka kääntävät katseensa sinuun")
            print("He hymyilevät ja sanovat: 'Ai katsos sieltä saapui pikkuinen ihminen'")
            print("'Juuri sopiva syötäväksi'")
            print("Koitat juosta karkuun, mutta ilkeät oliot saavat sinut kiinii")
            print("Ja syövät sinut")
            print("Peli loppui :(")

        



