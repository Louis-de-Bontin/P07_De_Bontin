# Je deal avec des list et non des dictionnaires, 
# lors de l'écriture du code il faudra remplacer les keys par des indexs
from actions import actions

def calcul_best_wallet(actions, capital):
    for  action in actions:
        euro_won = action[2]/action[1]
        action.append(euro_won)

    i = 0
    best_wallet = [[], 0, 0, 0]
    while i <= capital:
        new_capital = i
        new_wallet = []
        actions_candidates = []
        for action in actions:
            if action[1] <= new_capital:
                actions_candidates.append(action)
        actions_candidates.sort(key = lambda x: x[3], reverse=True)

        ROI_new_wallet = 0
        if len(actions_candidates) > 0:
            for action_candidate in actions_candidates:
                if action_candidate[1] <= new_capital:
                    new_wallet.append(action_candidate)
                    new_capital -= action_candidate[1]
                    ROI_new_wallet += action[2]

            if len(new_wallet) > 0:
                monney_invested = capital - new_capital
                if ROI_new_wallet > best_wallet[2]:
                    best_wallet = [new_wallet, monney_invested, ROI_new_wallet, len(new_wallet)]
        i+=1
    
    return best_wallet

# calcul_best_wallet(actions, 100)
print(calcul_best_wallet(actions, 500))