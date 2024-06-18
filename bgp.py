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

xmlparser = jxmlease.Parser()
result = jxmlease.parse(rpc_xml)

for neighbor in result['bgp-information']['bgp-peer']:
    print(f"Checking peer with IP address {neighbor['peer-address']}")
    print(f" BGP accepted prefixes:\t {neighbor['bgp-rib']['accepted-prefix-count']}")
    print(f" BGP peer AS:\t\t {neighbor['peer-as']}")
    print(f" BGP peer state:\t {neighbor['peer-state']}")
    print(f" BGP session uptime:\t {neighbor['elapsed-time']}")
    print(f" BGP input messages:\t {neighbor['input-messages']}")
    print(f" BGP output messages:\t {neighbor['output-messages']}")
dev.close()
