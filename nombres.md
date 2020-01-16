# Manipulations numériques #

## Opérateurs arithmétiques ##

- addition `+`
```python
>>> 1 + 1
2
```
- soustraction `-`
```python
>>> 3 - 2
1
```
- multiplication `*`
```python
>>> 2 * 3
6
```
- puissance `**`

**Attention** `^` existe aussi mais il s'agit du ou exclusif logique binaire
```python
>>> 2 ** 4
16
>>> 2 ^ 4
6
```
- division `/`
```python
>>> 3 / 2
1.5
```
- quotient dans la divison euclidienne `//`
```python
>>> 3 // 2
1
```
- reste dans la divison euclidienne `%`
```python
>>> 3 % 2
1
```

## Deux types de nombres ##

- Nativement en python on a les nombres entiers `int` et les nombres à virgules `float` (techniquement nombres à virgule flottante)

```python
>>> type(1)
<class 'int'>
>>> type(1.5)
<class 'float'>
```

- **Remarque** on notera ici l'utilisation de la fonction `type` qui permet de récupérer le type de n'importe quel objet python.

- **Attention** la virgule numérique est dénotée par `.` en python. La virgule `,` est un séparateur pour les `tuple`, `list`...

- On notera que les opérations arithmétiques homogènes respectent le type (sauf pour la division de deux `int` qui renvoit un `float`)

- En cas de mélange de type par contre on récupère un `float`
```python
>>> type(1 + 1.1)
<class 'float'>
>>> type(2 * 2.5)
<class 'float'>
```

- On peut rentrer les `float` via la notation scientifique
```python
>>> 12.3e5
1230000.0
```
- **Attention** les opérations avec les `int` sont toujours exactes en python mais avec les `float` on a des erreurs d'arrondis.
```python
>>> (1e8 + 1e-8) / 1e8
1.0000000000000002
>>> (1e1 + 1e-10) / 1e10
1.0
```
