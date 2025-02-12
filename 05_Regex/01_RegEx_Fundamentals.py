####################################################################################################################
#  work and try this website "https://regex101.com/"
# |           --> This mean 'or'
# ()          --> This means group
# \.          --> This will help to find '.' ex: you search cisco.com that time you can search 'cisco.' # '.' search '.' in easy
# \S          --> (Uppercase S) → Matches Non-Whitespace Characters
# \s          --> (Lowercase s) → Matches Whitespace Characters
# \n          --> Matches a newline character (line break).
# \B          --> Match with center character. ex: aaaaciscobbbbb   ---> match with 'cisco'  
# \b          --> Matches the empty string, but only at the beginning or end of a word.print once only
# \Z          --> Only match at the end of the string, print once only
# \A          --> Only match at the start of the string, print once only
# \w          --> Any word character will match ex: [ a-zA-Z0-9_ ] 
# {m,n}       --> a{3,5} will match from 3 to 5 'a' , how many times that single character repeat you mention 3 or 5 times more that will match.  
# [\w\.-]+    --> Matches one or more word characters, dots, or hyphens, forming longer strings.
# [Cc]isco    --> [] this will match 2types of C but its output is cisco or Cisco.
# [Cc].sco    --> . dot   is match for any character if you give 'a' that will accept ex: casco
# [Cc]i*sco   --> * It means 0 or more repetitions in 'i' letter it will suppord ex: ciiiiiiiiiiiiiiiiisco
# [Cc]i+sco   --> + That means 1 or more repetitions ex: ciiiiiiiiiiiiiiiiisco
# [Cc]i?sco   --> ? It will match 0 or 1 repetitions 
# ^[Cc]i?sco  --> ^ Sentence 1st Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
# [Cc]i?sco$  --> $ It means end match with string.

# ### Greedy and non-Greedy RegEx ###

# Cis.+o      --> .+ It's means greedy behaviour , it will start cis at the end of 'o' stoped.
# Cis.+       --> It will start Cis end is that word full sentece when stop that time stop.
# Cis.+?o     --> Match with exact word . 
# Cis\S.+?o   --> \S Match with white space ex: "Cis co"
# Ci\S.+?o    --> \S Match with one missing word to any letter ex: "Cit co"
# 
# ####################################################################################################################

# st = r'\nhello\tthere' #--> 'r' is row string 
# print(st) 
# print(type(st))
####################################################################################################################
import re


# with open('05_Regex/show_version.txt') as ver_data:
#     ver_output =ver_data.read()
# my_pattern =r'Cisco'
# # re_output =re.search(my_pattern, ver_output) # output is <re.Match object; span=(20, 25), match='Cisco'>  how many matches are tell in between
# re_output =re.search(my_pattern, ver_output) 
# print(re_output.group(0)) # i choose the group
######################################################################################################################

# my_pattern =r'cisco(.+) C\d\S.+'  # --> i match with this  'cisco Nexus9000 C9300v Chassis' major role in this '()'
# re_output =re.search(my_pattern, ver_output) 
# version_output = re_output.group(1)  # group 1 is  'Nexus9000' group 0 means full line like 'cisco Nexus9000 C9300v Chassis' 
# print(f"{'IOS version:'.ljust(18)}:{version_output}") # IOS version:      :  Nexus9000
#######################################################################################################################

# my_pattern =r'(gnu)\.(org)' 
# re_output =re.search(my_pattern, ver_output) 


# if re_output:
#     print("Match Found...")
#     print(re_output.group(0))
#     print(re_output.group(1))
#     print(re_output.group(2))
#     # print(re_output.group(3))
# else:
#     print("***************MAtch not found**************")
#######################################################################################################################
'''compile'''

# my_pattern = re.compile(r'(gnu)\.(\w+)')
# result = (re.search(my_pattern, ver_output))
# print(result)
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
#######################################################################################################################

""" compile exmaple """

# my_pattern = re.compile(r'C....')
# print(re.search(my_pattern, ver_output)) #--> It will show only first iteration only
# print(re.findall(my_pattern, ver_output))  #--> It will show all possible of matches
# results = re.finditer(my_pattern, ver_output)  #--> It will show iterator ex: <callable_iterator object at 0x770c4e637c10>
# for result in results:
#     #print(result) #---> It will print all matches and span details
#     print(result.group()) ##-->{
#     print(result.span()) ##-->{  It will show span with group all detials
#######################################################################################################################

""" Validate User input """

# input1 = input("Enter the python version:\t")
# my_pattern = re.compile(r"python3(\.10)?$|")
# match = my_pattern.search(input1)

# if match:
#     print(f"Matched with :{input1}")
# else:
#     print("Not matched")
#######################################################################################################################
""" Email validation pattern """

# support_mail = 'please reach out to help@gmail.com, support@gmail.com, admin@gmail.co.iab@abc.co.us,abc@aa.co.uk'
# email_pattern = re.compile(r'[\w\.-]{3,16}@[\w\.-]+.co[m|.](\w{2})?')
# results = email_pattern.finditer(support_mail)
# for result in results:
#     print(result.group())
 
# #### output #######
#####################
"""     help@gmail.com
        support@gmail.com
        admin@gmail.co.ia
        abc@aa.co.uk         """
#######################################################################################################################

# str1 = """DC01 IND R1"""

str1 = """DC01 IND R1
DC01 US R1
DC01 UK R1
"""
# print(re.search(pattern=r'^D.+1$', string=str1))
# print(re.findall(pattern=r'^D.+1$', string=str1))

# r = re.finditer(pattern=r'^D.+1$', string=str1) 
# for data in r:
#     print(data.group())
#######################################################################################################################
""" Multiline """ # It can access for multiline strings

# print(re.search(pattern=r'\AD.+1$', string=str1, flags=re.MULTILINE))
# print(re.findall(pattern=r'\AD.+1$', string=str1, flags=re.MULTILINE))

# r = re.finditer(pattern=r'\AD.+1$', string=str1, flags=re.MULTILINE) 
# for data in r:
#     print(data.group())

''' 
^ \Z matches only with single line

^ : (Caret.) Matches the start of the string, 
and in MULTILINE mode also matches immediately after each newline.

\Z : Matches the end of the string or just before the newline at the end of the string,
 and in MULTILINE mode also matches before a newline.

\A : Matches only at the start of the string.

\Z : Matches only at the end of the string.

\A and \Z scans entire multiline and prints last result'''
###############################################################
# str1 = """DC01 IND R1"""

str1 = """DC01 IND R1
DC02 US R1
DC03 UK R1"""

# print(re.search(pattern=r"^D.+1\Z", string=str1))
# print(re.findall(pattern=r"^D.+1\Z", string=str1))
# r = re.finditer(pattern=r"^D.+1\Z", string=str1)
# for data in r:
#     print(data.group())
####################################
# print(re.search(pattern=r"^D.+1\Z", string=str1, flags=re.MULTILINE))
# print(re.findall(pattern=r"^D.+1\Z", string=str1, flags=re.MULTILINE))
# r = re.finditer(pattern=r"^D.+1\Z", string=str1, flags=re.MULTILINE)
# for data in r:
#     print(data.group())
############################################
'''
\b :Matches the empty string,
 but only at the beginning or end of a word. 

 \B
Matches the empty string, 
but only when it is not at the beginning or end of a word. 
 '''
# matches empty string only at beginning or end
# my_pattern = re.compile(r'\Bcisco')
# string1 = 'fgciscoroutercisco'
# print(my_pattern.search(string1))
############################################
'''{m,n}'''
# my_pattern = re.compile(r'cisco{2,5}')
# string1 = 'ciscorouterciscoo'
# print(my_pattern.search(string1))
############################################
''' \''''
# noinspection PyRedeclaration
# my_pattern = re.compile(r'\*\n')
# print(my_pattern.search(ver_output))
############################################

'''IGNORECASE'''
# print(re.search('hello', 'Hello', re.I))  #--> 're.I' is ingnore case for 'H' and 'h'
############################################
'''DOTALL
by default, dot matches any character except the newline'''

# print(re.search('hello.hello', 'Hello\nHello', flags= re.DOTALL | re.IGNORECASE))
# print(re.search('hello.hello', 'Hello\nHello'))

############################################
'''match'''
my_string = 'abcd1234abcd'
# print(re.match('abcd', my_string)) # None   #--> '.match' the begining of the string only match. 
# print(re.search('1234abcd', my_string)) # match:
# print(re.fullmatch('abcd1234abcd', my_string)) # match   #---> It will full file or string are only match. 

#################################################################################################################
""" match with 2 file """

# with open('05_Regex/show_version.txt') as sh_version:
#     a = sh_version.read().strip()
# with open('05_Regex/test.txt') as sh_test:
#     b = sh_test.read().strip()
# # Escape special regex characters in the pattern
# escaped_pattern = re.escape(a)

# # Perform full match
# match_result = re.fullmatch(pattern=escaped_pattern, string=b, flags=re.MULTILINE)

# # Print the result
# print("Match Found!" if match_result else "No Match!")
############################################
'''sub'''
# noinspection PyRedeclaration
my_string = 'VLAN100 ip address 1.1.1.1 VLAN200, VLAN300'
# print(re.sub(r'V', r'Vx', my_string)) #--> '.sub()' is convertion process, ex: v change vx
# print(re.subn(r'V', r'Vx', my_string))  #--> '.subn' is conversion process with tuple tell the how many conversion here.