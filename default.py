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

default = RouteTable(dev)
default.get('0.0.0.0')
print (f" {default}")
for item in default:
    print (f" IGP protocol:\t\t\t {item.protocol}")
    print (f" Route age:\t\t\t {item.age}")
    print (f" Selected best-path interface:\t {item.via}")

dev.close()
