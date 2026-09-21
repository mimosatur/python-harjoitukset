# Tehtävä 1

class Hissi:
    def __init__(self, nimi, alin_kerros, ylin_kerros):  #muista aina self
        self.nykyinen_kerros = alin_kerros
        self.alinkerros = alin_kerros
        self.ylinkerros = ylin_kerros
        self.nimi = nimi

    def siirry_kerrokseen(self, kohdekerros): #muista aina self
        print(f"Siirrytään kerrokseen {kohdekerros}")
        if kohdekerros > self.nykyinen_kerros:   # toimii myös ilman if ja elif
            while self.nykyinen_kerros < kohdekerros:
                self.kerros_ylös()
        elif kohdekerros < self.nykyinen_kerros:  # ei tarvii elif, jos haluat tulostaa yksittäisen kerroksen tarvitaan if ja elif
            while self.nykyinen_kerros > kohdekerros:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylinkerros:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alinkerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")


class Talo:
    def __init__(self, hissien_lkm, alin_kerros, ylin_kerros):
        self.hissit = []
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(f"numero {i + 1}", alin_kerros, ylin_kerros)  # lisätään indeksi hissin numeroksi
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, numero, kohdekerros):
        # hissi numero 1 on listalla indeksissä 0
        print(f"Ajetaan hissiä {numero} kerrokseen {kohdekerros}")
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)

    def palohälyytys(self):  # vaikka ei anneta parametrejä niin tarttee self. Ilman sitä ei voi käyttää luokan ominaisuuksia
        print("Palohälyytys!!!")
        # muuttuja h viittaa vuorollaan jokaiseen hissiolioon listalla
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin_kerros)


talo = Talo(2, 12, 3)

#talo.hissit[0].siirry_kerrokseen(5)
talo.aja_hissiä(1,5)
talo.aja_hissiä(1,7)
talo.aja_hissiä(3,2)
talo.aja_hissiä(3,8)

talo.palohälyytys()


# Testejä pelkällä hissiluokalla suoraan pääohjelmasta
'''
hissi1 = Hissi("Pääaula1",1,12)
hissi2 = Hissi("Henkilökunta",5,20)
#print(hissi1.nykyinen_kerros)
#print(hissi2.nykyinen_kerros)
hissi1.siirry_kerrokseen(8)
hissi2.siirry_kerrokseen(15)
hissi1.siirry_kerrokseen(5)
hissi2.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(1)
'''