# import password_gen # use 1st method in directly pyhton file name
# from password_gen import user_cmd_gen, users_cmd_gen # use 2nd method in directly mention inside the name of functions
import password_gen as pwd # use 3rd method in pyhton file name to change coustom name

# print(password_gen.user_cmd_gen('vicky',15)) # 1st method
# print(user_cmd_gen('vicky',15)) # 2nd method
print(pwd.user_cmd_gen('vicky',15)) # 3rd method