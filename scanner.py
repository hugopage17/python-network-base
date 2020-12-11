from pythonping import ping
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup
mac = MacLookup()

class Scanner():
    def __init__(self):
        pass

    def get_range(self, range):
        lastIp = int(range.split('-')[1])
        network = range.split('-')[0]
        firstIp = int(network.split('.')[3])
        network = network.replace(str(firstIp), "")
        nodes = []
        while firstIp <= lastIp:
            nodes.append(network+str(firstIp))
            firstIp+=1
        return nodes

    def poll(self, node):
        status = str()
        response_list = ping(node, timeout=2, count=1)
        time = response_list.rtt_avg_ms
        if time == 2000:
            status = 'offline'
        else:
            status = 'online'
        return [node, status, time]

    def run_scan(self, nodes):
        range = self.get_range(nodes)
        return_data = []
        for ip in range:
            poll = self.poll(ip)
            return_data.append(poll)
        return return_data

    def mac_scan(self, ip):
        ip_mac = get_mac_address(ip=ip)
        vendor = str()
        if ip_mac != None:
            vendor = mac.lookup(ip_mac)
        return{
            "mac":ip_mac,
            "vendor":vendor
        }
