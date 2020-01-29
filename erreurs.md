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

**ATTENTION** Le lecteur attentif aurait pu ici se dire qu'on pouvait tester avant de faire la division si le dénominateur est nul ce qui est vrai le choix d'utiliser des exceptions est guidé par l'heuristique, qu'il est souvent plus commode de demander pardon que demander la permission. En fait on pourrait remarquer qu'un test de validation à priori consiste souvent à faire de manière plus compliquée l'opération avant de la refaire ensuite. Ainsi si le fichier contient en fait
```python
12 3
14 2
15 3
douze 0
123 1
21 3
```
L'erreur ne viendra plus de la division par zéro mais pas l'opération qui demande de passe de la chaine `'12'` à un `float`, il est nettement plus délicat ici d'écrire un test de validation pour la conversion d'une chaine en `float` le plus simple est d'essayer de le faire et d'intercepter l'erreur éventuelle.

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

- La syntaxe élémentaire pour les exceptions est la suivante
```python
try:
    TENTATIVE
    QUI POURRAIT
    ECHOUER
except EXCEPTION1:
    PREMIERE
    ALTERNATIVE
except EXCEPTION2:
    DEUXIEME
    ALTERNATIVE
```

Il y a en fait des possibilités supplémentaires (clause `else` et `finally`) on pourra aller lire [ceci](https://docs.python.org/fr/3.5/tutorial/errors.html) pour la documentation complète.

- Pour reprendre l'exemple précédent avec un fichier `data` contenant
```python
12 1
123 2
132 5
douze 123
12 0
```
On va procéder ainsi
```python
>>> with open("data", "r") as fichier:
...     lignes = fichier.readlines()
...
>>> with open("resultat", "w") as fichier:
...     for ligne in lignes:
...             try:
...                     x, y = ligne.split()
...                     num, den = float(x), float(y)
...                     fichier.write("{} {} {}\n".format(num, den, num / den))
...             except ZeroDivisionError:
...                     fichier.write("{} {} NaN\n".format(num, den))
...             except ValueError:
...                     pass
...
14
15
15
12
```
Le fichier `resultat` contient maintenant
```python
12.0 1.0 12.0
123.0 2.0 61.5
132.0 5.0 26.4
12.0 0.0 NaN
```
