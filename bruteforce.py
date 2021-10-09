import itertools
from actions import actions

def calculate_best_wallet(actions, capital):

    best_wallet = [[], 0, 0, 0, 0]
    for action in range(0, len(actions)+1): # Les 2 premières lignes créent tous les wallets possibles (peu importe le capital)
        wallets_itertools = itertools.combinations(actions, action)
        for wallet in wallets_itertools: # Pour chaque wallet il va soustraire au capital le pris de toutes les actions comprise dans le wallet
            new_capital = capital
            for action in wallet:
                new_capital -= action[1]
                # Peut être indenter le if, et comment on sait pour 114
            # if new_capital < 0:
            #     break
            if new_capital == 0 and new_capital <114: #Si le capital restant est compris entre 0 et le priw de l'action la plus chere, il retient le wallet comme étant viable
                sum_pourcentage = 0
                for action in wallet: # Il calcule donc son ROI et l'ajoute dans ma liste de wallet # Cette boucle est en 2x car sinon il ne calcule pas le %age correctement
                    sum_pourcentage += action[2]
                pourcentage = (sum_pourcentage/len(wallet))
                monney_invested = capital - new_capital
                roi = monney_invested * (pourcentage/100)
                # Une vaiable best wallet, et la comparer avec new wallet
                if roi > best_wallet[3]:
                    best_wallet = [wallet, monney_invested, pourcentage, roi, len(wallet)]

    return best_wallet # Retourne le plus rentale


best_wallet = calculate_best_wallet(actions, 500)
print(
    "Le meilleur portefeuille est composés des " +
    str(best_wallet[4]) +
    " actions suivantes : "
)
for action in best_wallet[0]:
    print(
        action[0] +
        " --> Prix : " +
        str(action[1]) +
        " Bénéfices après 2ans : " +
        str(action[2])
    )
print(
    "Après 2 ans, ce portefeuille raportera " +
    str(best_wallet[3]) +
    "€ avec " +
    str(best_wallet[1]) +
    "€ d'investis, soit " +
    str(best_wallet[2]) +
    "% de gains."
)
