import time
import os
import subprocess
import getpass

inputpasswd = 0
placeholdervariable = 1   #used as a place-holder, ignore

rootusrname = "root"   #the root username, cannot be changed via user interaction
rootpasswd = "python"   #the root password, can be changed

print("Welcome to PythonOS! An incredibly lightweight OS based on Python, with no GUI other than this command prompt.")   #welcome message
usrname = input("Please input a new username: ")
passwd = input("Please create a new password, it cannot be recovered if forgotten, so choose carefully: ")
confirmpasswd = input("Re-type the password to confirm: ")

if passwd == confirmpasswd:  #confirms if first password inputted is equal to the second
    print("Password saved successfully.")
else:
    while passwd != confirmpasswd:  #loops the password change satement until passwd variable is equal to confirmpasswd
        print("Oops! First password does not match second password, please try again.")
        passwd = input("Please create a new password, it cannot be recovered if forgotten, so choose carefully: ")
        confirmpasswd = input("Re-type the password to confirm: ")
    print("Password saved successfully.")

rootpasswdchange = input("Default root password is 'python', would you like to change this? [Y/N]").lower()   #requests the root password to be changed, makes string input lowercase for ease-of-use
if rootpasswdchange == "y":
    rootpasswdchange1 = input("Select a new root password: ")
    rootpasswdchange2 = input("Re-type the password to confirm: ")
    if rootpasswdchange1 == rootpasswdchange2:   #confirms if the first root password inputted is equal to the second
        print("Root password saved successfully.")
    else:
        while rootpasswdchange1 != rootpasswdchange2:   #loops the root password change statement until rootpasswdchange1 variable is equal to rootpasswdchange2
            print("Oops! First password does not match second password, please try again.")
            rootpasswdchange1 = input(print("Select a new root password: "))
            rootpasswdchange2 = input(print("Re-type the password to confirm: "))
        print("Root password saved successfully.")
elif rootpasswdchange == "n":
    print("Okay, root password is unchanged.")
else:
    while rootpasswdchange != "y":   #loops te entire root password statement until rootpasswdchange variable is either "y" or "n"
        if rootpasswdchange != "n":
            print("Oops! What you typed is not one of the options, please try again.")
            rootpasswdchange = input(print("Default root password is 'python', would you like to change this? [Y/N]")).lower()
            if rootpasswdchange == "y":
                rootpasswdchange1 = input(print("Select a new root password: "))
                rootpasswdchange2 = input(print("Re-type the password to confirm: "))
                if rootpasswdchange1 == rootpasswdchange2:
                    print("Root password saved successfully.")
                    rootpasswdchange2 = rootpasswd
                else:
                    while rootpasswdchange1 != rootpasswdchange2:
                        print("Oops! First password does not match second password, please try again.")
                        rootpasswdchange1 = input(print("Select a new root password: "))
                        rootpasswdchange2 = input(print("Re-type the password to confirm: "))
                    print("Root password saved successfully.")
            elif rootpasswdchange == "n":
                print("Okay, root password is unchanged.")

loginusrname = input('Username: ')
loginpasswd = input('Password: ')

if loginusrname == usrname:
    usrnameinfo = "valid"
elif loginusrname == rootusrname:
    usrnameinfo = "admin"
else:
    usrnameinfo = "invalid"

if usrnameinfo == "valid":
    if loginpasswd == passwd:
        passwdinfo = "valid"
    else:
        passwdinfo = "invalid"
        print("Username or password is incorrect, please try again.")
elif usrnameinfo == "admin":
    if loginpasswd == rootpasswd:
        passwdinfo = "admin"
    else:
        passwdinfo = "invalid"
        print("Username or password is incorrect, please try again.")
elif usrnameinfo == "invalid":
    if loginpasswd == passwd:
        passwdinfo = "invalid"
    elif loginpasswd == rootpasswd:
        passwdinfo = "invalid"
    else:
        passwdinfo = "invalid"
        print("Username or password is incorrect, please try again.")

while passwdinfo == "invalid":
    loginusrname = input('Username: ')
    loginpasswd = input('Password: ')

    if loginusrname == usrname:
        usrnameinfo = "valid"
    elif loginusrname == rootusrname:
        usrnameinfo = "admin"
    else:
        usrnameinfo = "invalid"
        print("Username or password is incorrect, please try again.")

    if usrnameinfo == "valid":
        if loginpasswd == passwd:
            passwdinfo = "valid"
        else:
            passwdinfo = "invalid"
            print("Username or password is incorrect, please try again.")
    elif usrnameinfo == "admin":
        if loginpasswd == rootpasswd:
            passwdinfo = "admin"
        else:
            passwdinfo = "invalid"
            print("Username or password is incorrect, please try again.")
    elif usrnameinfo == "invalid":
        if loginpasswd == passwd:
            passwdinfo = "invalid"
        elif loginpasswd == rootpasswd:
            passwdinfo = "invalid"
        else:
            print("Username or password is incorrect, please try again.")

if passwdinfo == "admin":
    print("Logged in as administrator. Please be careful, you have full control over PythonOS.\n")
elif passwdinfo == "valid":
    print("Logged in as normal user. Welcome,", usrname)
elif passwdinfo == "invalid":
    print("If you somehow made it here, there is an error in the code! Check line 122 or previous for errors.\n")
else:
    print("If you somehow made it here, there is an error in the code! Check line 124 or previous for errors.\n")

whattodo = str(input("What would you like to do?\n\n1. Linux Terminal\n2. Log out\n3.Coming soon!\nNone"))
if whattodo == "1":
    linuxcmd = input("Type 'exit' to exit\n>> ").lower()
    pingoperation = "ping "
    exitoperation = "exit"
    pwdoperation = "pwd"
    errorcrtnoperation = " "
    if pingoperation in linuxcmd:
        while pingoperation in linuxcmd:
            os.system(linuxcmd)
        while pingoperation not in linuxcmd:
            print("Error:",linuxcmd, "command not found.")
            while pingoperation not in linuxcmd:
                linuxcmd = input(">> ").lower()
                pingoperation = "ping "
                if pingoperation in linuxcmd:
                    os.system(linuxcmd)
                elif pingoperation not in linuxcmd:
                    print("Error:", linuxcmd, "command not found.")
    elif pwdoperation in linuxcmd:
        while pwdoperation in linuxcmd:
            os.system("pwd")
        while errorcrtnoperation in linuxcmd:
            print("Error:", linuxcmd, "command not found.")
            while errorcrtnoperation not in linuxcmd:
                r
    elif exitoperation in linuxcmd:
        print("\n[process exited with code 1 (0x00000001)]\n")
        while exitoperation in linuxcmd:
            r