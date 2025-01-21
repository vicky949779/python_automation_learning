from paramiko import client
from getpass import getpass

hostname = '192.168.40.10'

username = input("Enter Username:")

if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"Enter password of the user {username}")

