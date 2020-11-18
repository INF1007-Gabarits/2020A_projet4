class Noeud(object):
    def __init__(self, nom):
        # TODO: à implémenter
        pass
    
    def ajoute_voisin(self, noeud):
        # TODO: à implémenter
        pass

    def __str__(self):
        # TODO: à implémenter
        pass
    
    def __repr__(self):
        # TODO: à implémenter
        pass


class Graphe(object):
    def __init__(self):
        # TODO: à implémenter
        pass
                
    def ajoute_noeud(self, noeud: Noeud, aretes: list):
        # TODO: à implémenter
        pass

    def ajoute_arete(self, noeud1, noeud2):
        # TODO: à implémenter
        pass

    def trouve_chemin(self, debut: Noeud, fin: Noeud, chemin=None):
        # TODO: à implémenter
        pass


if __name__ == "__main__":
    # Création des noeuds
    a, b, c, d, e = Noeud('A'), Noeud('B'), Noeud('C'), Noeud('D'), Noeud('E')

    # Création du graphe
    graphe = Graphe()

    # Ajout des noeuds et des arêtes au graphe
    graphe.ajoute_noeud(noeud=a, aretes=[b, d])
    graphe.ajoute_noeud(noeud=b, aretes=[c])
    graphe.ajoute_noeud(noeud=c, aretes=[d, e])
    graphe.ajoute_noeud(noeud=d, aretes=[a, c, e])
    graphe.ajoute_noeud(noeud=e, aretes=[d])

    # Affichage de quelques noeuds
    print(a)
    print(d)
    print(e)

    # Recherche d'un chemin entre le noeud B et le noeud A
    chemin = graphe.trouve_chemin(b, a)
    print(f'Le chemin entre B et A est {chemin}')

    # Recherche d'un chemin entre le noeud E et le noeud B
    chemin = graphe.trouve_chemin(e, b)
    print(f'Le chemin entre E et B est {chemin}')
