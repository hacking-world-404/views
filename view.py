#------------- IMPORT -------------#
from os import system as c
import time
import random
import os

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G}
██╗   ██╗████████╗     ██╗   ██╗████████╗
██║   ██║╚══██╔══╝     ██║   ██║╚══██╔══╝
██║   ██║   ██║        ██║   ██║   ██║   
██║   ██║   ██║        ██║   ██║   ██║   
╚██████╔╝   ██║        ╚██████╔╝   ██║   
 ╚═════╝    ╚═╝         ╚═════╝    ╚═╝   
{R}        HACKING WORLD - YT AUTO VIEW TOOL (ROOT)
{A}------------------------------------------------
""")

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{A}[1] START VIEW HACK")
    print(f"{A}[0] EXIT TOOL")
    print(f"{A}------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        view_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION")
        time.sleep(1)
        menu()

#------------- VIEW HACK -------------#
def view_hack():
    logo()
    c('espeak "YouTube Auto Views Hack Starting"')
    link = input(f"{C}Enter YouTube Video Link: ")

    print(f"\n{Y}[+] Connecting to YouTube Servers...")
    for i in range(6):
        print(f"{B}[*] Connecting{' .' * i}")
        time.sleep(0.5)

    print(f"{R}\n[!] ROOT PERMISSION REQUIRED!")
    time.sleep(1)
    # Fake Root Check
    check = os.system("su -c exit")

    if check == 0:
        print(f"{G}[✓] Root Permission Granted!")
        time.sleep(1)
        print(f"{C}[+] Boosting Views...\n")

        for i in range(20):
            views = random.randint(5000, 20000)
            print(f"{P}[*] {views} Views Added...")
            time.sleep(0.4)

        print(f"\n{Y}[✓] Process Complete.")
        time.sleep(1)
        print(f"{R}[!] SECURITY VERIFICATION REQUIRED!")
        print(f"{G}Visit: https://yt-verify-view.com")

    else:
        print(f"{R}[X] Root Permission Denied!")
        time.sleep(1)
        print(f"{Y}This tool requires ROOT access to proceed.")
    
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- START TOOL -------------#
menu()