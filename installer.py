import os

def start():

    print("Welcome to Installer, lets start setting up!\n\n")
    print("Cloning the repository...\n\n")
    os.system("rm -rf flood.py")
    os.system("wget -O flood.py https://raw.githubusercontent.com/CasperCloudku/Server/main/flood.py")
    os.system("wget -O requirements.txt https://raw.githubusercontent.com/CasperCloudku/Server/main/requirements.txt")
    print("\n\nDone")
    print("\nCongrats. All done!\nTime to start the bot!")
    print("\nInstalling requirements... This might take a while...")
    os.system("pip3 install -r requirements.txt")
    os.system("pip3 install requests")
    os.system("pip3 install pyfiglet")
    os.system("pip3 install animation")
    print("\nStarting...")
    os.system("python3 flood.py")
    os.system("clear")

start()
