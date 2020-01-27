# Dictionnaires

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
