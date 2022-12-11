import platform
import socket
from os.path import exists
import GPUtil
from PyQt5 import QtNetwork
from tabulate import tabulate
import psutil
import os.path
from pyboy import PyBoy
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
import time
import random
from tkinter import *
from tkinter import messagebox
from random import *
from freegames import *
from turtle import *
from colorama import Fore
import stem.process
import re
import requests
import json
from datetime import datetime

os.system("taskkill /f /im tor.exe")

loggedin = "False"

os.system("mkdir %userprofile%\\Pyth-OS-Files")

os.chdir(os.path.expanduser('~') + "\\Pyth-OS-Files")

romdir_exists = exists(os.path.expanduser('~') + "\\Pyth-OS-Files\\ROMs")

if romdir_exists == False:
    os.system("mkdir %userprofile%\\Pyth-OS-Files\\ROMs")
else:
    pass

usrdir_exists = exists(os.path.expanduser('~') + "\\Pyth-OS-Files\\user")

if usrdir_exists == False:
    os.system("mkdir %userprofile%\\Pyth-OS-Files\\user")
else:
    pass

doom_exists = exists(os.path.expanduser('~') + "\\Pyth-OS-Files\\gzdoom")

if doom_exists == False:
    print("Downloading DOOM, please wait...")
    os.system('powershell "curl https://github.com/WilliamAfton-codes/Pyth-OS/raw/main/gzdoom.zip -o %userprofile%\\Pyth-OS-Files\\gzdoom.zip"')
    os.system("mkdir %userprofile%\\Pyth-OS-Files\\gzdoom")
    os.system('tar -xf %userprofile%\\Pyth-OS-Files\\gzdoom.zip -C %userprofile%\\Pyth-OS-Files\\gzdoom"')
else:
    pass

tor_exists = exists(os.path.expanduser('~') + "\\Pyth-OS-Files\\Tor")

if tor_exists == False:
    print("Downloading TOR, please wait...")
    os.system('powershell "curl https://github.com/WilliamAfton-codes/Pyth-OS/raw/main/Tor%20Proxy.zip -o %userprofile%\\Pyth-OS-Files\\Tor.zip"')
    os.system("mkdir %userprofile%\\Pyth-OS-Files\\Tor")
    os.system('tar -xf %userprofile%\\Pyth-OS-Files\\Tor.zip -C %userprofile%\\Pyth-OS-Files\\Tor"')
else:
    pass

os.system("cls")

def newuser():
    global loggedin
    print(Fore.CYAN + """
██████╗░██╗░░░██╗████████╗██╗░░██╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║░░░░░░██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║█████╗██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║╚════╝██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░""")  # welcome message
    file_exists = exists('user\\rootpassword.txt')
    if file_exists is False:
        usrname = input(Fore.GREEN + "Enter a new username: ")  # Create username
        with open("user\\username.txt", "w") as f:  # Saves username in user folder
            f.writelines(usrname)
        while True:  # Creates password and loops until both passwords match
            passwd = input(Fore.GREEN + "Please enter a new password: ")
            confirmpasswd = input(Fore.GREEN + "Confirm your password: ")
            if passwd == confirmpasswd:
                break
            else:
                print(Fore.RED + "Passwords do not match! Try again.")
        with open("user\\password.txt", "w") as f:
            f.writelines(confirmpasswd)

        while True:  # Creates root password and loops until both root passwords match
            changerp = input(Fore.GREEN + "Please enter a new root password: ")
            changerp2 = input(Fore.GREEN + "Confirm your root password: ")
            if changerp == changerp2:
                break
            else:
                print(Fore.RED + "Passwords do not match! Try again.")
        with open("user\\rootpassword.txt", "w") as f:
            f.writelines(changerp2)
        os.system("cls")
        mainscript()

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif file_exists is True:
        passwdsave = open("user\\password.txt")
        pwds = passwdsave.readline()
        rootpasswdsave = open("user\\rootpassword.txt")
        rpwds = rootpasswdsave.readline()
        while True:
            login = input(Fore.GREEN + "Please enter your password: ")
            if login == pwds:
                break
            elif login == rpwds:
                print(Fore.GREEN + "ROOT password accepted, proceed")
                break
            else:
                print(Fore.RED + "Wrong password! Try again.")
        loggedin = 'True'
        with open("user\\loggedin.txt", "w") as f:
            f.writelines(loggedin)
        os.system("cls")
        mainscript()


def mainscript():
    global loggedin
    global tor_process
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
    loggedinfalse = 'False'
    if l_i == 'False':
        with open("user\\loggedin.txt", "w") as f:
            f.writelines("False")
        print("Not logged in correctly! Relaunch and log in correctly")
    if l_i == 'True':
        with open("user/loggedin.txt", 'w') as f:
            f.writelines(loggedinfalse)
        print(Fore.CYAN + """
██████╗░██╗░░░██╗████████╗██╗░░██╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║░░░░░░██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║█████╗██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║╚════╝██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░""")  # welcome message
        print(Fore.LIGHTBLUE_EX + "Welcome, " + l_u)
        print(Fore.LIGHTBLUE_EX + "Date: " + time.strftime("%d/%m/%y"))

        def batterypercent():
            print(Fore.LIGHTBLUE_EX + "Battery: ", end="", flush=True)

        batterypercent()
        if battery.percent >= 51:
            print(Fore.LIGHTGREEN_EX + str(battery.percent) + "%")
        elif battery.percent <= 50:
            print(Fore.LIGHTRED_EX + str(battery.percent) + "%")
        while True:
            print(Fore.GREEN + """
[1] Web Browser
[2] Text Editor
[3] BioS Utility
[4] Games :D
[5] Powershell / Command Line
[6] Exit""")
            whattodo = str(input("[?]: "))
            if whattodo == '1':
                time.sleep(0.5)
                os.system(r'google.py')
                os.system("cls")
            elif whattodo == '2':
                time.sleep(0.5)
                editor()
                os.system("cls")
            elif whattodo == '3':
                time.sleep(0.5)
                for i in range(1):
                    b_open = input(Fore.GREEN + "To open BioS, enter password for ROOT user : ")
                    if b_open == l_rp:
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
                        print(Fore.BLUE + "\n\nOpening BioS...\n\n")
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
                            tabulate(list_gpus,
                                     headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                              "temperature", "uuid")))
                        input("\nTo exit BioS, press Enter\n")
                    else:
                        print(Fore.RED + "Incorrect! Closing BioS.")
                os.system("cls")
            elif whattodo == '4':
                time.sleep(0.5)
                os.system("cls")
                print(Fore.YELLOW + """\nGAMES!
1: Tic-Tac-Toe
2: Snake
3: 2048
4: Pac-Man
5: DOOM
6: GameBoy Emulator

Type 'exit' to exit.""")
                gamechoice = str(input(Fore.GREEN + "What game do you want to play?: "))
                if gamechoice == '1':
                    time.sleep(0.5)
                    tictactoe()
                    tictactoe()
                    os.system("cls")
                elif gamechoice == '2':
                    time.sleep(0.5)
                    snakegame()
                    snakegame()
                    os.system("cls")
                elif gamechoice == '3':
                    time.sleep(0.5)
                    twenty48()
                    os.system("cls")
                elif gamechoice == '4':
                    time.sleep(0.5)
                    pacman()
                    os.system("cls")
                elif gamechoice == '5':
                    time.sleep(0.5)
                    os.chdir(os.path.expanduser('~') + "\\Pyth-OS-Files")
                    os.system("gzdoom\\gzdoom.exe")
                    os.system("cls")
                elif gamechoice == '6':
                    time.sleep(0.5)
                    os.chdir(os.path.expanduser('~') + "\\Pyth-OS-Files")
                    print(Fore.YELLOW + "Type 'exit' to exit.")
                    time.sleep(0.25)
                    print(Fore.YELLOW + r"Please place your ROM in 'C:\Users\yourusername\Pyth-OS-Files\ROMs\'")
                    romdir = str(input(Fore.GREEN + "What is the name of your ROM? (e.g. pokemon.gb, pokemon.gbc): "))
                    if romdir == "exit":
                        print("Okay, closing...")
                    else:
                        try:
                            pyboy = PyBoy('ROMs\\' + romdir)
                            while not pyboy.tick():
                                pass
                            pyboy.stop()
                        except:
                            print(Fore.RED + "Invalid ROM!")
                            time.sleep(1.5)
                    os.system("cls")
                elif gamechoice == "exit":
                    print(Fore.YELLOW + "Okay, returning to main menu...")
                else:
                    print(Fore.RED + "Invalid game choice! Returning to main menu...")
            elif whattodo == '5':
                os.system("cls")
                print(Fore.YELLOW + "Type 'exit' to exit")
                print(Fore.WHITE + '')
                time.sleep(0.5)
                os.system("powershell")
                os.system("cls")
            elif whattodo == '6':
                with open("user/loggedin.txt", 'w') as f:
                    f.writelines(loggedinfalse)
                time.sleep(0.5)
                print(Fore.YELLOW + "\nOkay, quitting!\n")
                input(Fore.YELLOW + "\n|Process completed, press Enter to close|\n")
                print(Fore.WHITE + '')
                break
            else:
                print(Fore.RED + "\nInvalid program/script!\n")


def editor():
    def process():
        global linecount
        while True:
            lines_input = str(input(">> "))
            lines = lines_input + "\n"
            if lines == "exit-editor\n":
                break
            else:
                fo.writelines(lines)

    if __name__ == "__main__":
        print("Welcome to Python-Notepad! Made with <3 by WilliamAfton-codes\n")

        filename_input = str(input("What would you like the file to be called?: "))
        print("Don't type the '.' in the extension")
        ext_input = str(input("What would you like the extension to be? (Leave blank to default to .txt): "))
        if ext_input == "":
            ext_input = "txt"
        else:
            pass
        filename = filename_input + "." + ext_input

        file_exists = os.path.exists(filename)
        if file_exists is True:
            print("A file with this name in this directory already exists, Python-Notepad will add text to the end")

        fo = open(filename, "a")

        print("Loading text editor...")
        time.sleep(1)
        print("\nType 'exit-editor' to stop writing.")
        process()


def browser():
    os.chdir(os.path.expanduser('~') + "\\Pyth-OS-Files")

    class AboutDialog(QDialog):
        def __init__(self, *args, **kwargs):
            super(AboutDialog, self).__init__(*args, **kwargs)

            QBtn = QDialogButtonBox.Ok  # No cancel
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

            layout = QVBoxLayout()

            title = QLabel("Python-Browse")
            font = title.font()
            font.setPointSize(20)
            title.setFont(font)

            layout.addWidget(title)

            logo = QLabel()
            logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
            layout.addWidget(logo)

            layout.addWidget(QLabel("Version 1.0"))

            for i in range(0, layout.count()):
                layout.itemAt(i).setAlignment(Qt.AlignHCenter)

            layout.addWidget(self.buttonBox)

            self.setLayout(layout)

    class MainWindow(QMainWindow):
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)

            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl("http://google.com"))

            self.browser.urlChanged.connect(self.update_urlbar)
            self.browser.loadFinished.connect(self.update_title)
            self.setCentralWidget(self.browser)

            self.status = QStatusBar()
            self.setStatusBar(self.status)

            navtb = QToolBar("Navigation")
            navtb.setIconSize(QSize(16, 16))
            self.addToolBar(navtb)

            back_btn = QAction(QIcon(os.path.join('images', 'arrow-180.png')), "Back", self)
            back_btn.setStatusTip("Back to previous page")
            back_btn.triggered.connect(self.browser.back)
            navtb.addAction(back_btn)

            next_btn = QAction(QIcon(os.path.join('images', 'arrow-000.png')), "Forward", self)
            next_btn.setStatusTip("Forward to next page")
            next_btn.triggered.connect(self.browser.forward)
            navtb.addAction(next_btn)

            reload_btn = QAction(QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
            reload_btn.setStatusTip("Reload page")
            reload_btn.triggered.connect(self.browser.reload)
            navtb.addAction(reload_btn)

            home_btn = QAction(QIcon(os.path.join('images', 'home.png')), "Home", self)
            home_btn.setStatusTip("Go home")
            home_btn.triggered.connect(self.navigate_home)
            navtb.addAction(home_btn)

            navtb.addSeparator()

            self.httpsicon = QLabel()  # Yes, really!
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
            navtb.addWidget(self.httpsicon)

            self.urlbar = QLineEdit()
            self.urlbar.returnPressed.connect(self.navigate_to_url)
            navtb.addWidget(self.urlbar)

            stop_btn = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
            stop_btn.setStatusTip("Stop loading current page")
            stop_btn.triggered.connect(self.browser.stop)
            navtb.addAction(stop_btn)

            # Uncomment to disable native menubar on Mac
            # self.menuBar().setNativeMenuBar(False)

            file_menu = self.menuBar().addMenu("&File")

            open_file_action = QAction(QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
            open_file_action.setStatusTip("Open from file")
            open_file_action.triggered.connect(self.open_file)
            file_menu.addAction(open_file_action)

            save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
            save_file_action.setStatusTip("Save current page to file")
            save_file_action.triggered.connect(self.save_file)
            file_menu.addAction(save_file_action)

            print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
            print_action.setStatusTip("Print current page")
            print_action.triggered.connect(self.print_page)
            file_menu.addAction(print_action)

            help_menu = self.menuBar().addMenu("&Help")

            about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Python-Browse", self)
            about_action.setStatusTip("Find out more about Python-Browse")  # Hungry!
            about_action.triggered.connect(self.about)
            help_menu.addAction(about_action)

            navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "Python-Browse Homepage",
                                                self)
            navigate_mozarella_action.setStatusTip("Go to Python-Browse Homepage")
            navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
            help_menu.addAction(navigate_mozarella_action)

            self.show()

            self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

        def update_title(self):
            title = self.browser.page().title()
            self.setWindowTitle("%s - Python-Browse" % title)

        def navigate_mozarella(self):
            self.browser.setUrl(QUrl("https://github.com/WilliamAfton-codes/Pyth-OS"))

        def about(self):
            dlg = AboutDialog()
            dlg.exec_()

        def open_file(self):
            filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                      "Hypertext Markup Language (*.htm *.html);;"
                                                      "All files (*.*)")

            if filename:
                with open(filename, 'r') as f:
                    html = f.read()

                self.browser.setHtml(html)
                self.urlbar.setText(filename)

        def save_file(self):
            filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                      "Hypertext Markup Language (*.htm *html);;"
                                                      "All files (*.*)")

            if filename:
                html = self.browser.page().toHtml()
                with open(filename, 'w') as f:
                    f.write(html)

        def print_page(self):
            dlg = QPrintPreviewDialog()
            dlg.paintRequested.connect(self.browser.print_)
            dlg.exec_()

        def navigate_home(self):
            self.browser.setUrl(QUrl("http://google.com"))

        def navigate_to_url(self):  # Does not receive the Url
            q = QUrl(self.urlbar.text())
            if q.scheme() == "":
                q.setScheme("http")

            self.browser.setUrl(q)

        def update_urlbar(self, q):

            if q.scheme() == 'https':
                # Secure padlock icon
                self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))

            else:
                # Insecure padlock icon
                self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))

            self.urlbar.setText(q.toString())
            self.urlbar.setCursorPosition(0)

    if __name__ == "__main__":

        app = QApplication(sys.argv)
        app.setApplicationName("Python-Browse")
        app.setOrganizationName("theplague676")
        app.setOrganizationDomain("https://github.com/WilliamAfton-codes/Pyth-OS")

        proxy = QtNetwork.QNetworkProxy()
        proxy.setType(QtNetwork.QNetworkProxy.Socks5Proxy)
        proxy.setHostName("127.0.0.1")
        proxy.setPort(9050)
        QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

        window = MainWindow()

        app.exec_()


def snakegame():
    try:
        """Snake, classic arcade game.
    
        Exercises
    
        1. How do you make the snake faster or slower?
        2. How can you make the snake go around the edges?
        3. How would you move the food?
        4. Change the snake to respond to mouse clicks.
        """

        food = vector(0, 0)
        snake = [vector(10, 0)]
        aim = vector(0, -10)

        def change(x, y):
            """Change snake direction."""
            aim.x = x
            aim.y = y

        def inside(head):
            """Return True if head inside boundaries."""
            return -200 < head.x < 190 and -200 < head.y < 190

        def move():
            """Move snake forward one segment."""
            head = snake[-1].copy()
            head.move(aim)

            if not inside(head) or head in snake:
                square(head.x, head.y, 9, 'red')
                update()
                return

            snake.append(head)

            if head == food:
                print('Snake:', len(snake))
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10
            else:
                snake.pop(0)

            clear()

            for body in snake:
                square(body.x, body.y, 9, 'black')

            square(food.x, food.y, 9, 'green')
            update()
            ontimer(move, 100)

        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: change(10, 0), 'Right')
        onkey(lambda: change(-10, 0), 'Left')
        onkey(lambda: change(0, 10), 'Up')
        onkey(lambda: change(0, -10), 'Down')
        move()
        done()

    except:
        pass


def twenty48():
    class Board:
        bg_color = {
            '2': '#eee4da',
            '4': '#ede0c8',
            '8': '#edc850',
            '16': '#edc53f',
            '32': '#f67c5f',
            '64': '#f65e3b',
            '128': '#edcf72',
            '256': '#edcc61',
            '512': '#f2b179',
            '1024': '#f59563',
            '2048': '#edc22e',
        }
        color = {
            '2': '#776e65',
            '4': '#f9f6f2',
            '8': '#f9f6f2',
            '16': '#f9f6f2',
            '32': '#f9f6f2',
            '64': '#f9f6f2',
            '128': '#f9f6f2',
            '256': '#f9f6f2',
            '512': '#776e65',
            '1024': '#f9f6f2',
            '2048': '#f9f6f2',
        }

        def __init__(self):
            self.n = 4
            self.window = Tk()
            self.window.title('2048 Game')
            self.gameArea = Frame(self.window, bg='azure3')
            self.board = []
            self.gridCell = [[0] * 4 for i in range(4)]
            self.compress = False
            self.merge = False
            self.moved = False
            self.score = 0
            for i in range(4):
                rows = []
                for j in range(4):
                    l = Label(self.gameArea, text='', bg='azure4',
                              font=('arial', 22, 'bold'), width=4, height=2)
                    l.grid(row=i, column=j, padx=7, pady=7)
                    rows.append(l);
                self.board.append(rows)
            self.gameArea.grid()

        def reverse(self):
            for ind in range(4):
                i = 0
                j = 3
                while (i < j):
                    self.gridCell[ind][i], self.gridCell[ind][j] = self.gridCell[ind][j], self.gridCell[ind][i]
                    i += 1
                    j -= 1

        def transpose(self):
            self.gridCell = [list(t) for t in zip(*self.gridCell)]

        def compressGrid(self):
            self.compress = False
            temp = [[0] * 4 for i in range(4)]
            for i in range(4):
                cnt = 0
                for j in range(4):
                    if self.gridCell[i][j] != 0:
                        temp[i][cnt] = self.gridCell[i][j]
                        if cnt != j:
                            self.compress = True
                        cnt += 1
            self.gridCell = temp

        def mergeGrid(self):
            self.merge = False
            for i in range(4):
                for j in range(4 - 1):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                        self.gridCell[i][j] *= 2
                        self.gridCell[i][j + 1] = 0
                        self.score += self.gridCell[i][j]
                        self.merge = True

        def random_cell(self):
            cells = []
            for i in range(4):
                for j in range(4):
                    if self.gridCell[i][j] == 0:
                        cells.append((i, j))
            curr = random.choice(cells)
            i = curr[0]
            j = curr[1]
            self.gridCell[i][j] = 2

        def can_merge(self):
            for i in range(4):
                for j in range(3):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                        return True

            for i in range(3):
                for j in range(4):
                    if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                        return True
            return False

        def paintGrid(self):
            for i in range(4):
                for j in range(4):
                    if self.gridCell[i][j] == 0:
                        self.board[i][j].config(text='', bg='azure4')
                    else:
                        self.board[i][j].config(text=str(self.gridCell[i][j]),
                                                bg=self.bg_color.get(str(self.gridCell[i][j])),
                                                fg=self.color.get(str(self.gridCell[i][j])))

    class Game:
        def __init__(self, gamepanel):
            self.gamepanel = gamepanel
            self.end = False
            self.won = False

        def start(self):
            self.gamepanel.random_cell()
            self.gamepanel.random_cell()
            self.gamepanel.paintGrid()
            self.gamepanel.window.bind('<Key>', self.link_keys)
            self.gamepanel.window.mainloop()

        def link_keys(self, event):
            if self.end or self.won:
                return
            self.gamepanel.compress = False
            self.gamepanel.merge = False
            self.gamepanel.moved = False
            presed_key = event.keysym
            if presed_key == 'Up':
                self.gamepanel.transpose()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.transpose()
            elif presed_key == 'Down':
                self.gamepanel.transpose()
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
                self.gamepanel.transpose()
            elif presed_key == 'Left':
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
            elif presed_key == 'Right':
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
            else:
                pass
            self.gamepanel.paintGrid()
            print(self.gamepanel.score)
            flag = 0
            for i in range(4):
                for j in range(4):
                    if (self.gamepanel.gridCell[i][j] == 2048):
                        flag = 1
                        break
            if (flag == 1):  # found 2048
                self.won = True
                messagebox.showinfo('2048', message='You Won!')
                print("won")
                return
            for i in range(4):
                for j in range(4):
                    if self.gamepanel.gridCell[i][j] == 0:
                        flag = 1
                        break
            if not (flag or self.gamepanel.can_merge()):
                self.end = True
                messagebox.showinfo('2048', 'Game Over!')
                print("Over")
            if self.gamepanel.moved:
                self.gamepanel.random_cell()

            self.gamepanel.paintGrid()

    gamepanel = Board()
    game2048 = Game(gamepanel)
    game2048.start()


def tictactoe():
    try:
        """Tic Tac Toe
    
        Exercises
    
        1. Give the X and O a different color and width.
        2. What happens when someone taps a taken spot?
        3. How would you detect when someone has won?
        4. How could you create a computer player?
        """

        def grid():
            """Draw tic-tac-toe grid."""
            line(-67, 200, -67, -200)
            line(67, 200, 67, -200)
            line(-200, -67, 200, -67)
            line(-200, 67, 200, 67)

        def drawx(x, y):
            """Draw X player."""
            line(x, y, x + 133, y + 133)
            line(x, y + 133, x + 133, y)

        def drawo(x, y):
            """Draw O player."""
            up()
            goto(x + 67, y + 5)
            down()
            circle(62)

        def floor(value):
            """Round value down to grid with square size 133."""
            return ((value + 200) // 133) * 133 - 200

        state = {'player': 0}
        players = [drawx, drawo]

        def tap(x, y):
            """Draw X or O in tapped square."""
            x = floor(x)
            y = floor(y)
            player = state['player']
            draw = players[player]
            draw(x, y)
            update()
            state['player'] = not player

        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        grid()
        update()
        onscreenclick(tap)
        done()

    except:
        pass


def pacman():
    try:
        """Pacman, classic arcade game.
    
        Exercises
    
        1. Change the board.
        2. Change the number of ghosts.
        3. Change where pacman starts.
        4. Make the ghosts faster/slower.
        5. Make the ghosts smarter.
        """

        from freegames import floor, vector

        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(5, 0)
        pacman = vector(-40, -80)
        ghosts = [
            [vector(-180, 160), vector(5, 0)],
            [vector(-180, -160), vector(0, 5)],
            [vector(100, 160), vector(0, -5)],
            [vector(100, -160), vector(-5, 0)],
        ]
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]

        # fmt: on

        def square(x, y):
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()

            for count in range(4):
                path.forward(20)
                path.left(90)

            path.end_fill()

        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index

        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)

            if tiles[index] == 0:
                return False

            index = offset(point + 19)

            if tiles[index] == 0:
                return False

            return point.x % 20 == 0 or point.y % 20 == 0

        def world():
            """Draw world using path."""
            bgcolor('black')
            path.color('blue')

            for index in range(len(tiles)):
                tile = tiles[index]

                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)

                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(2, 'white')

        def move():
            """Move pacman and all ghosts."""
            writer.undo()
            writer.write(state['score'])

            clear()

            if valid(pacman + aim):
                pacman.move(aim)

            index = offset(pacman)

            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(20, 'yellow')

            for point, course in ghosts:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y

                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'red')

            update()

            for point, course in ghosts:
                if abs(pacman - point) < 20:
                    return

            ontimer(move, 100)

        def change(x, y):
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y

        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.goto(160, 160)
        writer.color('white')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        world()
        move()
        done()

    except:
        pass


def tor_proxy():
    global tor_process



    # -*- coding: utf-8 -*-
    """
    Created on Mon Nov 22 16:56:56 2021

    @author: Yicong
    """


    SOCKS_PORT = 9050
    TOR_PATH = os.path.normpath(os.path.expanduser('~') + "\\Pyth-OS-Files\\Tor\\tor.exe")
    tor_process = stem.process.launch_tor_with_config(
        config={
            'SocksPort': str(SOCKS_PORT),
        },
        init_msg_handler=lambda line: print(line) if re.search('Bootstrapped', line) else False,
        tor_cmd=TOR_PATH
    )

    PROXIES = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    response = requests.get("http://ip-api.com/json/", proxies=PROXIES)
    result = json.loads(response.content)
    print('TOR IP [%s]: %s %s' % (datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))


if __name__ == "__main__":
    tor_proxy()
    newuser()
