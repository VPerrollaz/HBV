# Booléens, opérateurs logiques, control flow #

## Booléens

- Il n'y a de fait que deux booléens codant les deux valeurs logiques *Vrai* et *Faux* en python `True` et `False` le type correspondant étant `bool`.
```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

## Opérateurs manipulant les booléns

- conjonction : *Et* logique en python `and`
```python
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
```

- disjonction : *Ou* logique en python `or`
```python
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
```
- négation : *Non* logique
```python
>>> not True
False
>>> not False
True
```

**Supplement** on a également deux fonctions agissant sur des collections de booléens.

- Au moins un Vrai parmi les éléments, en python `any`
```python
>>> any((True, False, False, False, False))
True
>>> any((False, False, False, False, False))
False
```
- Tous les éléments sont Vrai, en python `all`
```python
>>> all((True, False, False, False, False))
False
>>> any((False, True, True, True, True))
True
```

## Création de booléens

- Test d'égalité entre deux valeurs, en python `==`
```python
>>> 1 == 2
False
>>> 1 == 1
True
```

**ATTENTION** on distinguera soigneusement `=` qui sert à l'affectation de variable et `==` qui sert à tester l'identité de deux valeurs.

- Test de différence entre deux valeurs, en python `!=`
```python
>>> 1 != 2
True
>>> 1 + 1 != 2
False
```

- Test d'identité entre deux objets, en python `is`
```python
>>> x = (1, 2)
>>> y = (1, 2)
>>> x == y
True
>>> x is y
False
```
```python
>>> x = (1, 2)
>>> y = x
>>> x == y
True
>>> x is y
True
```

**ATTENTION** On voit ici que deux variables peuvent référer au même objet python. L'utilisation d'une variable pour modifier l'objet sous jacent est alors observer sur l'autre variable.

- Comparaisons arithmétiques, supérieur, inférieur, inférieur ou égal, supérieur ou égal , en python `>`, `<`, `<=` et `>=`
```python
>>> 1 < 2
True
>>> 1 > 2
False
>>> 1 + 1 <= 2
True
>>> 1 + 1 >= 2
True
```

- Test d'appartenance, un élément est-il présent dans une collection, en python `in`
```python
>>> 1 in (1, 2, 3)
True
>>> 0 in (1, 2, 3)
False
```

## Utilisation de booléens

- Branchement, en python

`if` EXPRESSION BOOLEENNE `:`
    bloc
    d'instruction
    premier
    cas
`else:`
    bloc
    d'instruction
    alternatif

```python
>>> if 12345 % 3 == 0:
...     print("Divisible par 3")
... else:
...     print("Pas divisible par 3")
...
Divisible par 3
```

- Répétition d'une suite d'instructions tant qu'une expression booléenne est Vrai, en python

`while` EXPRESSION BOOLEENNE `:`
    bloc
    d'instructions
    à répéter

```python
>>> x = 13
>>> while x != 1:
...    if x % 2 == 0:
...        x = x // 2
...    else:
...        x = 3 * x + 1
...    print(x)
40
20
10
5
16
8
4
2
1
```

**ATTENTION** En python les blocs d'instructions sont démarqués par le niveau d'indentation (alignement horizontal) et non par des accolades ou autres séparateurs comme dans la majorité des autres langages de programmation.
