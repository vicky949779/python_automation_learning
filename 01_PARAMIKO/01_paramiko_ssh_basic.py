import time
from paramiko import client # type: ignore
from getpass import getpass

hostname = '192.168.40.10'

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"Enter password of the user {username}: ") or "123"

ssh_client = client.SSHClient() #it has to use for ssh_connection
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy()) #it is auto connecting and  without authentication to connect a device. one method is AutoAddPolicy
ssh_client.connect(hostname=hostname,
                   username=username,
                   password=password,
                   look_for_keys=False,allow_agent=False) #tell next class
print("connected successfully")
device_access = ssh_client.invoke_shell() #it will works to triger the commend to ssh
device_access.send("terminal len 0\n") #it will extend termianl to show more contend
device_access.send("show run\n")
time.sleep(5) #it is wait for 5 sec to show up all exicuted commends
output = device_access.recv(65535)  # store the output variable to output. recive the data in byte formate,Standard buffer size: 65535 bytes (or 64 KB) is commonly used as a buffer size when reading large chunks of data.
print(output.decode()) #.decode is allign use out put structured, human readable formate.

ssh_client.close() #after configuration you close ssh connection
