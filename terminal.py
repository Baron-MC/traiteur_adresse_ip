""" module terminal """


def affiche_adresse( adresse ):
    """
    Affichage d'un masque ou d'une adresse ip en décimal pointé
    Paramètre :
    adresse = list() Format : [ X , X , X , X ]
    """
    adresse_affiche = str() # Variable qui contiendra l'adresse
    # Boucle FOR pour créée la adresse
    for octet in adresse:
        adresse_affiche += ( octet + '.' )
    # Affichage avec un slicing pour enlever le dernier '.' et un retour chariot
    print( adresse_affiche[: (len(adresse_affiche) - 1) ] + '\t' )