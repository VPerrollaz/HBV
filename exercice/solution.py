# Question 1

with open("data.tsv", "r") as fichier:
    texte = fichier.read()

lignes = texte.split("\n")
table = [ligne.split("\t") for ligne in lignes]

# On sépare la première ligne qui contient les noms de colonnes
noms_colonnes = table.pop(0)

# On enlève la dernière ligne qui est vide
table.pop()

# On définit des constantes pour accéder plus lisiblement aux colonnes
ID, GENRE, NEUF, SURFACE, PIECES, QUARTIER, PRIX = range(7)

# Question 2

nb_annonces = len(table)
print("Le nombre d'annonces immobilières est : ", nb_annonces)

# Question 3

nb_valides = 0
for annonce in table:
    if annonce[QUARTIER] != "NaN":
        nb_valides = nb_valides + 1

pourcentage_quartiers = 100 * nb_valides / nb_annonces
print(
    "Pourcentage d'annonces ayant un quartier valide : ",
    round(pourcentage_quartiers, 2),
)

# Question 4

surface_totale = 0.0
nb_maisons_neuves = 0
for annonce in table:
    if annonce[GENRE] == "Maison" and annonce[NEUF] == "1":
        surface_totale = surface_totale + float(annonce[SURFACE])
        nb_maisons_neuves = nb_maisons_neuves + 1

surface_moyenne = surface_totale / nb_maisons_neuves
print("La surface moyenne des maisons neuves est : ", round(surface_moyenne, 2))

# Question 5

# On veut détecter les problèmes de conversion de nombres
from math import isnan

genres = ["Maison", "Appartement"]
ages = ["0", "1"]
nan = float("NaN")
for genre in genres:
    for age in ages:
        total_prix_m2 = 0.0
        nb_annonces_categorie = 0
        for annonce in table:
            if annonce[GENRE] == genre and annonce[NEUF] == age:
                prix = float(annonce[PRIX])
                surface = float(annonce[SURFACE])
                rapport = prix / surface
                if not isnan(rapport):
                    nb_annonces_categorie += 1
                    total_prix_m2 += rapport
        moyenne_m2 = total_prix_m2 / nb_annonces_categorie
        print(
            "Prix moyen au m2 pour les {} en {}".format(
                genre, "ancien" if age == "0" else "neuf"
            ),
            round(moyenne_m2, 2),
        )
