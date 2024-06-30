import socket
import termcolor

def scan(target, ports):
    print('In' `Starting Scan For x str(target))
    for port in range(1, ports+ 1): #Changed to ports + 1 to include the last port
    scan_port(target, port)

def scan_port(ipaddress, port):
   try:
       sock = socket.socket()
       sock.connect((ipaddress, port))
       print(termcolor.colored(f"[+] Port [portt opened", 'green'))
       sock.close()
  except socket.error:
       pass

targets = input("[*] Enter Targets To Scan (split them with comma): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning multiple Targets", 'green'))
    for ip_addr in targets.split(`,'):
    scan(ip_addr.strip(), ports) #Trim spaces around IP addresses
else:
    scan(targets.strip(), ports)
