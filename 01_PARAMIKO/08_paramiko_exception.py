import sys
import time
import traceback
from paramiko import client, ssh_exception # type: ignore
from getpass import getpass
import socket

# hostname = '192.168.40.10'
# hostname = '192.168.40.20'

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "123" 

cmd_switch_01 = ['conf t','int lo1','ip add 1.1.1.1 255.255.255.255','no sh','end'] 
cmd_switch_02 = ['conf t','int lo1','ip add 1.1.1.2 255.255.255.255','no sh','end'] 

def cisco_cmd_exicuter(hostname, commands): 
    try:  # all are under the try . it will use for devides errors and show seperate so this method use.
        print(f"connecting to the device {hostname}..... ") 
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname,
                        username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

        print(f"connected to the device\t{hostname} ")

        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")

        for cmd in commands: 
            device_access.send(f"{cmd}\n") 
            time.sleep(1)
            output = device_access.recv(65535)
            print(output.decode(), end='' ) 

        device_access.send("sh run int lo1\n")
        time.sleep(2)
        output = device_access.recv(65535)
        print(output.decode())
        ssh_client.close()
    except ssh_exception.AuthenticationException: # import ssh_exception then username and password is wrong time tell this.
        print("\U00002757\U00002757\U00002757Authentication failed, Check your credentials \U00002757\U00002757\U00002757")
    except socket.gaierror: #it is used for hostname error time using.
        print("\U00002757\U00002757\U00002757Check the hostname \U00002757\U00002757\U00002757")
    except ssh_exception.NoValidConnectionsError: # it is you enter wrong ip that time come error show
        print("\U00002757\U00002757\U00002757SSH Port not reachable\U00002757\U00002757\U00002757")
    except:
        print("\U00002757\U00002757\U00002757Exception Occured \U00002757\U00002757\U00002757")
        print(sys.exc_info()) # it will show exception error found to tell.
        #traceback.print_exception(*sys.exc_info()) # this line will show what error in each devices to seperate.

cisco_cmd_exicuter('192.168.40.30',cmd_switch_01) # i change hostname with error
cisco_cmd_exicuter('192.168.40.20',cmd_switch_02) 