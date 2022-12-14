from asyncio import subprocess
from sys import stderr
from paramiko import SSHClient, AutoAddPolicy
import dotenv, os

def connect():
    dotenv.load_dotenv()
    SSH_USER = str(os.getenv("SSH_USER"))
    IP = str(os.getenv("IP_ADDRESS"))
    client = SSHClient()

    client.load_host_keys("ssh/known_hosts")
    client.load_system_host_keys()

    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(IP, username=SSH_USER)
    return client


def command(command):
    client = connect()
    stdin, stdout, stderr = client.exec_command(str(command))
    output = f'{stdout.read().decode("utf8")}'
    stdout.close()
    client.close()
    return output


if __name__ == '__main__':
    pass