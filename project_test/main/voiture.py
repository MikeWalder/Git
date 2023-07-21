class Voiture:
    compteur = 0
    def __init__(self, marque='Peugeot', prix=0, reduction=0):
        self._marque = marque
        self.prix = prix
        self.reduction = reduction
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
        self._prix = int(value)
    
    @property
    def reduction(self):
        return self._reduction

    @reduction.setter
    def reduction(self, value):
        self._reduction = int(value)

    @classmethod
    def demander_reduction(self):
        reduction = input('Réduction appliquée (en %) : ')
        return reduction

    def afficher_infos(self):
        print(f'La marque de votre voiture est : {self.marque}')
        print(f'Prix actuel : {self.prix} €.')
        print(f'Nombre total de voitures : {Voiture.compteur}')
    
    @staticmethod
    def appliquer_reduction(reduction, prix):
        if not reduction.isdigit() and reduction != '':
            print(f'La réduction entrée n\'est pas un entier (entré : {reduction}).')
            reduction = Voiture.demander_reduction()
            Voiture.appliquer_reduction(reduction, prix)
        elif reduction == '':
            print('Le champ est vide, réessayez.')
            reduction = Voiture.demander_reduction()
            Voiture.appliquer_reduction(reduction, prix)
        elif reduction.isdigit():
            reduction = int(reduction)
            prix = round(prix * (1 - int(reduction) / 100))
            print(f'Après réduction de {reduction}%, votre voiture a un prix de {prix} €.')