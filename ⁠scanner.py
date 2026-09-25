Here is the enhanced version of your code. You can copy and paste it directly into your Python file:

import socket
# Get user inputtarget = input("Enter target IP or domain: ")ports = [21, 22, 80, 443, 8080]
try:
    # 1. Resolve domain to IP once to ensure it's valid and prevent crashes
    target_ip = socket.gethostbyname(target)
    print(f"\nScanning target: {target} ({target_ip})...\n")

    for port in ports:
        # 2. Using 'with' automatically and safely closes the socket after use
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")
except socket.gaierror:
    # Catches invalid domains (e.g., typos like "gogle.cmom")
    print("\n[-] Error: Could not resolve hostname. Please check the spelling or your internet connection.")except socket.error:
    # Catches general network connection failures
    print("\n[-] Error: Could not connect to the network.")


