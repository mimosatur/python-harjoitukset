# Mod 08 esimerkki

# monikko, tuple
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")

print("Ensimmäinen viikonpäivä on", viikonpäivät[0])

# käytetään monikkoa aina kun mahdollista, jos tarvitsee muokata sisältöä -> käytä listaa

# monikko monikon sisällä (kaksi- tai moniulotteinen monikko
print("\narkipäivät ja viikonlopun päivät ovat omissa monikoissaan samassa monikossa: ")
viikonpäivät_v2 = (("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai"))
print(viikonpäivät_v2)
print("Arkipäiviä ovat", viikonpäivät_v2[0]) #kaikki arkipäivät
print("Ensimmäinen viikonpäivä on", viikonpäivät_v2[0][0])
# tärkein, monikko toimii kuin lista, mutta sitä ei pysty muuttamaan

# yksittäisten arvojen purku muuttujiin

(eka, toka, kolmas, neljäs, viides, kuudes, seitsemäs) = viikonpäivät
print(eka, kolmas, viides)
