import outils
import masque

def conversion_adresse_binaire( adresse_decimal ):
    """
    Conversion d'une adresse binaire en décimal
    Paramètre :
    adresse_decimal = str() format : X.X.X.X
    Renvoie :
    adresse_binaire = list()
    """
    adresse_decimal_split = adresse_decimal.split(".")
    adresse_binaire = list()
    for octet in adresse_decimal_split:
        adresse_binaire.append( outils.convertisseur_octet_decimal_binaire( octet ) )
    return adresse_binaire

def adresse_reseau_binaire( adresse_decimal, masque_decimal ):
    """
    A partir d'une adresse et d'un masque en décimal on veut avoir une adresse réseau
    Paramètre :
    adresse_decimal = list()
    masque_decimal = list()
    Renvoie :
    adresse_res_binaire = list()
    """
    # Variables
    adresse_binaire = conversion_adresse_binaire( adresse_decimal ) # A partir de l'adresse déciaml j'obtiens l'adresse binaire
    adresse_res_binaire = list() # Création de la variable qui contiendra l'adresse réseau en binaire
    masque_binaire =  masque.masque_en_octets_binaire( masque_decimal ) # A partir du masque en décimal j'obitens le masque en binaire

    for i in range( len(masque_binaire) ):
        octet = str()
        for y in range( len(masque_binaire[i]) ):
            if masque_binaire[i][y] == '1':
                octet += adresse_binaire[i][y]
            else:
                octet += '0'
        adresse_res_binaire.append( octet )

    return adresse_res_binaire

def adresse_reseau_decimal( adresse_res_binaire ):
    """
    A partir de l'adresse réseau en binaire je veux obtenir l'adresse réseau en décimal
    Paramètre :
    adresse_res_binaire : list()
    Renvoie :
    adresse_res_decimal : list()
    """
    adresse_res_decimal = list()

    for octet in adresse_res_binaire:
        adresse_res_decimal.append( outils.convertisseur_octet_binaire_decimal( octet ) )

    return adresse_res_decimal

def adresse_plus_haute( adresse_reseau_decimal, masque_decimal ):
    """
    A partir d'une adresse réseau en décimal et un masque en décimal renvoie l'adresse la plus haute
    Paramètres :
    adresse_reseau_decimal = list()
    masque_decimal = str
    Renvoie :
    adresse_haute
    """
    # Variables
    masque_binaire = masque.masque_en_octets_binaire( masque_decimal ) # Masque en binaire
    adresse_res_binaire = conversion_adresse_binaire( adresse_reseau_decimal ) # Adresse réseau en binaire

    # Pour chaque octet dans le masque
    for octet in range( len(masque_binaire) ):
        # Pour chaque bit dans un octet
        for bit in range( len(masque_binaire[octet]) ):
            if masque_binaire[octet][bit] == '0'
                adresse_res_binaire[octet][bit] = '1'

    adresse_broadcast = 


def adresse_plus_basse( adresse_reseau ):
    """
    A partir de l'adresse réseau renvoie l'adresse la plus basse possible du réseau
    Paramètre :
    adresse_reseau = list()
    Renvoie :
    adresse_reseau = list()
    """
    nbr = int(adresse_reseau[3])
    adresse_reseau[3] = str( nbr + 1 )
    return adresse_reseau

def affiche_adresse( adresse ):
    """
    Affichage d'un masque ou d'une adresse ip en décimal pointé
    Paramètre :
    adresse = list()
    """
    adresse_affiche = str() # Variable qui contiendra l'adresse
    # Boucle FOR pour créée la adresse
    for octet in adresse:
        adresse_affiche += ( octet + '.' )
    # Affichage avec un slicing pour enlever le dernier '.' et un retour chariot
    print( adresse_affiche[: (len(adresse_affiche) - 1) ] + '\t' )
