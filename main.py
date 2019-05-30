""" L'obectif du programme est de donner l'adresse de réseau, le masque, de broadcast, la plus haute
et la plus petite en partant d'une adresse ip en notation classless"""

# modules
import terminal


def programme_console():
    stop = False
    while stop is False:
        renvoie = terminal.programme()
        if renvoie == 'stop':
            stop = True


# Programme principal
def main():
    programme_console()


if __name__ == '__main__':
    main()
