  GNU nano 7.2                                                                                                      task2.py                                                                                                               
import nmap
import requests

def scan_ports(target_host):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_host, arguments='-p 1-65535 -T4')

    open_ports = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    open_ports.append(port)
    
    return open_ports

def check_server_version(url):
    headers = requests.get(url).headers
    server_info = headers.get('Server')
    return server_info

def main():
    target_host = input("Enter target IP or hostname to scan: ")
    
    # Scan for open ports
    open_ports = scan_ports(target_host)
    if open_ports:
        print("Open Ports:")
        for port in open_ports:
            print(f"  Port {port} is open")
    else:
        print("No open ports found")
    
    # Check server version
    url = f"http://{target_host}"
    server_info = check_server_version(url)
    if server_info:
        print(f"Server Version: {server_info}")
    else:
        print("Server version information not available")
    
if __name__ == "__main__":
    main()


