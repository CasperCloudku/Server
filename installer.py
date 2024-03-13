import os

def start():

    clear_screen()

    print("Welcome to Installer, lets start setting up!\n\n")
    print("Cloning the repository...\n\n")
    os.system("rm -rf flood.py")
    os.system("git clone https://github.com/CasperCloudku/Server.git")
    print("\n\nDone")
    clear_screen()
    print("\nCongrats. All done!\nTime to start the bot!")
    print("\nInstalling requirements... This might take a while...")
    os.system("pip3 install -r requirements.txt")
    os.system("pip3 install requests")
    clear_screen()
    print("\nStarting...")
    os.system("Python3 flood.py")

start()
