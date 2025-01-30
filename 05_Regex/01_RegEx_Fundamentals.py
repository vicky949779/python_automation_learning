####################################################################################################################
#  work and try this website "https://regex101.com/"
# ()          --> This means group
# \.          --> This will help to find '.' ex: you search cisco.com that time you can search 'cisco.' # '.' search '.' in easy  
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


with open('05_Regex/show_version.txt') as ver_data:
    ver_output =ver_data.read()
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

my_pattern =r'(gnu)\.(org)' 
re_output =re.search(my_pattern, ver_output) 

if re_output:
    print("Match Found...")
    print(re_output.group(0))
    print(re_output.group(1))
    print(re_output.group(2))
    # print(re_output.group(3))
else:
    print("***************MAtch not found**************")