
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

    def suunnan_valinta():
        print("Olet saapunut metsän reunalle")
        print("Edessäsi on kolmen eri polkua, itä, pohjoinen ja länsi")
        print("Mitä pitkin haluaisit lähteä auttamaan metsän jälleenrakennuksessa?")