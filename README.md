# Basic Junos tools

A few small op scripts to automate some basic tasks, using pyez for Junos.

## Getting Started

info.py - returns a list of device facts, device software version, RE states, and basic device information

bgp.py - returns a list of BGP peers, provides peer state, peer-AS number and the number of messages sent and received, along with the elapsed time of the session

default.py - provides the resolved next-hop interface for an OSPF default route, along with it's age.

drops.py - retreives the counter stats for tx_packets + tx_err_drops on all interfaces from a Juniper router

## Future

I'd like to add more functionality to bgp.py, to also display the number of advertised and received routes, and also allow to specify a specific peer - could be useful in edge peering scenarios where there are hundreds of peers. 

For drops.py, I'd like to possibly call a file full of devices - and run this against a large number of devices, essentially looking for egress drops - I would also possibly call some of the other statistics, which would aid in finding congestion, eg; discards or overruns. 

