
import os, signal
from re import findall



output = os.popen('ps aux', 'r')
#print([item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()])

for line in output:
    if line.find('ru.tpp.myrmidon.ModuleMyrmidonParser') != -1:
        PID = int(findall(r'\d+', line)[0])
        print(PID)
        os.kill(PID, signal.SIGTERM)