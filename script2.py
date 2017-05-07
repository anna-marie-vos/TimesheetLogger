import psutil

for proc in psutil.process_iter():
    try:
        pinfo = proc
    except psutil.NoSuchProcess:
        pass
    else:
        print(pinfo)
