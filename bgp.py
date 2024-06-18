from jnpr.junos import Device
from lxml import etree
from getpass import getpass
import jxmlease

hostname = input("Device hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS or SSH key password: ")

dev = Device(host=hostname, user=junos_username, passwd=junos_password)

dev.open()

rpc = dev.rpc.get_bgp_summary_information()
rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
dev.close()


xmlparser = jxmlease.Parser()
result = jxmlease.parse(rpc_xml)


for neighbor in result['bgp-information']['bgp-peer']:
    print('Checking peer with IP address: ' + neighbor['peer-address'])
    print(neighbor['peer-as'])
    print(neighbor['peer-state'])
    print(neighbor['elapsed-time'])
    print(neighbor['input-messages'])
    print(neighbor['output-messages'])