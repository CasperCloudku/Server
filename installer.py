import os

def start():

    print("Welcome to Installer, lets start setting up!\n\n")
    print("Cloning the repository...\n\n")
    os.system("rm -rf flood.py")
    os.system("git clone https://github.com/CasperCloudku/Server.git")
    print("\n\nDone")
    print("\nCongrats. All done!\nTime to start the bot!")
    print("\nInstalling requirements... This might take a while...")
    os.system("pip3 install -r requirements.txt")
    os.system("pip3 install requests")
    print("\nStarting...")
    os.system("Python3 flood.py")
    os.system("clear")

start()
