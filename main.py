""" L'obectif du programme est de donner l'adresse de réseau, le masque, de broadcast, la plus haute
et la plus petite en partant d'une adresse ip en notation classless"""

# modules
import saisie
import adresse
import terminal

# Programme principal pour tester vos fonctions
def main():
    # Saisie d'une adresse IP
    adresse_saisie = saisie.saisie_adresse_ip()

    # Traitement
    adresse_res = adresse.adresse_reseau( adresse_saisie[0], adresse_saisie[1] )
    adresse_la_plus_basse = adresse.adresse_plus_basse( adresse_res )
    adresse_broadcast_haute = adresse.broadcast( adresse_res, adresse_saisie[1] )

    # Affichage graphique
    print("Pour l'adresse : " + adresse_saisie[0] + '/' +adresse_saisie[1])
    print("L'adresse réseau est ", end='')
    terminal.affiche_adresse( adresse_res )
    print("L'adresse la plus basse ", end='')
    terminal.affiche_adresse( adresse_la_plus_basse )
    print("L'adresse de diffusion ", end="")
    terminal.affiche_adresse(adresse_broadcast_haute)


if __name__ == '__main__':
    main()
