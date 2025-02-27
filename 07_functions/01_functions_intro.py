import string
import random
import os

os.chdir('07_functions') # now i chnage my directory for create file store inside of 07_functions.

# password = random.choices(string.ascii_uppercase, k=8) # i randomly print 8 characters of strings. K=8 means number of charecter.""" output: ['H', 'W', 'A', 'P', 'G', 'W', 'Y', 'Z'] """
# password = "".join(random.choices(string.ascii_uppercase, k=8)) # output : "" WBHIHZPQ "", join to this ''.

# Add more valuse: captial, small and numbers
# password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)) # output : "" wmN7BmRN ""
# print(password)

# create a function 

# def user_cmd_gen(user,priv):# this parameter
#     password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

#     # print(f"username:{user} privillage:{priv} secret:{password}")# this will print directly terminal
#     return f"username:{user} privillage:{priv} secret:{password}\n" # this will return the valuse in "" with open() ""

# print(user_cmd_gen("vicky",15))
# with open('test.txt', 'w') as file:
#     file.write(user_cmd_gen("vicky",15)) # now use this print come to error, it is "" TypeError: write() argument must be str, not None "", beacuse don't use return .

##########################################################################
# with open('test.txt', 'w') as file:
#     file.write(user_cmd_gen("vicky",15))
#     file.write(user_cmd_gen("surya",15))
#     file.write(user_cmd_gen("mohan",15))
#     file.write(user_cmd_gen("prakash",15))
#     file.write(user_cmd_gen("shihab",15))
##########################################################################
''' notes:

     1) function is call another function it is called callback
     2) function is return another function it is called Higher order fuction '''

# print(user_cmd_gen("vicky",15))
##########################################################################

# print(user_cmd_gen("vicky",priv=15)) # position arguments
##########################################################################

# name = "vicky"
# privillage = 15
# print(user_cmd_gen(name,privillage))
##########################################################################

''' The * operator takes out the values from the list and passes them one by one as separate arguments.
    Without *  -->  # This passes the entire list as a single argument, causing an error
    Using ** with Dictionaries '''

# u_list =['user2',15]
# print(user_cmd_gen(*u_list))
# print(user_cmd_gen(*[u_list[0],u_list[1]]))
# print(user_cmd_gen(*['user3',15]))# pass with list in a arguments
##########################################################################

''' For dictionaries, we use ** (double asterisk) instead of *.
    1) *dict unpacks keys only.
    2) **dict unpacks key-value pairs. '''

# u_dict = {'user':'admin','priv':15}
# print(user_cmd_gen(**u_dict))
##########################################################################

''' How to send an arbitory number of positional arguments or keyword arguments 
'''
# def user_cmd_gen(user,priv, *args, **kwargs): # must you give *args because this takes 3 positional arguments, then i add dict mention **
#     password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

#     print(f"username:{user} privillage:{priv} secret:{password}\n")
#     print("Commands are..")
#     for cmd in args:
#         print(cmd)
#     for data in kwargs: 
#         print(f"{data} is : {kwargs[data]}") # # Now this "" kwargs[data] "" mention for keys you will call keys print the values.


lst2 = ['conf t','int lo1001','no shut','sh ip int br']
dict2 = {'location': 'banglore', 'team': 'vicky'}
# user_cmd_gen('admin',15,*lst2)

'''
# for data in dict2: # dict2 have key pair values, but data have only keys
#     print(f"{data} is : {dict2[data]}") # Now this "" dict2[data] "" mention for keys you will call keys print the values.
'''

##################################################################################################
''' pass Arbitory number of elements to function ,It has passed list of multiple dictionary '''

def user_cmd_gen(user,priv):
    password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

    conf_list = [f"username:{user} privillage:{priv} secret:{password}"]
    return conf_list


user_dict = [{'name': 'user1','priv':15},
             {'name': 'user2','priv':15},
             {'name': 'user3','priv':15}]
def users_cmd_gen(*args):
    cmd_list = []
    for user in args:
        password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

        user_cmd = f"username:{user['name']} privillage:{user['priv']} secret:{password}"
        cmd_list.append(user_cmd)
    return cmd_list

print(users_cmd_gen(*user_dict))
print(user_cmd_gen('vicky',15))
