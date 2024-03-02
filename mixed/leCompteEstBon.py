import random

listTiragePossible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
listTirage = list()
nombreDemande = random.randint(101, 999)

for i in range(1, 7):
    tirage = listTiragePossible[random.randrange(0, len(listTiragePossible))]
    listTiragePossible.remove(tirage)
    listTirage.append(tirage)

print("=" * 25)
print("Nombre demandé: {}".format(nombreDemande))
print("{}".format(listTirage))
print("=" * 25)
