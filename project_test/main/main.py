from voiture import Voiture
if __name__ == '__main__':
    print('Ceci est un tout premier script Python appelé project_test.')
    # Nous ajouterons ici de futurs scripts dans les prochaines versions du projet à venir
    print('Ceci est une nouvelle fonctionnalité du projet.')

    voiture1 = Voiture()
    voiture1.prix = 12_500
    
    voiture1.afficher_infos()
