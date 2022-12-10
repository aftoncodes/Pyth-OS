import platform
import socket
import time
from os.path import exists
import GPUtil
from tabulate import tabulate
import psutil
import requests
import wolframalpha
import os.path
import hashlib
from pyboy import WindowEvent, PyBoy

romdir = ""

phvar = 0
directory = os.getcwd()

hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
battery = psutil.sensors_battery()
login_usrname = open('user/username.txt')  # opens username text file
login_passwd = open('user/password.txt')  # opens password text file
l_u = login_usrname.read()  # reads username from file
l_p = login_passwd.read()  # reads password from file
login_rootpassword = open('user/rootpassword.txt')
l_rp = login_rootpassword.read()  # reads root password from file
loggedin = open('user/loggedin.txt')
l_i = loggedin.read()
loggedinfalse = 'False'.encode()
if l_i == 'False':
    with open("user/loggedin.txt", 'wb') as f:
        f.write(loggedinfalse)
    print("Not logged in! Log in by running launch.py and enter your password.")
    print("\n|Process completed, press Enter to close|\n")
    with open("user/loggedin.txt", 'wb') as f:
        f.write(loggedinfalse)
    debug_login = input()
    if debug_login == 'debug':
        print("Logged in as debug, meant ONLY FOR TESTING")
        l_i = 'True'
        time.sleep(1)
    else:
        pass
if l_i == 'True':
    with open("user/loggedin.txt", 'wb') as f:
        f.write(loggedinfalse)
    print("""
██████╗░██╗░░░██╗████████╗██╗░░██╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║░░░░░░██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║█████╗██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║╚════╝██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░""")  # welcome message
    print("Welcome, " + l_u)
    print("Date: " + time.strftime("%d/%m/%y"))


    def batterypercent():
        print("Battery: ", end="", flush=True)


    batterypercent()
    print(battery.percent, "%")
    while True:
        print("""
[1] Web Browser
[2] Text Editor
[3] BioS Utility
[4] Virtual Assistant
[5] Games :D
[6] Powershell / Command Line
[7] Exit""")
        whattodo = int(input("[?]: "))
        if whattodo == 1:
            time.sleep(0.5)
            os.chdir("./browser/")
            os.startfile("google.py")
            os.chdir("..")
        elif whattodo == 2:
            time.sleep(0.5)
            os.startfile("editor.py")
        elif whattodo == 3:
            time.sleep(0.5)
            for i in range(1):
                b_open = input("To open BioS, enter password for ROOT user : ")
                hash_b_open = hashlib.md5(b_open.encode())
                if hash_b_open.hexdigest() == l_rp:
                    gpus = GPUtil.getGPUs()
                    list_gpus = []
                    for gpu in gpus:
                        # get the GPU id
                        gpu_id = gpu.id
                        # name of GPU
                        gpu_name = gpu.name
                        # get % percentage of GPU usage of that GPU
                        gpu_load = f"{gpu.load * 100}%"
                        # get free memory in MB format
                        gpu_free_memory = f"{gpu.memoryFree}MB"
                        # get used memory
                        gpu_used_memory = f"{gpu.memoryUsed}MB"
                        # get total memory
                        gpu_total_memory = f"{gpu.memoryTotal}MB"
                        # get GPU temperature in Celsius
                        gpu_temperature = f"{gpu.temperature} °C"
                        gpu_uuid = gpu.uuid
                        list_gpus.append((
                            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                            gpu_total_memory, gpu_temperature, gpu_uuid
                        ))
                    print("\n\nOpening BioS...\n\n")
                    time.sleep(2)
                    hostname = socket.gethostname()
                    hostip = socket.gethostbyname(hostname)
                    print("USERNAME: " + l_u)
                    print("PASSWORD: " + l_p)
                    print("HOST NAME: ", hostname)
                    print("LAN IP: " + hostip)
                    url = f'https://api.ipify.org/?format=json'
                    response = requests.get(url)
                    wanip = response.json()['ip']
                    print("WAN IP: ", wanip)
                    my_system = platform.uname()
                    print(f"System: {my_system.system}")
                    print(f"Machine: {my_system.machine}")
                    print(f"CPU: {my_system.processor}")
                    print("GPU: " + gpu_name)
                    print("=" * 40, "CPU Info", "=" * 40)
                    # number of cores
                    print("Physical cores:", psutil.cpu_count(logical=False))
                    print("Total cores:", psutil.cpu_count(logical=True))
                    # CPU frequencies
                    cpufreq = psutil.cpu_freq()
                    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
                    print("=" * 70, "GPU Details", "=" * 70)
                    print(
                        tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                                     "temperature", "uuid")))
                    input("\nTo exit BioS, press Enter\n")
                else:
                    print("Incorrect! Closing BioS.")
        elif whattodo == 4:
            time.sleep(0.5)
            for i in range(1):
                print("Virtual Assistant using Wolfram|Alpha API")
            while True:
                # Taking input from user
                wolfram_query = input('What would you like to know? (Type exit to exit): ')
                if wolfram_query == 'exit':
                    print("\nOkay, quitting Virtual Assistant\n")
                    break
                wolfram_app_id = 'KW896T-R8UQR8ET4V'
                wolfram_client = wolframalpha.Client(wolfram_app_id)
                wolfram_res = wolfram_client.query(wolfram_query)
                wolfram_answer = next(wolfram_res.results).text
                print(wolfram_answer)
        elif whattodo == 5:
            time.sleep(0.5)
            print("""\nGAMES!
1: Tic-Tac-Toe
2: Snake
3: 2048
4: Pac-Man
5: DOOM
6: GameBoy Emulator

Type 'exit' to exit.""")
            gamechoice = str(input("What game do you want to play?: "))
            if gamechoice == '1':
                time.sleep(0.5)
                os.chdir("games")
                os.startfile("tictactoe.py")
                os.chdir("..")
            elif gamechoice == '2':
                time.sleep(0.5)
                os.chdir("games")
                os.startfile("snake.py")
                os.chdir("..")
            elif gamechoice == '3':
                time.sleep(0.5)
                os.chdir("games")
                os.startfile("2048.py")
                os.chdir("..")
            elif gamechoice == '4':
                time.sleep(0.5)
                os.chdir("games")
                os.startfile("pacman.py")
                os.chdir("..")
            elif gamechoice == '5':
                time.sleep(0.5)
                os.chdir("games/doom")
                os.system("gzdoom.exe")
                os.chdir("..")
                os.chdir("..")
            elif gamechoice == '6':
                time.sleep(0.5)
                print("Please place your ROM in the 'ROMs' folder")
                romdir = str(input("What is the name of your ROM? (e.g. pokemon.gb, pokemon.gbc): "))
                if romdir == "exit":
                    print("Okay, closing...")
                else:
                    try:
                        pyboy = PyBoy('ROMs\\' + romdir)
                        while not pyboy.tick():
                            pass
                        pyboy.stop()
                    except:
                        print("Invalid ROM!")
            elif gamechoice == "exit":
                print("Okay, returning to main menu...")
            else:
                print("Invalid game choice! Returning to main menu...")
        elif whattodo == 6:
            for i in range(1):
                print("Type 'exit' to exit")
                time.sleep(0.5)
                os.system("powershell")
        elif whattodo == 7:
            with open("user/loggedin.txt", 'wb') as f:
                f.write(loggedinfalse)
            time.sleep(0.5)
            print("\nOkay, quitting!\n")
            input("\n|Process completed, press Enter to close|\n")
            break
        else:
            print("\nInvalid program/script!\n")
