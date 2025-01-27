import sys
import time
from paramiko import client, ssh_exception  # type: ignore
from getpass import getpass
import socket
import datetime
import os

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "123"

# cmd_switch_01 = ['sh run']
# cmd_switch_02 = ['sh run']

with open('02_file_operations/config_file.txt', 'r') as conf_file: # ---> I read this to seperate file into commends after that commends run here.
    new_cmd =conf_file.readlines()

print(new_cmd)

os.chdir('02_file_operations/backup_files')
def cisco_cmd_exicuter(hostname, commands):
    try:
        print(f"connecting to the device {hostname}..... ")
        now = datetime.datetime.now().replace(microsecond=0)  
        current_conf_file = f"{now}_{hostname}.txt"  
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname,
                           username=username,
                           password=password,
                           look_for_keys=False, allow_agent=False)

        print(f"connected to the device\t{hostname} ")

        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")
        with open(current_conf_file, 'w') as cmd_data: 
            for cmd in commands:
                device_access.send(f"{cmd}") #---> i reamove \n . beacouse using seperate config file read.
                time.sleep(1)
                output = device_access.recv(65535)
                cmd_data.write(output.decode()) 
                print(output.decode(), end='')

        ssh_client.close()

    except ssh_exception.AuthenticationException:
        print("\U00002757\U00002757\U00002757Authentication failed, Check your credentials \U00002757\U00002757\U00002757")
    except socket.gaierror:
        print("\U00002757\U00002757\U00002757Check the hostname \U00002757\U00002757\U00002757")
    except ssh_exception.NoValidConnectionsError:
        print("\U00002757\U00002757\U00002757SSH Port not reachable\U00002757\U00002757\U00002757")
    except:
        print("\U00002757\U00002757\U00002757Exception Occured \U00002757\U00002757\U00002757")
        print(sys.exc_info())

cisco_cmd_exicuter('192.168.40.10', new_cmd)
cisco_cmd_exicuter('192.168.40.20', new_cmd)
