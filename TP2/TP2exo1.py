def perm():

    x = input("Donne une valeur : ")
    y = input("Donne une valeur : ")

    print(f"\nEntrez x: {x} \nEntrez y: {y}\n")

    print(f"Avant permutation: \n x : {x} \n y : {y}\n")

    x, y = y, x

    print(f"Après permutation: \nx : {x} \ny : {y}")

    return

print(perm())


