# Boucle for

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
