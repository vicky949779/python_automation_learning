from myconflib import cisco_cmd_executor, users_cmd_gen, user_cmd_gen # This will add specific
# from myconflib import * # This will add all files inside the myconflib

user_cmd = user_cmd_gen('test_admin1', 15)
print(user_cmd)
