# Fonctions

## Concept et syntaxe de base

- L'objectif d'une fonction est d'isoler un bloc de code pour faciliter sa réutilisation et également augmenter la lisibilité du code (en effet on va à la fois nommer la fonction et on peut ajouter une doctring)
- La syntaxe élémentaire est la suivante
```python
def NOM_DE_LA_FONCTION(ARGUMENT1, ARGUMENT2, ...):
    BLOC
    D'INSTRUCTION
    DE LA
    FONCTION
    return VALEUR_DE_RETOUR_DE_LA_FONCTION
```

- On également la possibilité d'ajouter une chaine de caractères juste en dessous de la ligne de définition qui décrit la fonction cette chaine de caractère est appelée `docstring` on peut la récupérer en faisant `help(NOM_DE_LA_FONCTION)`.

- Les variables introduite dans le bloc d'instructions de la fonction existe indépendament des autres variables. On dit qu'on a deux espaces de nom le local (fonction) et le global (extérieur).

## Bonnes pratiques

- On gardera en tête qu'idéalement une fonction a une et une seul tâche précise, s'il y en a plus il convient de redécouper la fonction.
- On choisira soigneusement le nom de fonction en particulier on gardera en tête qu'on décrit une action.
- On essayera dans la majorité des cas de garder sa fonction pure.
- On fournira toujours une docstring d'une ligne au moment de créer la fonction.

## Pour aller plus loin et pièges classiques.

- Named arguments
- Valeurs par défaut
- Décorateur (ex `lru_cache`)
- Closure
- Objets
