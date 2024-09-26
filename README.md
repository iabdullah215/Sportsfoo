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

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/PortSpoof.git
   cd PortSpoof
   ```
2. Run the tool:

  ```bash
  python3 portspoof.py
  ```

  > Follow the on-screen instructions to select which ports to spoof.

## Menu Options
  When the tool starts, you will see the following options:
  
  ```console
  [1] Spoof HTTP (80)
  [2] Spoof SSH (22)
  [3] Spoof SMTP (25)
  [4] Spoof HTTPS (443)
  [5] Spoof All
  [6] Exit
  ```
  
  > Select the desired option(s) by entering the corresponding number(s) separated by commas.

  ```console
  [PORT SPOOFER TOOL]
  [1] Spoof HTTP (80)
  [2] Spoof SSH (22)
  [3] Spoof SMTP (25)
  [4] Spoof HTTPS (443)
  [5] Spoof All
  [6] Exit
  
  Select option(s) (e.g. 1,2): 1, 3
  ```
## Disclaimer
  This tool is intended for educational purposes only. Ensure that you have permission to test the network services you are targeting. Use responsibly and ethically.
