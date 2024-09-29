import socket
import threading
import time

RED = "\033[91m"
RESET = "\033[0m"

ASCII_ART = f"""{RED}
  ██████     ██▓███      ▒█████      ██▀███     ▄▄▄█████▓     ██████      █████▒    ▒█████      ▒█████  
▒██    ▒    ▓██░  ██▒   ▒██▒  ██▒   ▓██ ▒ ██▒   ▓  ██▒ ▓▒   ▒██    ▒    ▓██   ▒    ▒██▒  ██▒   ▒██▒  ██▒
░ ▓██▄      ▓██░ ██▓▒   ▒██░  ██▒   ▓██ ░▄█ ▒   ▒ ▓██░ ▒░   ░ ▓██▄      ▒████ ░    ▒██░  ██▒   ▒██░  ██▒
  ▒   ██▒   ▒██▄█▓▒ ▒   ▒██   ██░   ▒██▀▀█▄     ░ ▓██▓ ░      ▒   ██▒   ░▓█▒  ░    ▒██   ██░   ▒██   ██░
▒██████▒▒   ▒██▒ ░  ░   ░ ████▓▒░   ░██▓ ▒██▒     ▒██▒ ░    ▒██████▒▒   ░▒█░       ░ ████▓▒░   ░ ████▓▒░
▒ ▒▓▒ ▒ ░   ▒▓▒░ ░  ░   ░ ▒░▒░▒░    ░ ▒▓ ░▒▓░     ▒ ░░      ▒ ▒▓▒ ▒ ░    ▒ ░       ░ ▒░▒░▒░    ░ ▒░▒░▒░ 
░ ░▒  ░ ░   ░▒ ░          ░ ▒ ▒░      ░▒ ░ ▒░       ░       ░ ░▒  ░ ░    ░           ░ ▒ ▒░      ░ ▒ ▒░ 
░  ░  ░     ░░          ░ ░ ░ ▒       ░░   ░      ░         ░  ░  ░      ░ ░       ░ ░ ░ ▒     ░ ░ ░ ▒  
      ░                     ░ ░        ░                          ░                    ░ ░         ░ ░  

      BY: !abdu11ah

{RESET}                                                                                                        
"""

PORTS = {
    80: b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\nContent-Length: 50\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Fake HTTP Server</h1></body></html>",
    22: b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n",
    25: b"220 fake-smtp.example.com ESMTP Postfix (Ubuntu)\r\n",
    443: b"HTTP/1.1 200 OK\r\nServer: nginx/1.18.0 (Ubuntu)\r\nContent-Length: 50\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Fake HTTPS Server</h1></body></html>"
}

BANNERS = {
    'HTTP': PORTS[80],
    'SSH': PORTS[22],
    'SMTP': PORTS[25],
    'HTTPS': PORTS[443]
}

def start_spoofing(port, banner, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        s.settimeout(timeout)
        print(f"[*] Listening on port {port}...")

        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    print(f"[+] Connection from {addr[0]}:{addr[1]} on port {port}")
                    try:
                        conn.sendall(banner)
                    except ConnectionResetError:
                        print(f"[!] Connection reset by peer on port {port}")
                    except BrokenPipeError:
                        print(f"[!] Broken pipe on port {port}")
            except socket.timeout:
                print(f"[!] Session timed out on port {port}.")
                break

def display_menu():
    print("\n[=================================================]")
    print("\n[C H O O S E  A N Y  O F  T H E  F O L L O W I N G]")
    print("")
    print("[1] Spoof HTTP (80)")
    print("[2] Spoof SSH (22)")
    print("[3] Spoof SMTP (25)")
    print("[4] Spoof HTTPS (443)")
    print("[5] Spoof All")
    print("[6] Spoof Custom Port")
    print("[7] Exit")
    print("\n[=================================================]")
    return input("\n[+] Select option(s) (e.g. 1,2): ").split(',')

def get_ports_from_choices(choices):
    selected_ports = []
    for choice in choices:
        if choice.strip() == '1':
            selected_ports.append(80)
        elif choice.strip() == '2':
            selected_ports.append(22)
        elif choice.strip() == '3':
            selected_ports.append(25)
        elif choice.strip() == '4':
            selected_ports.append(443)
        elif choice.strip() == '5':
            return [80, 22, 25, 443]
        elif choice.strip() == '6':
            port = int(input("[+] Enter the port number: "))
            service = input("[+] Enter the service (HTTP, SSH, SMTP, HTTPS): ").strip().upper()
            if service in BANNERS:
                selected_ports.append((port, BANNERS[service]))
            else:
                print("[!] Invalid service selected.")
                continue
    return selected_ports

def main():
    timeout_duration = 15

    print(ASCII_ART)
    print("[*] Checking System Requirements...")
    time.sleep(4)
    print("[*] Initializing things...")
    time.sleep(3)
    print("[*] Starting Sportsfoo...")
    time.sleep(5)

    while True:
        choices = display_menu()

        if '7' in choices:
            print("[*] Exiting...")
            break

        selected_ports = get_ports_from_choices(choices)
        if not selected_ports:
            print("[!] Invalid selection, try again.")
            continue

        threads = []
        for item in selected_ports:
            if isinstance(item, tuple):
                port, banner = item
                t = threading.Thread(target=start_spoofing, args=(port, banner, timeout_duration))
            else:
                port = item
                banner = PORTS[port]
                t = threading.Thread(target=start_spoofing, args=(port, banner, timeout_duration))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("\n[!] No activity. Session timed out. Returning to menu...")
        time.sleep(2)

if __name__ == "__main__":
    main()
