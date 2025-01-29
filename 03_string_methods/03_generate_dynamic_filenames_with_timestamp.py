import datetime

with open('03_string_methods/show_commands.txt') as sh_cmd:
    commands =sh_cmd.readlines()

now =datetime.datetime.now().replace(microsecond=0)
now_12hr = now.strftime("%d-%m-%Y %I:%M:%S %p") # Date in YYYY-MM-DD format and %I is 12-hour, %M is minutes, %S is seconds, and %p is AM/PM

# Time and commands with sequence number
for cmd in enumerate(commands, start=1): #---> enumerate is each list items give seperate sequence or serial number like this : (1, 'show running-config\n')
     # this will check horizontal zero th index is sequence number and first index is commands.
    file_name = (f"{str(now_12hr).replace(' ',':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ','_').strip()}.txt") #---> '.zfill()'is sequence number is 1 to change 01 like that "2025-01-29:03:32:07:PM_01_show_running-config.txt"
    with open(file_name, 'w') as cmd_data:
        cmd_data.write('test_data')