# TITRE DU COURS : Python for Data Science, AI & Development

## Module 1 : Les bases de python 

## A propos du cours : 
- Ce cours a été conçu pour fournir les bases de la programmation Python et de la collecte de données à ceux qui choisissent une carrière dans la science des données, l'ingénierie des données, l'IA ou le développement d'applications.

Qu'est ce qui fait de python un language grand ?
    1 - Il contient une large library standard
    2 - Pour la science des donnees, il contient les libraries scientific comme Pandas, Numpy, Scipy et Matplotlib
    3 - Pour l'IA, il a les libraries like Tensorflow, Pytorch, Keras et Scikit-learn
    4 - Il peut etre utiliser pour le Traitement du langage Naturel en utilisant NLTK(Natural Language Toolkit)


# Afficher la version du python utiliser : 
    import sys
    print(sys.version)

# Les types de donnees
    - les entiers : int -> 1, 3, 10, -4 etc.
    - les decimaux : float -> 4.2, -1.8, etc.
    - les chaines : str -> "Je suis dev python"
    - les booleans : bool -> true | false
    * Note : pour afficher le type d'une variable type(variable_name)

## Changer le type d'une expression
    - float(int) -> float   Ex : float(3) -> 3.0
    - int(float) -> int Ex : int(1.4) -> 1
    - int('int') -> int Ex : int('3') -> 3
    - int('str') -> Errors, impossible la conversion de caractere alpha en chiffre
    - int(bool) -> 0 if bool=False or 1 if bool=True
    - bool(int) -> True if int is 1 or False if int is 0

# Tuples 
    * Les Tuples sont des sequence ordonner 
    * les valeurs d'un Tuples sont entre : ( )
    * Ils peuvent prendre plusieurs type de donnees
    * Les elements sont accesible a partir de l'index
    * nous pouvons utiliser les index netagifs pour avoir acces aux valeurs d'un Tuple
    * Nous utilisont len(nom_tuple) pour avoir la taille du tuple
    * Les tuples sont immutable, i-e nous ne pouvons pas modifier un element par affectation 
    * Un tuple a plusieurs dimension, c'est un tuple qui contient d'autre tuple

**Le slicing (Extraction)**
    L'operation d'extraction d'une partie du tuple
    Exple : my_tuple = (1.3,-4,5,-3)
    my_tuple[1:2] => 1.3, -4 
    Nb : la dernier valeur entre crochet etant exclu

    Tuple multi-dimensional : Ex (2,3,1,(-1,0,'guil'), 'yaboigui', (3.1,-2, -1))

# Listes
    * comme des Tuples, les listes sont des sequences ordonner de valeur
    * les valeurs sont entre crochets [ ]
    * Ils sont mutable i-e qu'on peut reafecter la valeur d'un indice donne
    * Les listes sont concatenable L1+L2 = L ou soit avec la fonction extend
    * Les operations sur les listes sont faites par references
    
# Les dictionnaires
    * Les dictionnaire est une collection donnee cle/valeur 
    * l'acces a une valeur se fait par sa cle DICT[key] => value
    * ajouter une nouvelle pair (cle/valeur) DICT[key] = value
**Quelques methodes des dictionaries**
    - DICT.keys() : retourne une liste de toutes les cles du dict
    - DICT.values() : retourne une liste des valeurs du dict
    - del(DICT[key]) : supprimer le couple key/value de la cle key
    - key in DICT : verifie si key est dans la liste des keys de DICT
    - 
 
