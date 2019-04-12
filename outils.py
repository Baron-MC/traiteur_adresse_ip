def convertisseur_octet_decimal_binaire( octet_decimal ):
    """ Convertie un octet en decimal en binaire """
    octet_binaire = str()                     # Création de la variable de type str qui va contenir la suite de bits
    octet_decimal = int( octet_decimal )
    for bit in range(7, -1, -1):              # Pour charque bit de 2^7 à 2^0
        if (octet_decimal - 2**bit) >= 0 :        # Si l'octet en decimal moins 2^bit est supérieur ou égale à 0
            octet_binaire += '1'                      # Ajout de 1
        else:                                     # Sinon
            octet_binaire += '0'                      # Ajout de 0
    return octet_binaire                      # Renvoie l'octet en binaire



def convertisseur_octet_binaire_decimal( octet_binaire ):
    """ Convertie un octet en binaire en decimal """
    octet_decimal = int()                     # Création de la variable de type int qui va contenir l'octet en decimal
    i = 0                                     # Cette variable sera incrémenté
    for bit in octet_binaire:                 # Pour chaque bit dans l'octet en binaire
        if bit == '1':                            # Si le bit est égale à 1
            octet_decimal += 2**(7 - i)               # L'octet en décimal est égale à 2^7-i
        i += 1                                    # Incrémentation de i avec i = i + 1
    return str(octet_decimal)                 # Renvoie octet_decimal au format str
