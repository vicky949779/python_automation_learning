import time
from paramiko import client # type: ignore
from getpass import getpass

# hostname = '192.168.40.10'
# hostname = '192.168.40.20'

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "123" 

cmd_switch_01 = ['sh version12'] 
cmd_switch_02 = ['sh version']

def exec_cmd_exicuter(hostname, commands): 
    print(f"connecting to the device {hostname}..... ") 
    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy()) 
    ssh_client.connect(hostname=hostname,
                    username=username,
                    password=password,
                    look_for_keys=False, allow_agent=False)

    print(f"connected to the device\t{hostname} ")

    
    for cmd in commands:
        print(f"\n{'#'*10} Executing {cmd}{'#'*10}")  #this is every cmd run that cmd front and back side put # this 10 times with that commend line like this {  ########## Executing sh version1234##########  }
        stdin, stdout, stderr = ssh_client.exec_command(cmd) # exec_command is using to check input,output and error , note this it will work only with any show commands only.
        print(stdout.read().decode()) # i set read mode
        err = stderr.read().decode()
        if err:
            print(f"Error Occurred: {err}")

exec_cmd_exicuter('192.168.40.10',cmd_switch_01) 
exec_cmd_exicuter('192.168.40.20',cmd_switch_02)