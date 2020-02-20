# Question 1

with open("data.tsv", "r") as fichier:
    texte = fichier.read()

lignes = texte.split("\n")
table = [ligne.split("\t") for ligne in lignes]
print("Première ligne : ", table[0])
print("Dernière ligne : ", table[-1])

# On sépare la première ligne qui contient les noms de colonnes
noms_colonnes = table.pop(0)
# On enlève la denière ligne qui est vide
table.pop()
