from scapy.all import ARP, Ether, srp

def arp_scan(ip_range):
    #first is to create ARP request so that we can move forward
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    
    # send and recieve the ARP requests 
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # and then extract device information from responses
    devices_list = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_info)
        
        return devices_list
    


#now define the IP range for ARP scanning
target_ip_range = "192.168.1.0/24" 

# at last perform ARP scan to discover devices
devices = arp_scan(target_ip_range)
print("Devices on the network:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")
