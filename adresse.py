import outils
import masque

def conversion_adresse_binaire( adresse_decimal ):
    """
    Conversion d'une adresse binaire en décimal
    Paramètre :
    adresse_decimal = str() format : X.X.X.X OU adresse_decimal = list() format : [ X, X, X, X]
    Renvoie :
    adresse_binaire = list()
    """
    if isinstance(adresse_decimal, str):
        adresse_decimal_split = adresse_decimal.split(".")
    else:
        adresse_decimal_split = adresse_decimal
    adresse_binaire = list()
    for octet in adresse_decimal_split:
        adresse_binaire.append( outils.convertion_octet_decimal_vers_binaire( octet ) )
    return adresse_binaire

def conversion_adresse_decimal( adresse_binaire ):
    """
    A partir d'une adresse en binaire je veux obtenir l'adresse en décimal
    Paramètre :
    adresse_res_binaire : list()
    Renvoie :
    adresse_res_decimal : list()
    """
    adresse_decimal = list()

    for octet in adresse_binaire:
        adresse_decimal.append( outils.convertion_octet_binaire_vers_decimal( octet ) )

    return adresse_decimal

def adresse_reseau( adresse_decimal, masque_decimal ):
    """
    A partir d'une adresse et d'un masque en décimal on veut avoir une adresse réseau
    Paramètre :
    adresse_decimal = list()
    masque_decimal = list()
    Renvoie :
    adresse_res_decimal = list()
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

    adresse_res_decimal = conversion_adresse_decimal( adresse_res_binaire )

    return adresse_res_decimal


def broadcast( adresse_reseau_decimal, masque_decimal ):
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
            if masque_binaire[octet][bit] == '0':
                adresse_res_binaire[octet] = adresse_res_binaire[octet][:bit] + '1'


    # On possède maintenant l'adresse de brodacast
    adresse_res_binaire[3] = adresse_res_binaire[3][: (len(adresse_res_binaire[3]) - 1)] + '1'

    # On la convertit en décimal
    adresse_diffusion_decimal = conversion_adresse_decimal( adresse_res_binaire )

    return adresse_diffusion_decimal


def adresse_plus_basse( adresse_reseau ):
    """
    A partir de l'adresse réseau renvoie l'adresse la plus basse possible du réseau
    Paramètre :
    adresse_reseau = list()
    Renvoie :
    adresse_pls_basse = list()
    """
    adresse_pls_basse = adresse_reseau
    nbr = int(adresse_pls_basse[3])
    adresse_pls_basse[3] = str( nbr + 1 )
    return adresse_pls_basse


def adresse_plus_haute( adresse_brodcast ):
    """
    Paramètre:
    adresse_broadcast = list() format = [X.X.X.X]
    Renvoie :
    adresse_pls_haute = liste() format = [X.X.X.X]
    """
    adresse_brodcast[3] = str( int(adresse_brodcast[3]) - 1 )

    adresse_pls_haute = adresse_brodcast

    return adresse_pls_haute

adresse_res = adresse_reseau(['192','168','1','94'], '24')
print(adresse_res)
adresse_pls_basse = adresse_plus_basse( adresse_res )
print(adresse_res)

print(adresse_pls_basse)