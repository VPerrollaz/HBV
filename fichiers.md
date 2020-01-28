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
