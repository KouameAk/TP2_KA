import random as rnd
def piece():
    a = rnd.randint(0,100)
    if a < 67 :
        print("c'est pile !")
    else :
        print("c'est face !")
    return


print(piece())