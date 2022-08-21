from asyncio import subprocess


# Faire une connection ssh sur le PI et lancer les commandes via ce shell

def connect():
    return

def getIP():
    return

def ping():
    ip = getIP()
    subprocess.run(f"ping {ip}")
    return

def getInfo():
    info = subprocess.run("sudo kubectl describe pods")
    info = info.stdout
    return


if __name__ == '__main__':
    connect()