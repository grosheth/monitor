from asyncio import subprocess


# Faire une connection ssh sur le PI et lancer les commandes via ce shell

def connect():
    return


def getInfo():
    info = subprocess.run("kubectl describe pods")
    info = info.stdout
    return


if __name__ == '__main__':
    connect()