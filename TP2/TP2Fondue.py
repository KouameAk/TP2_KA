def Fondue():
    base = 4
    fromage = 800.0
    eau = 2
    ail = 2
    pain = 400

    nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

    nfromage = fromage * nbConvives / base
    neau = eau * nbConvives / base
    nail = ail * nbConvives / base
    npain = pain * nbConvives / base

    print(f"Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :"
          f"\n- {nfromage} gr de fromage"
          f"\n- {neau} dl d'eau"
          f"\n- {nail} gousse(s) d'ail"
          f"\n- {npain} gr de pain")

print(Fondue())