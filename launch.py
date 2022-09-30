import os
import time
from re import *
import pip
from pkg_resources import DistributionNotFound, VersionConflict

installed = os.system("pip freeze")
required = open('requirements.txt')
reqs = required.readlines()
loggedin = "True".encode()

if installed == None and reqs not in installed:
    print("Requirements not met!")
    time.sleep(0.3333)
    print("Installing all requirements, please wait...")
    time.sleep(1)
    os.system("pip install freegames")
    os.system("pip install GPUtil")
    os.system("pip install psutil")
    os.system("pip install pygame")
    os.system("pip install PyQt5")
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install wolframalpha")
    os.system("pip install pyqtwebengine")
    os.system("pip install hashlib")
else:
    print("Requirements met, starting...")
    time.sleep(1)

from os.path import exists
import hashlib

phvar = 1  # used as a place-holder, ignore

rootusrname = "root"  # the root username, cannot be changed via user interaction
r_p = 'python'
rootpasswd = r_p  # the root password, can be changed

print("""
██████╗░██╗░░░██╗████████╗██╗░░██╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║░░░░░░██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║█████╗██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║╚════╝██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░""")  # welcome message
file_exists = exists('user/rootpassword.txt')
if file_exists == False:
    usrname = input("Please input a new username: ")
    with open('user/username.txt', 'w') as f:
        f.writelines(usrname)
    passwd = input("Please create a new password, it cannot be recovered if forgotten, so choose carefully: ")
    confirmpasswd = input("Re-type the password to confirm: ")
    if passwd == confirmpasswd:  # confirms if first password inputted is equal to the second
        print("Password saved successfully.")
    else:
        while passwd != confirmpasswd:  # loops the password change satement until passwd variable is equal to confirmpasswd
            print("Oops! First password does not match second password, please try again.")
            passwd = input("Please create a new password, it cannot be recovered if forgotten, so choose carefully: ")
            confirmpasswd = input("Re-type the password to confirm: ")
        print("Password saved successfully.")
    hash_passwd = hashlib.md5(passwd.encode())
    with open('user/password.txt', 'w') as f:
        f.writelines(hash_passwd.hexdigest())
    changerp = input("Please create a new ROOT password: ")
    changerp2 = input("Re-type the ROOT password to confirm: ")
    while True:
        if changerp == changerp2:
            print("Root password saved successfully! Welcome to PythOS,", usrname)
            time.sleep(1)
            hash_rootpasswd = hashlib.md5(changerp2.encode())
            with open("user/rootpassword.txt", 'w') as f:
                f.writelines(hash_rootpasswd.hexdigest())
            os.startfile("main.py")
            with open("user/loggedin.txt", 'wb') as f:
                f.write(loggedin)
            break
        elif changerp != changerp2:
            print("Oops! First password does not match second password, please try again.")
            changerp = input("Please create a new ROOT password: ")
            changerp2 = input("Re-type the ROOT password to confirm: ")
        with open("user/loggedin.txt", 'wb') as f:
            f.write(loggedin)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif file_exists == True:
    while True:
        login_usrname = open('user/username.txt')  # opens username text file
        login_passwd = open('user/password.txt')  # opens password text file
        l_u = login_usrname.read()  # reads username from file
        l_p = login_passwd.read()  # reads password from file
        login_rootpasswd = open('user/rootpassword.txt')
        l_rp = login_rootpasswd.read() # reads root password from file
        login = input("Enter password for user " + l_u + ': ')
        hash_login = hashlib.md5(login.encode())
        if hash_login.hexdigest() == l_p:
            os.startfile("main.py")
            with open("user/loggedin.txt", 'wb') as f:
                f.write(loggedin)
            break
        elif hash_login.hexdigest() == l_rp:
            os.startfile("main.py")
            with open("user/loggedin.txt", 'wb') as f:
                f.write(loggedin)
            break
        else:
            print("Wrong password, please try again")