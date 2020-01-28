# Gestion de fichiers

## Fonction `open`

- La fonction `open` permet de passer du nom de fichier à un objet python permettant d'interagir avec le fichier.

- La syntaxe est `open(nom_de_fichier, mode)`  où `nom_de_fichier`  est une chaine de caractère permettant d'accédeder au fichier à ouvrir et `mode` est `'r'` (pour read), `'w'` (pour write) ou `'a'` (pour append).
**REMARQUE** il y a en fait d'autres modes d'ouverture mais ce sont les trois plus importants en première lecture.

- `'r'` permet de récupérer le contenu d'un fichier

- `'w'` permet d'écrire dans un fichier, si celui-ci n'existe pas il est crée sinon il est remplacer.
- `'a'` permet également d'écrire dans un fichier, si celui-ci n'existe pas il est crée mais sinon on se contente d'écrire après le contenu existant déjà.

**ATTENTION** On prendra l'habitude d'écrire la ligne fermant le fichier (via la méthode `close` ) tout de suite après avoir écrit l'ouverture.

## Ecriture

- premier contact, type renvoyer par `open` et méthodes associées
```python
>>> fichier = open("test", "w")
>>> type(fichier)
<class '_io.TextIOWrapper'>
>>> dir(fichier)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> fichier.close()
```
- La méthode la plus fondamentale pour écrire dans un fichier ouvert avec `'w'` ou `'a'` est `write` à laquelle on fournit une chaine de caractère à écrire.
```python
>>> fichier = open("test", "a")
>>> fichier.write("Essai")
5
>>> fichier.write("Suite")
5
>>> fichier.close()
```
**ATTENTION** après le code précédent le fichier `test` contient juste
```
EssaiSuite
```
Il n'y a pas d'insertion de sauts de lignes entre les appels à `write`.

- On peut insérer des sauts de ligne soit avec le caractère spécial `'\n'` soit avec une chaine de caractère avec triple entourage.
```python
>>> fichier = open("test", "w")
>>> fichier.write("Première ligne\nSeconde ligne")
28
>>> fichier.write("""
... Troisième ligne
... Quatrième ligne
... """)
33
>>> fichier.close()
```
Le fichier `test` contient maintenant

```
Première ligne
Seconde ligne
Troisième ligne
Quatrième ligne

```

## Lecture

- On a plusieurs moyen d'accéder au contenu d'un fichier ouvert avec `open` le plus élémentaire est la méthode `write` qui renvoit tout le contenu du fichier dans une chaine de caractère.
```python
>>> fichier = open("test", "r")
>>> texte = fichier.read()
>>> fichier.close()
>>> print(texte)
Première ligne
Seconde ligne
Troisième ligne
Quatrième ligne

```
**ATTENTION** une fois un fichier lu avec read il faut réaliser que le "curseur virtuel" est en fin de fichier donc une seconde lecture n'apporte rien.

```python
>>> fichier = open("test", "r")
>>> texte = fichier.read()
>>> texte_bis = fichier.read()
>>> fichier.close()
>>> print(texte)
Première ligne
Seconde ligne
Troisième ligne
Quatrième ligne

>>> print(texte_bis)

```
On peut alors soit fermer et réouvrir le fichier soit déplacer le curseur virtuel avec la méthode `seek` qui prend en argument la position voulue.
```python
>>> fichier = open("test", "r")
>>> texte = fichier.read()
>>> fichier.seek(0)
0
>>> texte_bis = fichier.read()
>>> fichier.close()
>>> print(texte)
Première ligne
Seconde ligne
Troisième ligne
Quatrième ligne

>>> print(texte_bis)
Première ligne
Seconde ligne
Troisième ligne
Quatrième ligne

```
- Pour les gros fichiers il peut se révéler pratique voir obligatoire de procéder ligne à ligne. A cette fin on peut (entre autre) utiliser le fait qu'un fichier est itérable et produit alors les lignes les unes après les autres.
```python
>>> fichier = open("test", "r")
>>> for ligne in fichier:
...     print(ligne)
...
Première ligne

Seconde ligne

Troisième ligne

Quatrième ligne


>>> fichier.close()
```
**ATTENTION** on voit que chaque ligne arrive ici avec son propre caractère de saut de ligne, comme `print` en rajoute un automatiquement on a le formattage ci-dessus par rapport au fichier de départ.

- On mentionnera aussi la méthode `readlines` qui renvoit une liste de lignes.
```python
>>> fichier = open("test", "r")
>>> lignes = fichier.readlines()
>>> fichier.close()
>>> print(lignes)
['Première ligne\n', 'Seconde ligne\n', 'Troisième ligne\n', 'Quatrième ligne\n']
```
- Finalement la méthode `readline`  (NOTER L'ABSENCE DE 's') renvoit la ligne suivante. Mais en fin de fichier elle renvoit juste une chaine vide alors qu'une ligne vide contient au moins `\n`.
```python
>>> fichier = open("test", "r")
>>> fichier.readline()
'Première ligne\n'
>>> fichier.readline()
'Seconde ligne\n'
>>> fichier.readline()
'Troisième ligne\n'
>>> fichier.readline()
'Quatrième ligne\n'
>>> fichier.readline()
''
>>> fichier.readline()
''
>>> fichier.readline()
''
>>> fichier.readline()
''
>>> fichier.readline()
''
>>> fichier.close()
```

## Différence fichier et buffer

- Description du problème
```python
>>> pour_ecrire = open("test", "w")
>>> pour_lire = open("test", "r")
>>> for i in range(1, 11):
...     pour_ecrire.write("ligne {}\n".format(i))
...     print(pour_lire.readline())
...
8
''
8
''
8
''
8
''
8
''
8
''
8
''
8
''
8
''
9
''
>>> pour_ecrire.close()
>>> pour_lire.close()
```
On ne voit que des lignes vides s'afficher avec les print et pourtant le fichier `test` contient

```python
ligne 1
ligne 2
ligne 3
ligne 4
ligne 5
ligne 6
ligne 7
ligne 8
ligne 9
ligne 10
```

- La solution du problème vient de la nature des objets renvoyés par `open`, ce sont des buffers intermédiaires et non pas directement les fichiers. Par défaut `write` écrit dans le buffer et ce n'est qu'à sa fermeture que le buffer transfère son contenu dans le fichier. On peut forcer le transfert avec la méthode `flush`.
```python
>>> pour_ecrire = open("test", "w")
>>> pour_lire = open("test", "r")
>>> for i in range(1, 11):
...     pour_ecrire.write("ligne {}\n".format(i))
...     pour_ecrire.flush()
...     print(pour_lire.readline())
...
8
ligne 1

8
ligne 2

8
ligne 3

8
ligne 4

8
ligne 5

8
ligne 6

8
ligne 7

8
ligne 8

8
ligne 9

9
ligne 10

>>> pour_ecrire.close()
>>> pour_lire.close()
```

## Remarque finale

On procédera en pratique un peut différement de ce qui a été présenté ci-dessus car si l'interpréteur rencontre une exception entre l'ouverture et la fermeture cette dernière n'est pas assurée. On utilisera alors soit une librairie comme `pathlib` que l'on couvrera plus loin dans le cours soit une syntaxe plus sophistiquée où l'interaction avec un fichier a lieu à l'intérieur d'un bloc `with` la fermeture du fichier est exécutée automatiquement en sortie de bloc.
```python
>>> with open("test", "r") as fichier:
...     for ligne in fichier:
...         print(ligne)
...
Première ligne

Seconde ligne

Troisième ligne

Quatrième ligne


```
