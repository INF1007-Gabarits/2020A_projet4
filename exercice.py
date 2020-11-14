import csv

# Variable globale
g = 9.80665  # m/s^2

def proprietes_eau(temperature):
    # Extraction de la base de données


    # Calcul des propriétés de l'eau à une température donnée
    # 1. Trouve l'élément le plus proche



    # 2. Calcule la valeur intermédiaire par interpolation. On assume que la température est toujours entre 0 et 40 inclusivement.
    

    return rho, mu


def regime_stockes(diametre_particule, rho_particule, rho_eau, mu_eau):
    # À compléter
    
    return V, Cd, Rep


def regime_intermediaire(Rep, diametre_particule, rho_particule, rho_eau, mu_eau):
    # À compléter
    
    return V, Cd, Rep


def calcule_vitesse(rho_particule, diametre_particule, temperature_eau):
    rho_eau, mu_eau = proprietes_eau(temperature_eau)

    # À compléter

    return vitesse_particule


if __name__ == "__main__":
    rho_particule = 2000  # kg/m^3
    diametre_particule = 1.0e-3  # m

    temperature_eau = 14.3  # degres celsius

    vitesse_particule = calcule_vitesse(rho_particule, diametre_particule, temperature_eau)
