# Chaines de caractères

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
