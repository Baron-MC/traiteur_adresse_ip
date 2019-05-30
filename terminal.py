""" module terminal """

# importation
import adresse
import saisie

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

def programme():
    # Saisie d'une adresse IP
    adresse_saisie = saisie.saisie_adresse_ip_commande()
    if adresse_saisie == 'stop':
        return 'stop'

    # Traitement
    adresse_res = adresse.adresse_reseau(adresse_saisie[0], adresse_saisie[1])
    adresse_la_plus_basse = adresse.adresse_plus_basse(adresse_res)
    adresse_broadcast = adresse.broadcast(adresse_res, adresse_saisie[1])
    adresse_la_plus_haute = adresse.adresse_plus_haute(adresse_broadcast)

    # Affichage graphique
    print("\n****   " + adresse_saisie[0] + '/' + adresse_saisie[1] + "   ****")
    print("Adresse réseau : ", end='')
    affiche_adresse(adresse_res)
    print("Adresse la plus basse : ", end='')
    affiche_adresse(adresse_la_plus_basse)
    print("Adresse de diffusion : ", end="")
    affiche_adresse(adresse_broadcast)
    print("Adresse la plus haute : ", end="")
    affiche_adresse(adresse_la_plus_haute)
