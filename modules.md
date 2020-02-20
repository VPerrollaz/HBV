# Utilisation de modules en python

## Généralités

- Certains composants (fonctions ou classes) sont isolés dans des modules pour pouvoir être utilisé sur demande. Considérer l'exemple suivant du module `fractions`.
```python
>>> 1 / 2 + 1 / 3
0.8333333333333333
>>> import fractions
>>> fractions.Fraction(1, 2) + fractions.Fraction(1, 3)
Fraction(5, 6)
```

- On a différentes variantes de la syntaxe pour éviter de "trainer" un nom de module à rallonge. On peut ainsi juste importer un objet à l'intérieur d'un module.
```python
>>> 1 / 2 + 1 / 3
0.8333333333333333
>>> from fractions import Fraction
>>> Fraction(1, 2) + Fraction(1, 3)
Fraction(5, 6)
```

- On peut également raccourcir le nom du module.
```python
>>> import fractions as fr
>>> fr.Fraction(1, 2) + fr.Fraction(1, 3)
Fraction(5, 6)
```

- Un des avantages d'avoir tout le module sous la main est les fonctions `dir` et `help` qui permettent de découvrir les fonctionnalités disponibles.
```python
>>> import fractions
>>> dir(fractions)
['Decimal', 'Fraction', '_PyHASH_INF', '_PyHASH_MODULUS', '_RATIONAL_FORMAT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_gcd', 'gcd', 'math', 'numbers', 'operator', 're', 'sys']
```
On testera l'effet de la commande `help(fractions)` dans un interpréteur.

**ATTENTION** On évitera d'utiliser à moins d'avoir une **très** bonne raison la syntaxe.
`from module import *` qui obscurcit complétement le contenu du module et éventuellement écrase silencieusement des fonctionnalités essentielles de python.

## Module `pathlib`

- Ce module permet d'interagir plus facilement avec le système de fichier que les appels à `open`, `os` et autres fonctionnalités plus anciennes (Par contre il n'existe qu'à partir de python3.4) il permet aussi plus facilement de porter les scripts entre des systèmes windows et des systèmes unix.

- Exemple d'utilisation
```python
>>> from pathlib import Path
>>> racine = Path('.').resolve()
>>> racine
PosixPath('/home/vincent/projets/COURS/geologie')
>>> dir(racine)
['__bytes__', '__class__', '__delattr__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__fspath__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rtruediv__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__truediv__', '_accessor', '_cached_cparts', '_closed', '_cparts', '_drv', '_flavour', '_format_parsed_parts', '_from_parsed_parts', '_from_parts', '_hash', '_init', '_make_child', '_make_child_relpath', '_opener', '_parse_args', '_parts', '_pparts', '_raise_closed', '_raw_open', '_root', '_str', 'absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'glob', 'group', 'home', 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_mount', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'with_name', 'with_suffix', 'write_bytes', 'write_text']
>>> racine.is_dir()
True
>>> racine.is_file()
False
>>> for contenu in racine.glob('*'):
...     print(contenu)
...
/home/vincent/projets/COURS/geologie/logique.md
/home/vincent/projets/COURS/geologie/tuples.md
/home/vincent/projets/COURS/geologie/exercice
/home/vincent/projets/COURS/geologie/tags
/home/vincent/projets/COURS/geologie/.gitignore
/home/vincent/projets/COURS/geologie/nombres.md
/home/vincent/projets/COURS/geologie/README.md
/home/vincent/projets/COURS/geologie/TODO.md
/home/vincent/projets/COURS/geologie/fichiers.md
/home/vincent/projets/COURS/geologie/string.md
/home/vincent/projets/COURS/geologie/erreurs.md
/home/vincent/projets/COURS/geologie/listes.md
/home/vincent/projets/COURS/geologie/.git
/home/vincent/projets/COURS/geologie/fonctions.md
/home/vincent/projets/COURS/geologie/Cahier_des_charges.md
/home/vincent/projets/COURS/geologie/dictionnaires.md
/home/vincent/projets/COURS/geologie/boucle_for.md
/home/vincent/projets/COURS/geologie/modules.md
>>> todo = racine / "TODO.md"
>>> todo
PosixPath('/home/vincent/projets/COURS/geologie/TODO.md')
>>> todo.exists()
True
```

## Module `matplotlib`

## Module `csv`
