
import os # ---> it access to linux to support using python
# print(os.getcwd()) # ----> check current working directory.  Then use double dot(../) to back the current directory
# os.chdir('01_PARAMIKO')
# # print(os.getcwd())
# # print(len(os.listdir())) # -----> it will shown current directory of listing files.
# # print(f"Current working directory is : {os.getcwd()}")
# # print(os.system('ls -larth')) # ----> run with directly os command and this shown list of that directory.


###########    Open method   ################################################################################################
# files = os.listdir()  # -----> this will show list of files into the current directory to print one by one.
# files.sort()
# for file in files:
#     #print(file)
#     with open(file) as file_data: #----> 'with open' method is using for files open method.
#         # print(type(file_data))
#         # print(dir(file_data)) # ---> show with supported all methods 
#         if "paramiko" in file.casefold():
#             print(print(f"{f'#'*10} {file} {'#'*10}")) # --->each matching file nmae with ### are prining
#             print(file_data.read()) # read the all data


##############################################################################################################################  
## ----------------------------------Read Method ---------------------------------------------------------------------------##


file1 = open('02_file_operations/config_file.txt', 'r') #----> This is a file path and mention read mode
#print(file1.read())
#print(dir(file1))
# print(file1.readline()) # ---> read 1st line you can continuesly use this read line by line.
# print(file1.readlines()) # -----> Entire lines are print, and same list are show the output.

#####################Now this print that files original formates like to print here.
# commands = file1.readlines()
# for command in commands:
#     print(command.rstrip('\n')) #-----> use string method of .rstrip('\n') it is remove the new empty line .
# file1.close() #--->This method must have want to after file open to close that. 

#############################################################################################################################
##################  with open ###############################################################################################

# with open('02_file_operations/config_file.txt') as file1:
#     commands = file1.readlines()
# for command in commands:
#     print(command.rstrip('\n'))

################################### write method ######################################################################
# with open('02_file_operations/config_file_02.txt', 'a') as file2: # ----> Now this write mode.
#     file2.write("Add append\nmethod to trying\n") #---> You can write you text.

#############################################################################################################################

# with open('02_file_operations/sample.pdf', 'rb') as source_file :  #---> using read method this 
#     s = source_file.read()
# with open('02_file_operations/sample_02.pdf', 'wb') as dest_file : # ----> using copy method pdf to another pdf using write method.
#     dest_file.write(s)

######################### Remove method ##########################################################################################

os.remove('02_file_operations/sample_02.pdf')


#############################################################################################################################