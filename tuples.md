# Tuples

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


