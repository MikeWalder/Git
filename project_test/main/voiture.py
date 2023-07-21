class Voiture:
    compteur = 0
    def __init__(self, marque='Peugeot', prix=0):
        self._marque = marque
        self.prix = prix
        Voiture.compteur += 1
    
    @property
    def marque(self):
        return self._marque
    
    @marque.setter
    def marque(self, value):
        self._marque = value
    
    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        self._prix = value

    def afficher_infos(self):
        print(f'La marque de votre voiture est : {self.marque}')
        print(f'Prix actuel : {self.prix} €.')
        print(f'Nombre total de voitures : {Voiture.compteur}')