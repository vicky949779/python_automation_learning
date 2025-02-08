import ipaddress # using for valid ip set

# ip = ipaddress.IPv4Address('169.254.0.1') # i set this is ipv4 network
# print(type(ip))
# print(ip.version) # check which version v4 or v6 ?
# print(ip.max_prefixlen)
# print(ip.reverse_pointer) # print like this : 1.0.168.192.in-addr.arpa
# exp = ip.exploded
# print(exp) # print normally string type
# print(ip.is_multicast) # check this multicast or not, ex: TRUE or FALSE
# print(ip.is_private) # check this private or not, ex: TRUE or FALSE
# print(ip.is_global) # check this global or not, ex: TRUE or FALSE
# print(ip.is_link_local) # check this link local ip or not, ex: TRUE or FALSE

######### now user give the ip address ########

try:
    ip = ipaddress.IPv4Address(input('Enter IP:'.ljust(10)))
except ValueError:
    print("Invalid IP")

# These are some of the basic operations of IP address module. 
