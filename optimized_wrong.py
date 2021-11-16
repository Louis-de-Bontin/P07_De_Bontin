from actions import actions
import csv
from time import time

# start_time = time()


def calcul_best_wallet(actions, capital):
    for action in actions:
        euro_won = action[2]/action[1]
        action.append(euro_won)

    i = 0
    best_wallet = [[], 0, 0, 0]
    while i <= capital:
        new_capital = i
        new_wallet = [[], 0, 0, 0]

        ROI_new_wallet = 0
        monney_invested = 0
        for action_candidate in actions:
            if action_candidate[1] <= new_capital:
                new_wallet[0].append(action_candidate)
                new_capital -= action_candidate[1]
                ROI_new_wallet += (action_candidate[2]/100)*action_candidate[1]
                monney_invested += action_candidate[1]
                new_wallet[1] = monney_invested
                new_wallet[2] = ROI_new_wallet
                new_wallet[3] = len(new_wallet[0])

        # if len(new_wallet) > 0:
        if ROI_new_wallet > best_wallet[2] and len(new_wallet) > 0:
            best_wallet = new_wallet
        i += 1

    return best_wallet


def read_files(files_names):
    actions = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for action in csvreader_file:
            if action[1] != "price":
                action[1] = float(action[1])
                action[2] = float(action[2])
                if action[1] > 0 and action[2] > 0:
                    actions.append(action)
    return actions


actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
best_wallet = calcul_best_wallet(actions, 500)
for action in best_wallet[0]:
    print(
        action[0] +
        " --> Prix : " +
        str(action[1]) +
        " Bénéfices après 2ans : " +
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
