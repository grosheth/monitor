from asyncio import subprocess
from paramiko import SSHClient, AutoAddPolicy
import dotenv, os

# Faire une connection ssh sur le PI et lancer les commandes via ce shell

dotenv.load_dotenv()

client = SSHClient()

client.load_host_keys("ssh/known_hosts")
client.load_system_host_keys()

client.set_missing_host_key_policy(AutoAddPolicy())


client.connect(os.getenv("IP_ADDRESS"), username=os.getenv("SSH_USER"))
def connect():
    return


def getInfo():
    info = subprocess.run("kubectl describe pods")
    info = info.stdout
    return


if __name__ == '__main__':
    connect()