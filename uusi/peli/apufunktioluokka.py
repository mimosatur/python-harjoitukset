# Pelissä tarvittavat funktiot
class Apufunktio:

    def tulosta_valikko():
        print("Mitä haluat tehdä?")
        print("1. Näytä nykyinen metsänosa")
        print("2. Näytä nykyisen metsänosan roskat")
        print("3. Siirry toiseen metsänosaan")
        print("4. Kerää roska")
        print("5. Näytä keräämäsi roskat")
        print("6. Näytä kaikki metsänosat")
        print("7. Näytä ohje")
        print("0. Lopeta")

    def tulosta_metsanosat(metsanosat):
        print("Metsänosat:")
        for numero in range(len(metsanosat)):
            metsanosa = metsanosat[numero]
            print(f"{numero + 1}. {metsanosa.nimi}")

    def valitse_metsanosa(metsanosat):
        Apufunktio.tulosta_metsanosat(metsanosat)
        valinta = input("Anna metsänosan numero: ")

        if valinta.isdigit():
            numero = int(valinta)

            if numero >= 1 and numero <= len(metsanosat):
                return metsanosat[numero -1]

        print("virheellinen valinta.")
        return None