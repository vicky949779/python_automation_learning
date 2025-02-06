# Open file in read mode, Then those are add to dictionary then write list inside the dictionary after that print.

import sys
import time
from paramiko import client, ssh_exception  # type: ignore
from getpass import getpass
import socket
import datetime
import os
from pprint import pprint


username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "Admin_1234!"

new_cmd = ["show ip interface brief"]

os.chdir('05_Regex/backup_files')
def cisco_cmd_exicuter(hostname, commands):
    try:
        print(f"connecting to the device {hostname}..... ")
        now = datetime.datetime.now().replace(microsecond=0)
        now_12hr = now.strftime("%d-%m-%Y %I:%M:%S %p")   
        current_conf_file = f"{now_12hr}_{hostname}.txt"  
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
                device_access.send(f"{cmd}\n") #---> i add \n . because that is Enter, im using list in cmd.
                time.sleep(2)
                output = device_access.recv(65535).decode() #--> i put the decode here because first read for output in parsing purpose.
                cmd_data.write(output) 
                print(output)

        ssh_client.close()

        print('######## Parse Formate ############')  
        output_list = output.splitlines()
        interface_list = output_list[38:-3]
        int_parse_list = list()
        # print(interface_list)
        for interface in interface_list:
            intf_dict = {}
            intf = interface.split()
            intf_dict['Int_name'] = intf[0]
            intf_dict['IP '] = intf[1]
            intf_dict['Status'] = intf[2]
            int_parse_list.append(intf_dict)
        pprint(int_parse_list)
            
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

