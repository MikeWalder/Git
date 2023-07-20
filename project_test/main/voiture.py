class Voiture:
    compteur = 0
    def __init__(self):
        self._marque = 'Peugeot'
        Voiture.compteur += 1
    
    @property
    def marque(self):
        return self._marque
    
    @marque.setter
    def marque(self, value):
        self._marque = value
    
    def afficher_marque(self):
        print(f'La marque de votre voiture est : {self.marque}')