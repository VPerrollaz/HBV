# Collections d'objets et boucle for

## Tuples

- Collection immutable d'objets hétérogènes.
- Syntaxe python : éléments entourés par `()`, séparés par `,`
```python
>>> type((1, 2, 3))
<class 'tuple'>
>>> type((1, 1.5, True))
<class 'tuple'>
```
- On peut accèder aux éléments dans l'ordre via l'opérateur `[]` en utilisant l'indice
```python
>>> x = (5, 2, 7)
>>> x[0]
5
>>> x[2]
7
>>> x[1]
2
```
**ATTENTION** les indices commencent à 0 : le premier élément est d'indice 0, et pour un tuple de longueur n le dernier élément est d'indice n-1.

- Surtout utiles à la volée en déstructurant
```python
>>> (x, y) = (1, 2)
>>> x
1
>>> y
2
```
**ATTENTION** On peut en fait enlever les parenthèses dans l'exemple précédent
```python
>>> x, y = 1, 2
>>> x
1
>>> y
2
```
- On peut par exemple rendre des mises à jour plus simples

Dans un autre langage
```python
>>> x = 1
>>> y = 2
>>> temp = x + y
>>> y = x - y
>>> x = temp
>>> x
3
>>> y
-1
```
Alors qu'ici
```python
>>> x, y = 1, 2
>>> x, y = x + y, x - y
>>> x
3
>>> y
-1
```

**ATTENTION** On voit ici que dans une affectation `=` toute l'expression à droite est évaluer avant d'être affectée à la partie gauche.


## Listes

- Les listes sont également des collections d'objets hétérogènes mais cette fois ci on peut la modifier, on dit qu'elle est mutable.
- La syntaxe python est là encore des éléments séparés par `,` mais entourés par `[]`.
```python
>>> type([1, 2, 3])
<class 'list'>
```
- On peut encore ici accèder aux éléments dans l'ordre via l'opérateur `[]` en utilisant l'indice de l'élément
```python
>>> ma_liste = [5, 3, 1]
>>> ma_liste[1]
3
```
- Les indices négatifs permettent de partir de la fin de la liste, le dernier élément est donc d'indice `-1`, l'avant dernier d'indice `-2` etc...
```python
>>> ma_liste = [1, 2, 3]
>>> ma_liste[-1]
3
>>> ma_liste[-3]
1
```

**ATTENTION** une tentative d'accès à un indice inexistant générera une erreur.
```python
>>> ma_liste = [1, 2, 3]
>>> ma_liste[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> ma_liste[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

- On peut utiliser l'opérateur `[]` à gauche de `=` pour remplacer un élément
```python
>>> ma_liste = [1, 2, 3]
>>> ma_liste[1] = 10
>>> ma_liste
[1, 10, 3]
```

- L'opérateur `[]` est en fait beaucoup plus riche il permet de faire du slicing pour récupérer des sous listes `ma_liste[i:j]` va créé une nouvelle liste extraite de `ma_liste` à partir des éléments d'indice allant de `i` à `j-1` (**NOTER LE DECALAGE**)
```python
>>> test = [0, 1, 2, 3, 4]
>>> test[1:3]
[1, 2]
```
**ATTENTION** si `i` n'est pas présent il est remplacé par `0` si `j` ne l'est pas il est remplacé par le nombre d'éléments.

- On a des fonctions prenant des listes en entrée, par exemple `len` qui renvoit le nombre d'éléments.
```python
>>> ma_liste = [1, 4, 2, 3]
>>> len(ma_liste)
4
```

- On a également des méthodes (appelée avec une syntaxe différente des fonctions) qui permettent de modifier la liste appelant la méthode. Par exemple `append` permet de rajouter un élément à la fin d'une liste et `pop` permet symétriquement d'en enlever.
```python
>>> ma_liste = [1, 2]
>>> ma_liste.append(3)
>>> ma_liste
[1, 2, 3]
>>> x = ma_liste.pop()
>>> ma_liste
[1, 2]
>>> x
3
```

**ATTENTION** De manière générale on essaye de faire en sorte que les fonctions ne modifient pas leurs arguments alors que les méthodes peuvent modifier les objets qui les appellent (mais là encore on évite de modifier les arguments). Ceci dit ce n'est qu'une convention.

- Pour lister toutes les méthodes accessibles par un certain objet on peut utiliser la fonction `dir`.
```python
>>> dir([1, 2])
>>> dir([1, 2])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
**ATTENTION** Les méthodes entourées par __ sont associées à des protocoles précis et leurs fonctions bien que très puissant devra être négligé dans un premier temps.

- On peut demander de l'aide sur un objet particulier via la fonction `help`. Les documentations des fonctions les plus fondamentales sont malheureusement parfois lapidaire (c.f. `extend` ) on se réfèrera  alors avec bonheur à [python.org](https://docs.python.org/3/)


## Chaines de caractères

- caractères alphanumériques séparés par `"` ou `'`, type `str` (pour string)
```python
>>> ma_chaine = "abc ABC 123"
>>> type(ma_chaine)
<class 'str'>
```

- On peut là encore accéder aux éléments via l'opérateur `[]`
```python
>>> ma_chaine = "abcde"
>>> ma_chaine[2]
'c'
```

- Pour des chaines de plusieurs lignes on utilise `"""` ou `'''` comme sépararateur
```python
>>> autre_chaine = "essai
  File "<stdin>", line 1
      autre_chaine = "essai
                              ^
SyntaxError: EOL while scanning string literal
>>> autre_chaine = """essai
... sur plusieurs
... lignes
... """
>>> print(autre_chaine)
essai
sur plusieurs
lignes
```

- conversion depuis nombres on peut passer de chaine à nombre ou même changer de types de nombres en utilisant les constructeurs de type `int`, `float` et `str`
```python
>>> x = 1
> type(x)
<class 'int'>
>>> y = float(x)
>>> y
1.0
<class 'float'>
>>> z = str(x)
>>> z
'1'
>>> type(z)
<class 'str'>
```

**ATTENTION** pour passer de chaines de caractères à nombre à virgule on fera attention au caractère de la virgule décimale qui doit être un point.
```python
>>> float("1.123")
1.123
>>> float("1,123")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '1,123'
```

- Les chaines de caractères possèdents de nombreuses méthodes permettant de les manipuler, par exemple.
```python
>>> ma_chaine = "abcde"
>>> ma_chaine.upper()
'ABCDE'
>>> ma_chaine
'abcde'
```

**ATTENTION** les chaines de caractères sont immutables comme les tuples donc ici les méthodes renvoient de nouvelles chaines.

- Parmi les méthodes les plus importantes on notera `join` et `format` qui permettent respectivement, de concaténer un conteneur de chaines avec un séparateur customisé, d'insérer les valeurs de variables dynamiquement dans une chaine pour se substituer à un bloc `{}`
```python
>>> "-*-".join(("ab", "cd", "ef", "gh"))
'ab-*-cd-*-ef-*-gh'
```
```python
>>> x = 1
>>> y = (1, 2)
>>> z = "sous chaine"
>>> "premier {} deuxième {} troisième {}".format(x, y, z)
'premier 1 deuxième (1, 2) troisième sous chaine'
```

- On pourra là encore faire `dir(str)` pour lister toutes les nombreuses méthodes utilisables avec les chaines de caractères. Puis on utilisera `help` pour voir leur utilisation.

- On peut basculer entre tuples, liste et chaines (ce dernier dans un seul sens) via les constructeurs
```python
>>> t = (1, 2, 3)
>>> list(t)
[1, 2, 3]
>>> list("abcde")
['a', 'b', 'c', 'd']
>>> tuple([1, 2, 3])
(1, 2, 3)
```

## Dictionnaires

- Certaines collections d'objets n'est pas naturellement ordonnée ou indexer par des nombres mais encode des associations entre une clef et une valeur c'est le rôle des dictionnaires de les implémenter en python. (Il y a des considérations algorithmiques profondes qu'on passera dans un premier temps)
- La syntaxe en python est des couples `clef : valeur` séparés par des virgules entourés par `{}`.
```python
>>> mon_dico = {'a' : 1, 'b' : 2, 'd' : 4}
>>> type(mon_dico)
<class 'dict'>
```
- On accède aux éléments via l'opérateur `[]` mais il faut fournir la clef à l'intérieur de ce dernier.

```python
>>> mon_dico = {'a' : 1, 'b' : 2, 'd' : 4}
>>> mon_dico["a"]
1
>>> mon_dico['d']
4
```
**ATTENTION** Là encore l'utilisation d'une clef inexistante provoque une erreur.
```python
>>> mon_dico = {'a' : 1, 'b' : 2, 'd' : 4}
>>> mon_dico["c"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
```

- on peut par contre affecter une valeur à une clef inexistante
```python
>>> mon_dico = {'a' : 1, 'b' : 2, 'd' : 4}
>>> mon_dico['c'] = 3
>>> mon_dico
>>> mon_dico["c"] } 3
{'a': 1, 'b': 2, 'd': 4, 'c': 3}
```
**ATTENTION** Il convient de ne pas utiliser l'ordre des éléments dans un dictionnaire celui-ci n'étant pas garanti constant de manière générale.

- On pourrait construire un peu plus facilement le dictionnaire précédent via le constructeur `dict` et ce de plusieurs façons.
```python
>>> dict(a=1, b=2, d=4, c=3)
{'a': 1, 'b': 2, 'd': 4, 'c': 3}
>>> dict((("a", 1), ("b", 2), ("d", 4), ("c",3)))
{'a': 1, 'b': 2, 'd': 4, 'c': 3}

```
- Là encore il paraît important de consulter les méthodes disponibles en particulier `get`.

## Boucle for

- On peut accéder aux éléments de tout conteneur de manière successive via la boucle `for`
    - tuples
    ```python
    >>> for x in (1, 2, 3):
    ...     print(x)
    ...
    1
    2
    3
    ```
    - listes
    ```python
    >>> for x in [1, 2, 3]:
    ...     print(x)
    ...
    1
    2
    3
    ```
    - chaines
    ```python
    >>> for lettre in "abcdef":
    ...     print(lettre)
    ...
    a
    b
    c
    d
    e
    f
    ```
    - dictionnaires
    ```python
    >>> mon_dico = dict(a=1, b=2, d=4, c=3)
    >>> for clef in mon_dico:
    ...     print("clef : ", clef)
    ...     print("valeur : ", mon_dico[clef])
    ...
    clef :  a
    valeur :  1
    clef :  b
    valeur :  2
    clef :  d
    valeur :  4
    clef :  c
    valeur :  3

    ```

**ATTENTION** En fait on peut itérer avec `for`  sur des objets encore plus généraux que des conteneurs : les itérables. On pourra ainsi regarder `range`, `reversed`, et les  objets renvoyés par les méthodes `keys`, `values` et `items` des dictionnaires pour les plus courants.
```python
>>> for x in range(1, 10):
...     print(x)
...
1
2
3
4
5
6
7
8
9
>>> type(range(1, 10))
<class 'range'>
>>> range(1, 10)
range(1, 10)
```

- Les boucles `for` permettent aussi de créer des nouvelles listes par transformation et/ou filtrage de conteneurs (en fait itérateurs) existant
```python
>>> nombres = [x for x in range(1, 11)]
>>> nombres
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> carres = [nbr ** 2 for nbr in nombres]
>>> carres
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> pairs = [nbr for nbr in nombres if nbr % 2 == 0]
>>> pairs
[2, 4, 6, 8, 10]
```
