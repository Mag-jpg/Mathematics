import math
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour calculer les racines d'un polynôme du second degré
def calculate_roots(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root, None
    else:
        return None, None

# Fonction pour calculer les dérivées d'un polynôme du second degré
def derivative(a, b):
    return 2*a, b

# Fonction pour créer le tableau de signe et de variation
def tableau_variation(a, b, c, root1, root2):
    # Filtrer les racines qui ne sont pas None
    critical_points = [p for p in [root1, root2] if p is not None]
    critical_points.sort()
    # Calcul des valeurs aux points critiques et aux limites
    x_values = [-np.inf] + critical_points + [np.inf]
    y_values = [a*x**2 + b*x + c for x in x_values]
    # Déterminer les signes
    signs = ['+' if a > 0 else '-'] * (len(x_values) - 1)
    if len(critical_points) == 2:
        signs[1] = '-' if a > 0 else '+'
    return x_values, y_values, signs

# Affichage du tableau de signe et de variation
def print_tableau_variation(x_values, y_values, signs):
    print("Tableau de signe et de variation:")
    print("Intervalles\t| Valeur\t| Signe")
    print("------------|--------------|------")
    for i in range(len(x_values) - 1):
        print(f"{x_values[i]:>10} à {x_values[i+1]:<10} | {y_values[i]:>10} | {signs[i]:>4}")

# Tracé du polynôme et de sa dérivée
def plot_polynomial(a, b, c, root1, root2):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    dy = 2*a*x + b
    
    plt.figure(figsize=(12, 6))
    
    # Tracé du polynôme
    plt.subplot(1, 2, 1)
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    if root1 is not None:
        plt.scatter(root1, 0, color='red')
    if root2 is not None:
        plt.scatter(root2, 0, color='red')
    plt.title("Polynôme du second degré")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    
    # Tracé de la dérivée
    plt.subplot(1, 2, 2)
    plt.plot(x, dy, label=f'Dérivée: {2*a}x + {b}', color='orange')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Dérivée du polynôme")
    plt.xlabel('x')
    plt.ylabel('dy/dx')
    plt.legend()
    
    plt.show()

# Fonction principale pour exécuter le programme
def main():
    print("Entrez les coefficients du polynôme du second degré (ax^2 + bx + c):")
    a = float(input("Entrez le coefficient a: "))
    b = float(input("Entrez le coefficient b: "))
    c = float(input("Entrez le coefficient c: "))
    
    # Calcul des racines
    root1, root2 = calculate_roots(a, b, c)
    print(f"Racines: {root1}, {root2}")
    
    # Calcul des dérivées
    da, db = derivative(a, b)
    print(f"Dérivée: {da}x + {db}")
    
    # Création et affichage du tableau de signe et de variation
    x_values, y_values, signs = tableau_variation(a, b, c, root1, root2)
    print_tableau_variation(x_values, y_values, signs)
    
    # Tracé des graphes
    plot_polynomial(a, b, c, root1, root2)

# Exécution du programme principal
if __name__ == "__main__":
    main()
