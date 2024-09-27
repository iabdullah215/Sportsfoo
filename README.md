```console
              ██████  ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████   █████▒▒█████   ▒█████  
            ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▓██   ▒▒██▒  ██▒▒██▒  ██▒
            ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒████ ░▒██░  ██▒▒██░  ██▒
              ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒░▓█▒  ░▒██   ██░▒██   ██░
            ▒██████▒▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒░▒█░   ░ ████▓▒░░ ████▓▒░
            ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ 
            ░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░ ░       ░ ▒ ▒░   ░ ▒ ▒░ 
            ░  ░  ░  ░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  
                  ░               ░ ░     ░                    ░             ░ ░      ░ ░  
```

**SportsFoo** is a simple port spoofing tool written in Python that allows you to simulate various services on common ports (HTTP, SSH, SMTP, HTTPS) by sending fake banners. This can be useful for testing and educational purposes, especially in network security scenarios.

## Features

- Spoof multiple common ports:
  - HTTP (80)
  - SSH (22)
  - SMTP (25)
  - HTTPS (443)
- Display customizable banners for each service.
- Multi-threaded handling of incoming connections.
- Timeout mechanism that returns to the menu after inactivity.

## Requirements

- Python 3.x

## Usage
1. Clone the repo.

  ```bash
   git clone https://github.com/yourusername/PortSpoof.git
   cd Sportsfoo
   ```

2. Run the tool:

  ```bash
  python3 sportsfoo.py
  ```

  > Follow the on-screen instructions to select which ports to spoof.

## Menu Options
  When the tool starts, you will see the following options:
  
  ```console
┌──(!abdu11ah㉿MNM)-[~]
└─$ python3 sportsfoo.py  

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

                                                                                                        

[*] Checking System Requirements...
[*] Initializing things...
[*] Starting Sportsfoo...

[=================================================]

[C H O O S E  A N Y  O F  T H E  F O L L O W I N G]

[1] Spoof HTTP (80)
[2] Spoof SSH (22)
[3] Spoof SMTP (25)
[4] Spoof HTTPS (443)
[5] Spoof All
[6] Exit

[=================================================]

[+] Select option(s) (e.g. 1,2):
  ```
  
  > Select the desired option(s) by entering the corresponding number(s) separated by commas.

  ```console
  [=================================================]
  
  [C H O O S E  A N Y  O F  T H E  F O L L O W I N G]
  
  [1] Spoof HTTP (80)
  [2] Spoof SSH (22)
  [3] Spoof SMTP (25)
  [4] Spoof HTTPS (443)
  [5] Spoof All
  [6] Exit
  
  [=================================================]
  
  [+] Select option(s) (e.g. 1,2): 1, 3
  ```
## Disclaimer
  This tool is intended for educational purposes only. Ensure that you have permission to test the network services you are targeting. Use responsibly and ethically.

---

## Usage Example:

```console
[*] Checking System Requirements...
[*] Initializing things...
[*] Starting Sportsfoo...

[=================================================]

[C H O O S E  A N Y  O F  T H E  F O L L O W I N G]

[1] Spoof HTTP (80)
[2] Spoof SSH (22)
[3] Spoof SMTP (25)
[4] Spoof HTTPS (443)
[5] Spoof All
[6] Exit

[=================================================]

[+] Select option(s) (e.g. 1,2): 5
[*] Listening on port 25...
[*] Listening on port 22...
[*] Listening on port 443...
[*] Listening on port 80...
[+] Connection from 127.0.0.1:48332 on port 80
[+] Connection from 127.0.0.1:51092 on port 443
[!] Connection reset by peer on port 443
[!] Connection reset by peer on port 80
[+] Connection from 127.0.0.1:37746 on port 25
[+] Connection from 127.0.0.1:48338 on port 80
[+] Connection from 127.0.0.1:51102 on port 443
[+] Connection from 127.0.0.1:37442 on port 22
[+] Connection from 127.0.0.1:37446 on port 22
[+] Connection from 127.0.0.1:48348 on port 80
[+] Connection from 127.0.0.1:37758 on port 25
[+] Connection from 127.0.0.1:51118 on port 443
[+] Connection from 127.0.0.1:48350 on port 80
[+] Connection from 127.0.0.1:51128 on port 443
[+] Connection from 127.0.0.1:48366 on port 80
[+] Connection from 127.0.0.1:48372 on port 80
[+] Connection from 127.0.0.1:51132 on port 443
[+] Connection from 127.0.0.1:48386 on port 80
[+] Connection from 127.0.0.1:51144 on port 443
[+] Connection from 127.0.0.1:51146 on port 443
[+] Connection from 127.0.0.1:48402 on port 80
[+] Connection from 127.0.0.1:51152 on port 443
[+] Connection from 127.0.0.1:48410 on port 80
[+] Connection from 127.0.0.1:51168 on port 443
[+] Connection from 127.0.0.1:48422 on port 80
[+] Connection from 127.0.0.1:51182 on port 443
[+] Connection from 127.0.0.1:48424 on port 80
[+] Connection from 127.0.0.1:51194 on port 443
```
## Local Host NMAP Scan:

```console
┌──(!abdu11ah㉿MNM)-[~]
└─$ nmap -sV localhost    
Starting Nmap 7.94 ( https://nmap.org ) at 2024-09-26 09:16 EDT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00034s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
25/tcp  open  smtp    Postfix smtpd
80/tcp  open  http    Apache httpd 2.4.41 ((Ubuntu))
443/tcp open  http    nginx 1.18.0 (Ubuntu)
Service Info: Host:  fake-smtp.example.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.39 seconds
```
