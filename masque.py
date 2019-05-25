import outils

def masque_en_octets_binaire( masque ):
    """ A partir du masque de la notation classless
    la fonction renvoie le masque en binaire """
    masque = int(masque)
    masque_en_octets = list()
    octet = str()
    for i in range(4):
        for y in range(8):
            if masque <= 0:
                octet += '0'
            else:
                octet += '1'
            masque -= 1
        masque_en_octets.append(octet)
        octet = str()
    return masque_en_octets

def masque_en_octets_decimal( masque ):
    """ A partir du masque de la notation classless
    la fonction renvoie le masque en decimal """
    masque_decimal = list()
    masque_binaire = masque_en_octets_binaire( masque )
    for octet in masque_binaire:
        octet_decimal = outils.convertisseur_octet_binaire_decimal( octet )
        masque_decimal.append( octet_decimal )
    return masque_decimal
