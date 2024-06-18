import sys
import json
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

hostname = input("Device hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS or SSH key password: ")

dev = Device(host=hostname, user=junos_username, passwd=junos_password)
try:

        dev.open()

except ConnectError as err:
        print (f"Cannot connect to device: {err}")
        sys.exit(1)
except Exception as err:
        print (err)
        sys.exit(1)
print (json.dumps(dict(dev.facts), indent=2, default=str))

dev.close()
