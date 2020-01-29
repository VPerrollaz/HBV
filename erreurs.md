# Gestion des erreurs

## Mise en situation

On imagine que le fichier `data` contient deux colonnes de nombres et qu'on veut écrire dans la troisième colonne le resultat de la division entre les deux. On peut imaginer procéder de la façon suivante.

```python
>>> with open("data", "r") as fichier:
...     lignes } fichier.readlines()
...
>>> with open("resultat", "w") as fichier:
...     for ligne in lignes:
...             x, y } ligne.split()
...             num, den } float(x), float(y)
...             fichier.write("ù= ù= ù=".format(num, den, num /den))
...
12
12
12
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  ZeroDivisionError: float division by zero

```

On voit qu'on tombe sur une erreur à la quatrième ligne et toute l'exécution est fini. Le problème vient de `data` qui contient en fait
```python
12 3
14 2
15 3
12 0
123 1
21 3
```
et donc la division par zéro provoque une erreur ou plus spécifiquement en python la lévée d'une exception. Une façon de régler le problème est ici de demander à python d'essayer de faire une opération tout en se préparant à intercepter une éventuelle exception.
**ATTENTION** on a différents types d'exception suivant la situation qui l'a provoqué par exemple.

```python
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> ls = list()
>>> ls[0]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
IndexError: list index out of range

```
On pourra aller voir [ici](https://docs.python.org/3/library/exceptions.html) pour la liste de toutes les exceptions prédéfinies.

## Syntaxe de l'interception
