def verification_masque( masque ):
    """ Verifie la validité du masque si ou renvoie de True sinon False """
    masque_valide = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    if masque in masque_valide:   # Si le masque fait partie des masques valides
        return True                 # Renvoie True
    return False                  # Renvoie False

def verification_adresse( adresse ):
    """ Verifie la validité de l'adresse IP si ou renvoie de True sinon False """
    if adresse.count(".") != 3:
        return False
    adresse_split = adresse.split(".")
    for octet in adresse_split:
        if ( int(octet) < 0 ) or ( int(octet) > 255 ):
            return False
    return True

def verification(adresse):
    if (adresse.find("/") == -1):
        return False
    adresse_split = adresse.split("/")
    if ( not verification_adresse(adresse_split[0]) ) or ( not verification_masque(adresse_split[1]) ):
        return False
    return True

def saisie_adresse_ip_commande():
    """ Demande à l'utilisateur une adresse ip, renvoie sous forme de liste ["adresse", "masque"] """

    adresse = input("Veuillez saisir une adresse en notation classless : ")  # Demande à l'utilisateur de saisir un adresse "X.X.X.X/Y"
    if adresse in ['STOP', 'stop', 'Stop']:
        return 'stop'

    while verification(adresse) == False :  # Si l'adresse ne respecte pas la norme
        adresse = input("Veuillez saisir une adresse en notation classless : ")  # Demande à l'utilisateur de saisir un adresse "X.X.X.X/Y"
        if adresse in ['STOP', 'stop', 'Stop']:
            return 'stop'
    adresse_masque_split = adresse.split("/") # Séparation de la chaine de caractère à partir du "/"

    return adresse_masque_split  # Renvoie l'adresse et le masque dans une liste '[adresse, masque]'
