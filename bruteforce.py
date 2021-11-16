import itertools
from actions import actions
from time import time

start_time = time()


def calculate_best_wallet(actions, capital):
    # Trie les actions pour connaître la plus chère
    actions.sort(key=lambda x: x[1])
    highest_price = actions[-1][1]

    best_wallet = [[], 0, 0, 0]
    # count = 0
    # Les 2 premières lignes créent tous les wallets possibles
    # (peu importe le capital)
    for action in range(0, len(actions)+1):
        wallets_itertools = itertools.combinations(actions, action)
        # Pour chaque wallet il va soustraire au capital le
        # prix de toutes les actions comprise dans le wallet
        for wallet in wallets_itertools:
            new_capital = capital
            ROI_new_wallet = 0
            # count += 1
            for action in wallet:
                new_capital -= action[1]

            # Si le capital restant est compris entre 0 et
            # le prix de l'action la plus chere,
            # il retient le wallet comme étant viable
            if new_capital >= 0 and new_capital < highest_price:
                # Il calcule donc son ROI et l'ajoute dans ma liste de wallet
                # Cette boucle est en 2x car sinon il ne calcule
                # pas le %age correctement
                for action in wallet:
                    ROI_new_wallet += (action[2]/100)*action[1]
                monney_invested = capital - new_capital
                # Une vaiable best wallet, et la comparer avec new wallet
                if ROI_new_wallet > best_wallet[2]:
                    best_wallet = [
                        wallet,
                        monney_invested,
                        ROI_new_wallet,
                        len(wallet)
                    ]
    # print(count)
    return best_wallet  # Retourne le plus rentale


best_wallet = calculate_best_wallet(actions, 500)
# Display
print("--- %s seconds ---" % (time() - start_time))
for action in best_wallet[0]:
    print(
        action[0] +
        " --> Prix : " +
        str(action[1]) +
        "; Bénéfices après 2ans : " +
        str(action[2])
    )
print(
    "Le meilleur portefeuille est composés des " +
    str(best_wallet[3]) +
    " actions ci-dessus : "
)
print(
    "Après 2 ans, ce portefeuille raportera " +
    str(best_wallet[2]) +
    "€ avec " +
    str(best_wallet[1]) +
    "€ d'investis, soit " +
    str((best_wallet[2]/best_wallet[1])*100) +
    "% de plus value."
)
