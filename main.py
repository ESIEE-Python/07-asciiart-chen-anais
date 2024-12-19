"""
contient deux fonctions secondaires qui retournent la liste de tuples 
encodant une chaîne de caractères passée en argument 
selon un algorithme itératif ou récurssif
une fonction principale main qui appelle les deux fonctions secondaires 
"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1500)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c=[s[0]]
    o=[1]
    for i in range(1,len(s)) :
        if s[i] == s[i-1] :
            o[-1] += 1
        else :
            c.append(s[i])
            o.append(1)
    final = []
    for item in zip(c,o) :
        final.append(item)
    return final


def artcode_r(chaine):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme récursif

    Args:
        chaine (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    if chaine== "":

        return []
    # recherche nombre de caractères identiques au premier
    lettre = chaine[0]
    occurence =1
    for item in chaine[1:]:
        if item == lettre:
            occurence += 1
        else:
            return [(lettre,occurence)]+ artcode_r(chaine[occurence:])

    return [(lettre,occurence)]
    # appel récursif

#### Fonction principale


def main():
    """
    appelle les fonctions secondaires
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
