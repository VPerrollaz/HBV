# Fonctions

## Concept et syntaxe de base

- L'objectif d'une fonction est d'isoler un bloc de code pour faciliter sa réutilisation et également augmenter la lisibilité du code (en effet on va à la fois nommer la fonction et on peut ajouter une doctring)
- La syntaxe est la suivante
```python
def NOM_DE_LA_FONCTION(ARGUMENT1, ARGUMENT2, ...):
    BLOC
    D'INSTRUCTION
    DE LA
    FONCTION
    return VALEUR_DE_RETOUR_DE_LA_FONCTION
```

- Notion de scope.

## Bonnes pratiques

- On gardera en tête qu'idéalement une fonction a une et une seul tâche précise, s'il y en a plus il convient de redécouper la fonction.
- On choisira soigneusement le nom de fonction en particulier on gardera en tête qu'on décrit une action.
- On essayera dans la majorité des cas de garder sa fonction pure.
- On fournira toujours une docstring d'une ligne au moment de créer la fonction.

## Pour aller plus loin
