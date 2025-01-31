import re

version_pattern = re.compile(r'NXOS.+ version (\S+)')
model_pattern = re.compile(r'cisco \S+ (\S+).Chassis')
serial_no_pattern = re.compile(r'Processor Board ID (\S+)')
up_time_pattern = re.compile(r'.+ uptime is (.+)')


with open('05_Regex/Show_version.txt') as file:
    output = file.read()
    version_match = version_pattern.search(output)
    # print(version_match)
    print('IOS Version'.ljust(18) + ':' + version_match.group(1))

    model_match = model_pattern.search(output)
    print('Model'.ljust(18) + ':' + model_match.group(1))

    serial_no_match = serial_no_pattern.search(output)
    print('Serial Number'.ljust(18) + ':' + serial_no_match.group(1))
    up_time_match = up_time_pattern.search(output)
    print('Device Uptime'.ljust(18)+ ':' + up_time_match.group(1))