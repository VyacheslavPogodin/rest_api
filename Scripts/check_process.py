import psutil


sum_process = []

if 'python.exe' in (p.name() for p in psutil.process_iter()):
    pass
    # import os
    # os.chdir("C:\pogodinvv\Test_uspd")
    # os.startfile("start.bat")


for p in psutil.process_iter():

    if p.name() == 'python.exe':
        sum_process.append(p.name())


print(len(sum_process), sum_process)
if len(sum_process)<3:
    import os
    os.chdir("C:\pogodinvv\Test_uspd")
    os.startfile("start.bat")
    #p.terminate()

print('python.exe' in (p.name() for p in psutil.process_iter()))
