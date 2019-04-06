def verification_masque( masque ):
    """ Verifie la validité du masque si ou renvoie de True sinon False """
    if 0 < int(masque) < 32:
        return True
    return False

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

def saisie_adresse_ip():
    """ Demande à l'utilisateur une adresse ip, renvoie sous forme de liste ["adress", "masque"] """
    adresse = input("Veuillez saisir une adresse en notation classless : ")
    while verification(adresse) == False :
            adresse = input("Veuillez saisir une adresse en notation classless : ")
    adresse_masque_split = adresse.split("/")
    return adresse_masque_split
