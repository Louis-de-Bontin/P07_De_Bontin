import pandas as pd
import csv
from actions import actions
import time

start = time.time()

def read_files(files_names):
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        actions_csv = []
        for action in csvreader_file:
            if action[1] != "price" and action[0] not in (action[0] for action in actions_csv):
                action[1] = round(float(action[1]))
                action[2] = round(float(action[2]))
                if action[1] > 0 and action[2] > 0:
                    actions_csv.append(action)
    print(len(actions_csv))
    return actions_csv

def get_best_folio(actions, capital):
    folio = []
    matrice_sad = pd.DataFrame([[(float(0), folio) for i in range(0,capital+1)]], index=["action0"])
    cap=1
    count = 0
    previous_action = "action0"
    for action in actions:
        new_row = pd.DataFrame([[(float(0), []) for i in range(0,capital+1)]], index=[action[0]])
        matrice_sad = matrice_sad.append(new_row, ignore_index=False)
        while cap<=capital:
            count+=1
            action_price = float(action[1])
            action_pourcent = float(action[2])
            # Je regarde combien vaut mon folio avec cette action plus le reste (colone cap-action_price) avec la case du dessus
            if action != "action0" and action_price <= cap:
                folio = [action]
                last_best_folio = matrice_sad.at[previous_action, cap]
                # print(last_best_folio)
                last_best_ROI = last_best_folio[0]
                new_folio_ROI = (action_price*action_pourcent/100) + matrice_sad.at[previous_action, cap-action_price][0]
                for share in matrice_sad.at[previous_action, cap-action_price][1]:
                    folio.append(share)
                if last_best_ROI >= new_folio_ROI:
                    matrice_sad.at[action[0], cap] = last_best_folio
                elif last_best_ROI < new_folio_ROI:
                    matrice_sad.at[action[0], cap] = (new_folio_ROI, folio)
            cap+=1
        curent_time = time.time()
        print(curent_time - start)
        previous_action = action[0]
        cap=0
    return matrice_sad.iloc[-1][500]

actions_csv = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])

best_folio = get_best_folio(actions_csv, 500)
end = time.time()
total_cost = 0
for action in best_folio[1]:
    print(action[0] + " --> Prix : " + str(action[1]) + "; Bénéfices après 2ans : " + str(action[2]))
    total_cost += action[1]
print("Le meilleur porte-feuille est composé des " + str(len(best_folio[1])) + " actions ci-dessus :")
print("Le cout total de ce wallet est de : " + str(total_cost) + "€.")
print("Après 2ans, il aurait rapporté " + str(best_folio[0]) + "€.")
print("Soit une plus value de " + str(best_folio[0]/total_cost*100) + "%.")

print(f"Runtime of the program is {end - start}")
