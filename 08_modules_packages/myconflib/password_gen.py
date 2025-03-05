''' 1) What is python module 
    2) How to import functions from module
    3) What is pyhton packages
'''
import string
import random

def user_cmd_gen(user,priv):
    password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

    conf_list = [f"username:{user} privillage:{priv} secret:{password}"]
    return conf_list

def users_cmd_gen(*args):
    cmd_list = []
    for user in args:
        password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

        user_cmd = f"username:{user['name']} privillage:{user['priv']} secret:{password}"
        cmd_list.append(user_cmd)
    return cmd_list