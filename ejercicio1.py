import random
def aleatorio10():

    miLista = []
    for indice in range(1, 11):
        miLista.append(random.randint(10, 100))
    print("Mi lista actual es: {}".format(miLista))

def borrarrep(lista1):
    newli=set(lista1)
    newli2=list(newli)
    print("Mi lista actual es: {}".format(newli2))

a=aleatorio10()
b=borrarrep(a)
