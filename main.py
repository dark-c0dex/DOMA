##########################################################
#                         DOMA                           #
#              An Domain Info Gathering Tool             #
#                  Made By Dark_C0dex                    #
##########################################################

# Importing Modules
import requests
import colorama
import os
import platform
import sys
import concurrent.futures
from colorama import Fore, init

# Setup Colorama
init(autoreset=True)

# Ascii Art Of Doma
ascii_ = fr'''{Fore.RED}
 ________      ______   ___      ___       __      
|"      "\    /    " \ |"  \    /"  |     /""\     
(.  ___  :)  // ____  \ \   \  //   |    /    \    
|: \   ) || /  /    ) :)/\\  \/.    |   /' /\  \   
(| (___\ ||(: (____/ //|: \.        |  //  __'  \  
|:       :) \        / |.  \    /:  | /   /  \\  \ 
(________/   \"_____/  |___|\__/|___|(___/    \___)
                                          {Fore.GREEN}Made BY : Dark_C0dex         
'''

# Api For Graping Domain's Info
api = "https://check-host.net/ip-info/whois"

# Clear Funtion For Clearing Terminul (FOR All OS)
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Main Domain Scrapper
def scrap_domain(api, domain):
    domain = domain.replace("https://", "").replace("http://", "").strip("/")
    payload = {"host": domain}
    try:
        res = requests.post(api, data=payload)
        if res.status_code == 200:
            print(Fore.GREEN + res.text)
        else:
            print(f"{Fore.RED}Domain Not Found")
    except requests.exceptions.RequestException:
        print(f"{Fore.RED}Can't Send Request...")


def Run(api):
    clear()
    print(ascii_)
    domain = input(f"{Fore.CYAN}Enter Your Domain >>> ").strip()
    threads = int(input(f"{Fore.CYAN}Enter Threads >>>"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.submit(scrap_domain, api, domain)

# Runner
if __name__ == '__main__':
    Run(api)
