import time
from paramiko import client # type: ignore
from getpass import getpass

hostname = '192.168.40.10'

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "123" 

commands = ['conf t','int lo1','ip add 1.1.1.1 255.255.255.255','no sh','end'] # now add this for using multi commands line in a single task.

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostname,
                   username=username,
                   password=password,
                   look_for_keys=False, allow_agent=False)

print("connected successfully")

device_access = ssh_client.invoke_shell()
device_access.send("terminal len 0\n")
for cmd in commands: # using for loop is line by line access commands variable to exicute cmd one by one. that variable is list method.
    device_access.send(f"{cmd}\n") # you must put the \n for end. because it has a proper way to triger cmd one by one.
    time.sleep(1)
    output = device_access.recv(65535)
    print(output.decode(), end='' ) # end='' it will work on not triger new line to showing. triger same line examplelike this {switch_01(config)#int lo1}

device_access.send("sh run int lo1\n")
time.sleep(2)
output = device_access.recv(65535)
print(output.decode())
ssh_client.close()