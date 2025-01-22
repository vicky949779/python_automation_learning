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

cmd_switch_01 = ['conf t','int lo1','ip add 1.1.1.1 255.255.255.255','no sh','end'] # i have seperate two cmd list
cmd_switch_02 = ['conf t','int lo1','ip add 1.1.1.2 255.255.255.255','no sh','end'] 

def cisco_cmd_exicuter(hostname, commands): #now using to function to pass parameter then all details are same so i write inside of fuction in this 
    print(f"connecting to the device {hostname}..... ") # initialy get ssh and print this.
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

cisco_cmd_exicuter('192.168.40.10',cmd_switch_01) # now i'm passing arguments of hostname and cmd list names. 
cisco_cmd_exicuter('192.168.40.20',cmd_switch_02) # must note this --> any variable mention you must not put '' and "" this because not triger in normally.