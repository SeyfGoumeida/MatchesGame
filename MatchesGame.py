# 1. Le nombre d'allumettes disposées entre les deux joueur (de 10 à 60).

nbrallumettes = 0
while not(int(nbrallumettes) >= 10 and int(nbrallumettes) <= 60):
    nbrallumettes = input("Choisir le nombre des allumettes (de 10 à 60)?   :")
    if not nbrallumettes.isdigit():
        print("Un chiffre svp (10..60) \n")
        nbrallumettes = 0

# --------------------------------------------------------------------------
# Le nombre maximal d'allumettes que l'on peut retirer.

nbrmax = 0
while (int(nbrmax) >= int(nbrallumettes) or int(nbrmax) == 0):
    nbrmax = input(
        "Choisir le nombre maximal d'allumettes que l'on peut retirer    : ")

    if not nbrmax.isdigit():
        print("Un chiffre svp (10..60) \n")
        nbrmax = 0

# --------------------------------------------------------------------------
# 3. Qui commence (0 pour le joueur et 1 pour l'ordinateur).
JOUEUR1 = input("Nom du Joueur 1 : ")
JOUEUR2 = input("Nom du Joueur 2 : ")
joueurActuel = " "  # joueur 1 à la main

while (joueurActuel != JOUEUR1 and joueurActuel != JOUEUR2):

    choix = input(
        "Choisir qui va commancer 0 pour ' %s ' ou bien 1 pour ' %s ' : " % (JOUEUR1, JOUEUR2))
    if not choix.isdigit():
        print("0 ou 1 ! \n")
    elif(int(choix) == 0):
        joueurActuel = JOUEUR1
    elif int(choix) == 1:
        joueurActuel = JOUEUR2

print(" \n")
print(" ----------------------------------------------------------------")

print("Le nombre d'allumettes disposées est                      :%s " %
      nbrallumettes)
print("Le nombre maximal d'allumettes que l'on peut retirer est  :%s " % nbrmax)
print("Le joueur qui va commencer est                            :%s " %
      joueurActuel)
print("----------------------    Are You Ready !  ----------------------\n ")


choixValides = []  # contiendra les choix valides en fonction des allumettes restants

# petite boucle principale
partieTerminee = False
while not partieTerminee:
    # on remplie la liste des choix valides
    choixValides = []
    for choixPossible in range(1, int(nbrmax)+1):
        if int(nbrallumettes) - choixPossible >= 0:
            choixValides.append(choixPossible)

    print(" ")
    print("Il y a %s allumettes" % nbrallumettes)
    print("Choix valides : ", choixValides)

    # on récupère un choix valide du joueur actuel
    choixJoueur = 0
    while choixJoueur == 0:
        choixJoueur = input("Votre choix %s ? : " % joueurActuel)
        if not choixJoueur.isdigit():
            print("Un chiffre svp ...")
            choixJoueur = 0
        elif choixJoueur.isdigit() and int(choixJoueur) not in choixValides:
            print("Choix invalide !... ")
            choixJoueur = 0

    # on vérifie si le joueur à gagné sinon la main passe

    nbrallumettes = int(nbrallumettes) - int(choixJoueur)
    if int(nbrallumettes) == 0:
        partieTerminee = True
    else:
        if joueurActuel == JOUEUR1:
            joueurActuel = JOUEUR2
        else:
            joueurActuel = JOUEUR1
if (joueurActuel == JOUEUR1):
    joueurActuel = JOUEUR2
else:
    joueurActuel = JOUEUR1

print("Félicitation  < %s >, vous avez gagné !!!" % joueurActuel)
