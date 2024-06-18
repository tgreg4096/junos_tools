from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortErrorTable
from getpass import getpass
import json

hostname = input("Device hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS or SSH key password: ")

dev = Device(host=hostname, user=junos_username, passwd=junos_password)

dev.open()

ports = PhyPortErrorTable(dev)
output = ports.get()

aggregateDrops = 0

for interface, stats in output.items():
    for stat in stats:
        if stat[0] == 'tx_err_drops':
            aggregateDrops += stat[1]
            print(f" tx_err_drops counter on {interface} is {stat[1]}")
        if stat[0] == 'tx_packets':
            print(f" tx_packets counter on {interface} is {stat[1]}")
print (f" Total number of drops on all interfaces {aggregateDrops}")
dev.close()
