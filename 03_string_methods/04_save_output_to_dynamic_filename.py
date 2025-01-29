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

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "Admin_1234!"

with open('03_string_methods/show_commands.txt', 'r') as conf_file: 
    new_cmd =conf_file.readlines()

print(new_cmd)

os.chdir('03_string_methods/backup')
def cisco_cmd_exicuter(hostname, commands):
    try:
        print(f"connecting to the device {hostname}..... ")
        now = datetime.datetime.now().replace(microsecond=0)
        now_12hr = now.strftime("%d-%m-%Y %I:%M:%S %p")        
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname,
                           username=username,
                           password=password,
                           look_for_keys=False, allow_agent=False)

        print(f"connected to the device\t{hostname} ")

        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n") 
        # Commends name are set with dynamic name of file name and each command output with seperate file 
        for cmd in enumerate(commands, start=1):
            file_name = (f"{str(now_12hr).replace(' ',':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ','_').strip()}.txt")
            with open(file_name, 'w') as cmd_data:
                device_access.send(f"{cmd[1]}") # i add [1] because access 1st index only that is commend section
                time.sleep(2)
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

cisco_cmd_exicuter('sbx-nxos-mgmt.cisco.com', new_cmd)

