from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass

hostname = input("Device hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS or SSH key password: ")

dev = Device(host=hostname, user=junos_username, passwd=junos_password)

dev.open()

tbl = RouteTable(dev)
tbl.get()

print ('Resolved egress interface for default')

gw = RouteTable(dev)
gw.get('0.0.0.0')
print (gw)
for item in gw:
    print ('protocol:', item.protocol)
    print ('age:', item.age)
    print ('via:', item.via)

dev.close()