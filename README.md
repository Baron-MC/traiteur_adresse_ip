traiteur_adresse_ip

# OBJECTIF #
  L'obejtif est d'avoir, à partir d'une adresse en classless, l'adresse réseau, le masque, la plus grande, la plus petite.

# FONCTIONS #
  Les fonctions sont répartis dans différents fichiers de manière plus "logique" pour en facilité l'usage et la compréhension de leurs effets.

  # outils.py #
    convertisseur_octet_decimal_binaire( octet_decimal ):
      |                                            |
      |  Paramètre en entré : octet en décimal     |
      |  Type : String                             |
      |  Renvoie l'octet en octet binaire          |
      |  Type : String                             |
      |____________________________________________|

    convertisseur_octet_binaire_decimal( octet_binaire ):
      |                                            |
      |  Paramètre en entré : octet en binaire     |
      |  Type : String                             |
      |  Renvoie l'octet en octet décimal          |
      |  Type : String                             |
      |____________________________________________|

  # saisie.py #
    saisie_adresse_ip():___________________________
      |                                            |
      | Ne prend aucun paramètre en entré          |
      | Renvoie : [adresse, masque ]               |
      | Type : list                                |
      |____________________________________________|

    verification(adresse):_________________________
      |                                            |
      | Prend l'adresse saisie en paramètre        |
      | Fomat : [adresse, masque]                  |
      | Type : list                                |
      | Renvoie booléen                            |
      |____________________________________________|

    verification_adresse( adresse ):_______________
      |                                            |
      | Prend en paramètre l'adresse               |
      | Format X.X.X.X                             |
      | Type : String                              |
      | Renvoie booléen                            |
      |____________________________________________|

    verification_masque( masque ):_________________
      |                                            |
      | Prend en paramètre le masque               |
      | Type : String                              |
      | Renvoie booléen                            |
      |____________________________________________|

  # adresse.py #

  # masque.py #

  # main.py #
