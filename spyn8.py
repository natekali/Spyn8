import socket
import sys
import time
import numpy as np

# logo
print("-" * 50)
print("-" * 50)
print("\033[92m#   _____  _____  __     __ _   _   ___    #")
print("#  / ____||  __ \ \ \   / /| \ | | / _ \   #")
print("# | (___  | |__) | \ \_/ / |  \| || (_) |  #")
print("#  \___ \ |  ___/   \   /  | . ` | > _ <   #")
print("#  ____) || |        | |   | |\  || (_) |  #")
print("# |_____/ |_|        |_|   |_| \_| \___/   #")
print("#                                          #\033[0m")
print("########### Provided by \033[92mnatekali\033[0m ###########")
print("####### https://github.com/natekali/ #######")
print("-" * 50)
print("-" * 50)

# function for the option 1
def most_commons():
    print("\033[94m->", domain_name, "have the IP Address :", ip_address, "\033[0m")
    print("\033[93mspyn8 currently working...\033[0m")
    print("With option n°1")
    print("---------------")

    port_list = [21, 22, 23, 25, 53, 80, 110, 135, 137, 139, 145, 443, 1433, 3306, 3389, 5900]

    start = time.time()
    for port in port_list:
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = (ip_address, port)
        bot.settimeout(1)

        response = bot.connect_ex(ip)
        if response == 0:
            print("Port", port, "Open")
            if port == 21:
                print("\033[91mPort 21 FTP\033[0m")
            else:
                pass
            if port == 22:
                print("\033[91mPort 22 SSH (Secure Shell)\033[0m")
            else:
                pass
            if port == 23:
                print("\033[91mPort 23 Telnet\033[0m")
            else:
                pass
            if port == 25:
                print("\033[91mPort 25 SMTP (Simple Mail Transfer Protocol)\033[0m")
            else:
                pass
            if port == 80:
                print("\033[91mPort 80 HTTP\033[0m")
            else:
                pass
            if port == 110:
                print("\033[91mPort 110 POP3\033[0m")
            else:
                pass
            if port == 135:
                print("\033[91mPort 135 TCP et UDP\033[0m")
            else:
                pass
            if port == 137:
                print("\033[91mPort 137 TCP et UDP\033[0m")
            else:
                pass
            if port == 139:
                print("\033[91mPort 139 TCP et UDP\033[0m")
            else:
                pass
            if port == 145:
                print("\033[91mPort 145 IMAP\033[0m")
            else:
                pass
            if port == 443:
                print("\033[91mPort 443 HTTPS\033[0m")
            else:
                pass
            if port == 1433:
                print("\033[91mPort 1433 SQL\033[0m")
            else:
                pass
            if port == 3306:
                print("\033[91mPort 3306 MySQL\033[0m")
            else:
                pass
            if port == 3389:
                print("\033[91mPort 3389 RDP\033[0m")
            else:
                pass
            if port == 5900:
                print("\033[91mPort 5900 VNC\033[0m")
            else:
                pass
        else:
            print("Port", port, "Close")
        bot.close()
    print("---------------")
    end = time.time()
    print("\033[94mExecution time :", int(end) - int(start), "seconds\033[0m")

# function for the option 2
def thousand_ports():
    print("\033[94m->", domain_name, "have the IP Address :", ip_address, "\033[0m")
    print("\033[93mspyn8 currently working...\033[0m")
    print("With option n°2")
    print("---------------")

    port_list1 = np.arange(1, 1001)

    start = time.time()
    for port1 in port_list1:
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = (ip_address, port1)
        bot.settimeout(0.1)

        response = bot.connect_ex(ip)
        if response == 0:
            print("\033[91mPort", port1, "Open\033[0m")
        else:
            pass
        bot.close()
    print("---------------")
    end = time.time()
    print("\033[94mExecution time :", int(end) - int(start), "seconds\033[0m")

# function for the option 3
def all_ports():
    print("\033[94m->", domain_name, "have the IP Address :", ip_address, "\033[0m")
    print("\033[93mspyn8 currently working...\033[0m")
    print("With option n°3")
    print("---------------")

    port_list2 = np.arange(0, 65536)

    start = time.time()
    for port2 in port_list2:
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = (ip_address, port2)
        bot.settimeout(0.1)

        response = bot.connect_ex(ip)
        if response == 0:
            print("\033[91mPort", port2, "Open\033[0m")
        else:
            pass
        bot.close()
    print("---------------")
    end = time.time()
    print("\033[94mExecution time :", int(end) - int(start), "seconds\033[0m")


# extension of domain name for the verification
domain_extensions = [".com", ".fr", ".net", ".me", ".org", ".cn", ".tk", ".gg", ".de", ".uk", ".tw", ".nl", ".ru",
                     ".co", ".us", ".eu", ".info", ".io", ".biz", ".edu", ".pro", ".tv", ".cc", ".ws", ".ly", ".fm",
                     ".guide", ".business", ".store", ".shop", ".tech", ".site", ".cloud", ".art", ".online", ".se"]
print("e.g. Scan for : example.com")
domain_name = input("Scan for : ")

# input first verification with domain extension
if any(extension in domain_name for extension in domain_extensions):
    pass
else:
    print("\033[91mInput is Invalid try again with a real domain name\033[0m")
    sys.exit()

# input second verification with available domain name
socket.setdefaulttimeout(0.5)
try:
    ip_address = socket.gethostbyname(domain_name)
except:
    print("\033[91mThis domain name is not working, try again\033[0m")
    sys.exit()

# main program
print("\033[92m(1)\033[0m Most commons ports | \033[92m(2)\033[0m 1-1000 ports | \033[92m(3)\033[0m All ports")
option = input("I choose the option : ")
if option == str(1):
    most_commons()
elif option == str(2):
    thousand_ports()
elif option == str(3):
    all_ports()
else:
    print("\033[91mRetry and choose between 1, 2 or 3\033[0m")
    sys.exit()
