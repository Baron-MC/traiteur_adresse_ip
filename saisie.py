def verification_masque( masque ):
    """ Verifie la validité du masque si ou renvoie de True sinon False """
    if 0 < int(masque) < 32:      # Si le masque est supérieur à 0 et inférieur à 32
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

def saisie_adresse_ip():
    """ Demande à l'utilisateur une adresse ip, renvoie sous forme de liste ["adress", "masque"] """
    adresse = input("Veuillez saisir une adresse en notation classless : ")  # Demande à l'utilisateur de saisir un adresse "X.X.X.X/Y"
    while verification(adresse) == False :  # Si l'adresse ne respecte pas la norme
            adresse = input("Veuillez saisir une adresse en notation classless : ")  # Demande à l'utilisateur de saisir un adresse "X.X.X.X/Y"
    adresse_masque_split = adresse.split("/") # Séparation de la chaine de caractère à partir du "/"
    return adresse_masque_split  # Renvoie l'adresse et le masque dans une liste '[adresse, masque]'
