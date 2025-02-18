# we'll see how to validate IP subnets using IP address module.

import ipaddress

ip_subnet = ipaddress.ip_network('192.168.0.0/24')

# print(ip_subnet) # this will tell what you write that all of see, like 192.168.0.0/24
# print(ip_subnet.network_address) # it will show only ip without subnet ex: 192.168.0.0
# print(ip_subnet.broadcast_address) # it will show broadcast address without subnet ex: 192.168.0.255
# print(ip_subnet.netmask) # it will show netmask without subnet ex: 255.255.255.0
# print(ip_subnet.num_addresses) # it will show particular subnet ex: 256
# print(ip_subnet.prefixlen) # it will show prefixlenth ex: 24
# print(ip_subnet.exploded) # it will print normal string ex: 192.168.0.0/24
# print(type(ip_subnet)) #<class 'ipaddress.IPv4Network'>
# print(ip_subnet.hostmask) #this is wildcard mask ex: 0.0.0.255
# print(ip_subnet.reverse_pointer) # this is dns reverse pointer ex: 0/24.0.168.192.in-addr.arpa
# print(ip_subnet.with_prefixlen) # print ip with prefixlen ex: 0/24.0.168.192.in-addr.arpa
# print(ip_subnet.version)
# print(ip_subnet.max_prefixlen) # tell what is max prefix length

# print(ip_subnet.overlaps(ipaddress.ip_network('192.168.0.5/32')))  # So we are getting to in this way we can validate a specific subnet as part of any other subnet.

# for ip in ip_subnet.hosts():
#     print(ip)   # this will give us an entire ip address  in this subnet

# ip_add1 = ipaddress.ip_address('192.168.0.1')
# print(ip_add1 in ip_subnet) # this will check both ip are parts. ex: in present print true not present false.

new_exclude = ipaddress.ip_network('192.168.0.5')
l1 = ip_subnet.address_exclude(new_exclude) # this will generate subnet list.
for ip in l1:
    print(ip)