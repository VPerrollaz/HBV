# Listes

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
