#There is a library that needs to be inported and that statement is commented out, you must uncomment it
import socket
#import fcntl
import struct
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # uncomment the following line if using python2
    #return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24])
    # uncomment the following line if using python3
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',bytes(ifname[:15],'utf-8')))[20:24])    
address = get_ip_address('wlan0')
#change wlan0 to eth0 if you want the wired IP address
print(address)
