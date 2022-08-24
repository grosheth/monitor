from asyncio import subprocess
from paramiko import SSHClient, AutoAddPolicy
import dotenv, os

def connect():

    dotenv.load_dotenv("monitor/.env")
    # SSH_USER = os.getenv("SSH_USER")
    # IP = os.getenv("IP_ADDRESS")
    client = SSHClient()

    client.load_host_keys("ssh/known_hosts")
    client.load_system_host_keys()

    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect("192.168.10.120", username="root")
    return client


def command(command):
    client = connect()
    stdout= client.exec_command(command)
    print(stdout)
    output = f'{stdout.read().decode("utf8")}'
    stdout.close
    client.close
    return output


if __name__ == '__main__':
    pass