from operator import itemgetter
from random import randint
from actions import actions

def build_wallet (actions, capital):
    # Tri des actions pour avoir accès à la moins chère facilement, puis déclarations de mes variables
    sorted_actions = sorted(actions, key = lambda x: x[1])
    wallet = []
    sum_pourcentage = 0

    # Tant que le capital est superieux ou égale au prix de l'action la moins chère
    while capital >= sorted_actions[0][1]:

        rand_number = randint(0, len(sorted_actions)-1) # Je crée un chiffre aléatoire compris entre 0 et le nombre d'actions encore achetables

        if capital >= sorted_actions[rand_number][1]:
            wallet.append(sorted_actions.pop(rand_number)) # J'ajoute une action au portefeuille
            capital -= wallet[-1][1] # Je soustrais la valueur de cette action

    # Je calcule le ROI d'un portefeuille
    for action in wallet:
        sum_pourcentage += action[2]
    renta = sum_pourcentage/len(wallet)

    return wallet, renta

def sort_wallet(actions, capital):
    wallets = []
    best_ROI = 0
    while True:
        wallets.append(build_wallet(actions, capital))
        wallets.sort(key=lambda x:x[1])
        if wallets[-1][1] > best_ROI:
            best_ROI = wallets[-1][1]
            print("Pour l'instant, le meilleur portefeuille est : \n")
            for action in wallets[-1][0]:
                print(action[0])
            print("Avec un ROI de : \n")
            print(best_ROI)   
    
sort_wallet(actions, 600)