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

## Lecture

## Différence fichier et buffer
