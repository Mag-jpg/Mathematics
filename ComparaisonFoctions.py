
import numpy as np
import matplotlib.pyplot as plt

# Définir les fonctions et leurs dérivées
def fonction_affine(x, a, b):
    return a * x + b

def derivee_fonction_affine(a):
    return a

def polynome_second_degre(x, a, b, c):
    return a * x**2 + b * x + c

def derivee_polynome_second_degre(x, a, b):
    return 2 * a * x + b

def polynome_troisieme_degre(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def derivee_polynome_troisieme_degre(x, a, b, c):
    return 3 * a * x**2 + 2 * b * x + c

def fonction_exponentielle(x, a):
    return a * np.exp(x)

def derivee_fonction_exponentielle(x, a):
    return a * np.exp(x)

# Générer des points pour le graphique
x = np.linspace(-10, 10, 400)

# Saisie des coefficients par l'utilisateur
def saisir_coefficients():
    print("Saisissez les coefficients de la fonction. Séparez-les par des espaces.")
    coefs = input("Coefficients : ").strip().split()
    coefs = [float(c) for c in coefs]
    return coefs

# Choix de la fonction par l'utilisateur
def choisir_fonction():
    print("Choisissez le type de fonction :")
    print("1. Fonction affine (ax + b)")
    print("2. Polynôme de second degré (ax^2 + bx + c)")
    print("3. Polynôme de troisième degré (ax^3 + bx^2 + cx + d)")
    print("4. Fonction exponentielle (a * exp(x))")
    
    choix = input("Votre choix (1/2/3/4) : ").strip()
    return choix

# Fonction pour poser la question et vérifier la réponse
def verifier_type_fonction(coefs, type_fonction):
    types_de_fonctions = {
        "affine": (2,),
        "second_degre": (3,),
        "troisieme_degre": (4,),
        "exponentielle": (1,)
    }

    print("Voici les coefficients de la fonction :")
    print(coefs)
    
    reponse = input("De quel type de fonction s'agit-il ? (affine, second_degre, troisieme_degre, exponentielle) : ").strip().lower()

    if type_fonction == reponse:
        print("Bonne réponse !")
    else:
        print("Mauvaise réponse. Essayez encore.")

# Programme principal
def main():
    nb_fonctions = int(input("Combien de fonctions voulez-vous comparer ? "))

    fonctions = []
    types_fonctions = []

    for i in range(nb_fonctions):
        print(f"Fonction {i + 1} :")
        choix = choisir_fonction()
        coefs = saisir_coefficients()
        types_fonctions.append(choix)
        fonctions.append(coefs)
    
    plt.figure(figsize=(14, 10))

    for i, (choix, coefs) in enumerate(zip(types_fonctions, fonctions)):
        if choix == '1':
            y = fonction_affine(x, *coefs)
            dy = np.full_like(x, derivee_fonction_affine(coefs[0]))
            label = 'Fonction Affine'
            couleur = 'blue'
        elif choix == '2':
            y = polynome_second_degre(x, *coefs)
            dy = derivee_polynome_second_degre(x, *coefs[:2])
            label = 'Polynôme de Second Degré'
            couleur = 'green'
        elif choix == '3':
            y = polynome_troisieme_degre(x, *coefs)
            dy = derivee_polynome_troisieme_degre(x, *coefs[:3])
            label = 'Polynôme de Troisième Degré'
            couleur = 'orange'
        elif choix == '4':
            y = fonction_exponentielle(x, *coefs)
            dy = derivee_fonction_exponentielle(x, *coefs)
            label = 'Fonction Exponentielle'
            couleur = 'red'
        else:
            print("Choix invalide.")
            return

        plt.subplot(1, 2, 1)
        plt.plot(x, y, label=f'Fonction {i + 1}: {label}', color=couleur)
        
        plt.subplot(1, 2, 2)
        plt.plot(x, dy, label=f'Dérivée {i + 1}', linestyle='--', color=couleur)

    plt.subplot(1, 2, 1)
    plt.title('Fonctions')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title('Dérivées')
    plt.legend()

    plt.tight_layout()
    plt.show()

    for coefs, type_fonction in zip(fonctions, types_fonctions):
        verifier_type_fonction(coefs, type_fonction)

    # Vérification des positions relatives des fonctions
    if nb_fonctions == 2:
        y1 = eval_fonction(x, types_fonctions[0], fonctions[0])
        y2 = eval_fonction(x, types_fonctions[1], fonctions[1])
        
        if np.all(y1 > y2):
            print("La première fonction est au-dessus de la deuxième sur tout l'intervalle.")
        elif np.all(y1 < y2):
            print("La deuxième fonction est au-dessus de la première sur tout l'intervalle.")
        else:
            print("Les fonctions se croisent dans l'intervalle.")

# Fonction pour évaluer les fonctions en fonction de leur type
def eval_fonction(x, choix, coefs):
    if choix == '1':
        return fonction_affine(x, *coefs)
    elif choix == '2':
        return polynome_second_degre(x, *coefs)
    elif choix == '3':
        return polynome_troisieme_degre(x, *coefs)
    elif choix == '4':
        return fonction_exponentielle(x, *coefs)

if __name__ == "__main__":
    main()
