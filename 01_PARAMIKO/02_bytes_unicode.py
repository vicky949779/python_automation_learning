# b1 = b"\n\n hy\tman"   #add "b" is mention for bytecode
# print(b1)
# print(type(b1))
# print(b1.decode()) # this will decode the word

# c1 = """


# hey man
# """
# print(c1.encode())


# b1 = b"\xF0\x9F\x98\x8D"
# print(b1.decode())

#-------------------------------------------------------------------
######## unicode formate #######------------start-------------------  
# ------------------------------------------------------------------

# u1 ="\U0001F603"
# print(u1)


#------------------------------------END----------------------------


# ------------------------------------------------------------------------
# Try to script with password section to set key emoji
# ------------------------------------------------------------------------

import time
from paramiko import client # type: ignore
from getpass import getpass

hostname = '192.168.40.10'

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"\U0001F511 Enter password of the user {username}: ") or "123"  # i mentioned this line of unicode is that U0001F511

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostname,
                   username=username,
                   password=password,
                   look_for_keys=False, allow_agent=False)

print("connected successfully")

device_access = ssh_client.invoke_shell()
device_access.send("terminal len 0\n")
device_access.send("show run\n")
time.sleep(5)
output = device_access.recv(65535)
print(output.decode())

ssh_client.close()
