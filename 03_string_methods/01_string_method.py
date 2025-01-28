# username = 'admin1'
# print(dir(username))

# print(username.capitalize()) # ---> use for first letter captial letter
# print(username.casefold()) # ---> get both letter captial or small
# print(username.center(20), "Hi") #---> yo

# user_input = input("Enter Username:").casefold().strip().replace(" ","") # strip is remove white space , replace is remove white space between words
# if user_input == username:
#     print(f"Input {user_input} matched")
# else:
#     print("Not matched")
########################################################################
# ip = '192.168.0.1'
# device = 'router'
# print(f"IP Address is: {ip}\nDevice type is: {device}")

########################################################
'''find'''
# print(username.index('2'))

##############################################################
'''is decimal'''
# a_number = '\u0035'
# print(a_number)
# print(a_number.isdigit())
# print(a_number.isdecimal())

# b_letter = 'A'
# print(b_letter.isascii())
##########################################################
'''is identifier  a-z, A-Z, 0-9, _ : should not start with number'''
# an_identifier = 'A123a_'
# print(an_identifier.isidentifier())
##########################################################
'''printable'''
# printable = 'Hey there'
# print(printable.isprintable())
##########################################################
'''join'''
# list1 = ['Cisco', "IOS", "17.3"]
# print('-'.join(list1))   #---> ex: Cisco-IOS-17.3
# print('.'.join(list1))   #---> ex: Cisco.IOS.17.3
##########################################################
'''ljust'''
# print("abc".ljust(18), '12345')  #--> ljust is 18 words space
# print("123456789012345678".ljust(18), '12345')  
# print("abcabc".ljust(18), '12345')
# print("abcrtui".ljust(18), '12345')

##########################################################
'''maketrans'''
# message = "Hey there.."
# trans = message.maketrans('e.', 'E!')
# print(message.translate(trans))

##########################################################
'''partition'''
# message = "ip route 192.168.0.0"
# print(message.partition(" route "))

##########################################################
'''split'''
users = 'user1, user2, user3'  
user_list = users.split(', ')  #--> this also will be returning the multiple users in the list.
# print(user_list)
# for user in user_list:
#     print(f"Username is: {user}")
##########################################################
'''splitlines'''
# print("user1\nuser2\nuser3".splitlines()) #----> This also will be returning the multiple users in the list.

##########################################################
'''translate'''
# trans = {46: 33} #---> Replacing in this way using even Unicode also you can translate.
# print("Hey there..".translate(trans)) #---> Here also we will try replacing .. to !!  

##########################################################

'''zfill'''
print('abc'.zfill(5)) # ---> This will add aditional two zeros, ex: 00abc


