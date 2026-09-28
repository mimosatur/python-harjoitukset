from elaimet import Koira, Kissa, Ihminen

koira1 = Koira("Rekku", "Labradori")
kissa1 = Kissa("Misu", "Musta")
ihminen1 = Ihminen("Joa", "suomalainen")

koira1.hauku()
kissa1.miau()
ihminen1.hauku() # [Joa]

# tiedosto = moduuli
# kansio = paketti

from peli import Pelaaja