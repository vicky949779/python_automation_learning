# show_output = """GigabitEthernet0/0     unassigned      YES unset  up                    up
# GigabitEthernet0/1     unassigned      YES unset  down                  down
# GigabitEthernet0/2     unassigned      YES unset  down                  down
# GigabitEthernet0/3     unassigned      YES unset  down                  down
# GigabitEthernet1/0     unassigned      YES unset  down                  down
# GigabitEthernet1/1     unassigned      YES unset  down                  down
# GigabitEthernet1/2     unassigned      YES unset  down                  down
# GigabitEthernet1/3     unassigned      YES unset  down                  down
# GigabitEthernet2/0     unassigned      YES unset  down                  down
# GigabitEthernet2/1     unassigned      YES unset  down                  down
# GigabitEthernet2/2     unassigned      YES unset  down                  down
# GigabitEthernet2/3     unassigned      YES unset  down                  down
# Vlan1                  192.168.40.10   YES manual up                    up
# """

# intf_lines = show_output.splitlines() #--> The .splitlines() method in Python splits a string into a list of lines, breaking at line boundaries (\n, \r\n, etc.), and removes the line breaks.
# for intf in intf_lines:
#     intf_details = intf.split() #---> .split() divides a string into smaller parts (called tokens) based on a delimiter (by default, spaces) and returns those parts as a list. ex: ['GigabitEthernet2/3', 'unassigned', 'YES', 'unset', 'down', 'down']
#     if intf_details[1] == 'unassigned':  # I want output is only print ip address section.
#         continue
#     print(f"Interface Name : {intf_details[0]} IP-Address : {intf_details[1]}")

# ###################################################################################################################################
# with open('03_string_methods/config_file.txt') as text:
#     lines = text.readlines()
#     print('Press Enter...', end='')
#     for line in lines:
#         if input() == '' :
#             line = line.strip(('\n'))  #---> .strip() removes any extra spaces (or specified characters) from the beginning and end of a string, but it doesn’t touch the middle part.
#             print(line, end='')
#     print( "completed")