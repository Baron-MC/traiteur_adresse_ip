""" L'obectif du programme est de donner l'adresse de réseau, le masque, de broadcast, la plus haute
                             et la plus petite en partant d'une adresse ip en notation classless"""


def saisie_adresse_ip():
    """cette fonction demande à l'utilisateur de saisire une adresse ip en notation classless au format :      X.X.X.X/Y
    Conditions à remplirs :
        - un octets n'est pas plus est compris dans l'intervalle 0 < 255
        - un adresse ip s'écrit en décimal pointé
        - la séparation ip / masque se fait avec un slash
        - un masque ne peut négatif, nul ou égale à 32 
    Si ce n'est pas le cas alors le programme boucle"""
    adresse = input("Veuillez saisir une adresse en notation classless : ")


# Programme principal pour tester vos fonctions
def main():
    pass

if __name__ == '__main__':
    main()