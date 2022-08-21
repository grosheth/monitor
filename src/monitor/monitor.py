from asyncio import subprocess

def getIP():
    return

def ping():
    ip = getIP()
    subprocess.run(f"ping {ip}")
    return

def getInfo():
    info = subprocess.run("sudo kubectl describe pods")
    return
