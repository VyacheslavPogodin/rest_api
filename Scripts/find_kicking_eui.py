import os
import glob


PATH =  sorted(glob.glob(os.path.dirname(__file__)+'/*.log'), key=os.path.getmtime)
with open(PATH[-1], 'r', encoding='utf-8') as f:
    data = f.readlines()

LIST_EUI = []

for line in data:
    if line.find("Kicking") != -1:
        LIST_EUI.append(line[-17:])

print(''.join(set(LIST_EUI)))