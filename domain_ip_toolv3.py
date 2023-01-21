import os
import sys
import platform
import socket
import datetime
import platform
import requests
import tkinter as tk
# Add these imports
from typing import Dict
from tkinter.filedialog import askopenfilename
from concurrent.futures import ThreadPoolExecutor

is_windows = True if platform.system() == "Windows" else False

if is_windows:
    os.system(f"title IP to Domain to IP")

def IP_to_Domain():
    root = tk.Tk()
    root.withdraw()
    file_path = askopenfilename()
    use_proxy = input("Do you want to use a proxy? y/n: ")
    proxy = {}
    if use_proxy.upper() == 'Y':
        proxy_file_path = askopenfilename()
        with open(proxy_file_path, 'r') as f:
            lines = f.readlines()
        proxy = {'http': lines[0].strip(), 'https': lines[0].strip()}
    with open(file_path, 'r') as f:
        lines = f.readlines()
    valid_results = []
    invalid_results = []
    thread_count = int(input("Enter the number of threads you want to use (default is 50): ") or 50)
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for i, line in enumerate(lines):
            ip = line.strip()
            if validate_ip(ip):
                future = executor.submit(socket.gethostbyaddr, ip)
                future.add_done_callback(lambda f: valid_results.append(f.result()))
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.stdout.write(f'Checking IP {i+1}/{len(lines)}\r')
                sys.stdout.flush()
            else:
                invalid_results.append(ip)
    sys.stdout.write('\n')
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    os.makedirs('IP to Domain', exist_ok=True)
    with open(os.path.join('IP to Domain', f'IP_to_Domain_{now}_valid_results.txt'), 'w') as f:
        f.write('\n'.join(valid_results))
    with open(os.path.join('IP to Domain', f'IP_to_Domain_{now}_invalid_results.txt'), 'w') as f:
        f.write('\n'.join(invalid_results))

def Domain_to_IP():
    root = tk.Tk()
    root.withdraw()
    file_path = askopenfilename()
    use_proxy = input("Do you want to use a proxy? y/n: ")
    proxy = {}
    if use_proxy.upper() == 'Y':
        proxy_file_path = askopenfilename()
        with open(proxy_file_path, 'r') as f:
            lines = f.readlines()
        proxy = {'http': lines[0].strip(), 'https': lines[0].strip()}
    with open(file_path, 'r') as f:
        lines = f.readlines()
    max_threads = input("Enter the number of max threads you want to use (default = 50): ")
    if max_threads.isdigit():
        max_threads = int(max_threads)
    else:
        max_threads = 50
    valid_results = []
    invalid_results = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i, line in enumerate(lines):
            domain = line.strip()
            if validate_domain(domain):
                future = executor.submit(socket.gethostbyname, domain)
                future.add_done_callback(lambda f: valid_results.append(f.result()))
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.stdout.write(f'Checking Domain {i+1}/{len(lines)}\r')
                sys.stdout.flush()
            else:
                invalid_results.append(domain)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    os.makedirs('Domain to IP', exist_ok=True)
    with open(os.path.join('Domain to IP', f'Domain_to_IP_{now}_valid_results.txt'), 'w') as f:
        f.write('\n'.join(valid_results))
    with open(os.path.join('Domain to IP', f'Domain_to_IP_{now}_invalid_results.txt'), 'w') as f:
        f.write('\n'.join(invalid_results))

# Add these functions
def get_domain_from_ip(ip: str, proxy: Dict[str, str]) -> str:
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        try:
            response = requests.get(f"http://ipinfo.io/{ip}/json", proxies=proxy)
            if response.status_code == 200:
                return response.json()['hostname']
        except requests.exceptions.RequestException:
            pass
    return ""

def get_ip_from_domain(domain: str, proxy: Dict[str, str]) -> str:
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        try:
            response = requests.get(f"http://ipinfo.io/{domain}/json", proxies=proxy)
            if response.status_code == 200:
                return response.json()['ip']
        except requests.exceptions.RequestException:
            pass
    return ""

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def validate_domain(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def print_ascii():
    print("""
                                                       .,-:;//;:=,
                                                  . :H@@@MM@M#H/.,+%;,
                                               ,/X+ +M@@M@MM%=,-%HMMM@X/,
                                             -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
                                            ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
                                          ,%MM@@MH ,@%=             .---=-=:=,.
                                          =@#@@@MX.,                -%HX$$%%%:;
                                         =-./@M@M$                   .;@MMMM@MM:
                                         X@/ -$MM/                    . +MM@@@M$
                                        ,@M@H: :@:                    . =X#@@@@-
                                        ,@@@MMX, .                    /H- ;@M@M=
                                        .H@@@@M@+,                    %MM+..%#$.
                                         /MMMM@MMH/.                  XM@MH; =;
                                          /%+%$XHH@$=              , .H@@@@MX,
                                           .=--------.           -%H.,@@@@@MX,
                                           .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
                                             =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
                                               =%@M@M#@$-.=$@MM@@@M; %M%=
                                                 ,:+$+-,/H#MMMMMMM@= =,
                                                       =++%%%%+/:-.
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii()
    while True:
        print("1. IP to Domain")
        print("2. Domain to IP")
        choice = input("Choose a module: ")
        start_time = datetime.datetime.now()
        if choice == '1':
            IP_to_Domain()
        elif choice == '2':
            Domain_to_IP()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_ascii()
            print("\033[31mInvalid choice\033[0m")
            continue
        end_time = datetime.datetime.now()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Check completed in {end_time - start_time}')
        choice = input("Press R to return to menu or Q to quit: ")
        if choice.upper() == 'Q':
            break

if __name__ == '__main__':
    main()
