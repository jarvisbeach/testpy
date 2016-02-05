import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 2

ip_addr = [ '50.76.53.27', '50.76.53.27']

username = 'pyclass'
password = '88newclass'

class SwitchConnect(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr.rstrip()
        self.username = username.rstrip()
        self.password = password.rstrip()
        self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    
    def login(self):
        self.remote_conn.read_until('sername', TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        time.sleep(1)
        self.remote_conn.read_until('assword', TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        return self.remote_conn.read_very_eager()

    def send_command(self, command):
        self.remote_conn.write(command + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()
    
switches = {}

for ip in ip_addr:
    switches[ip] = SwitchConnect(ip, username, password)

for switch in switches:
    print switches[switch].login()
    print switches[switch].send_command('term len 0')
    print switches[switch].send_command('show ip inter bri')
    print switches[switch].send_command('show run')
    switches[switch].remote_conn.close()
    
raw_input('Press enter to exit')
