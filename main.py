""" L'obectif du programme est de donner l'adresse de réseau, le masque, de broadcast, la plus haute
et la plus petite en partant d'une adresse ip en notation classless"""

# modules
import saisie
import adresse

# Programme principal pour tester vos fonctions
def main():
    # Saisie d'une adresse IP
    adresse_saisie = saisie.saisie_adresse_ip()

    # Traitement
    adresse_res_binaire = adresse.adresse_reseau_binaire( adresse_saisie[0], adresse_saisie[1] )
    adresse_res_decimal = adresse.adresse_reseau_decimal( adresse_res_binaire )

    # Affichage graphique
    print("Pour l'adresse : " + adresse_saisie[0] + '/' +adresse_saisie[1])
    print("L'adresse réseau est ", end='')
    adresse.affiche_adresse( adresse_res_decimal )

if __name__ == '__main__':
    main()
