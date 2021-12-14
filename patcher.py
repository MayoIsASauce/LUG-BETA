import os, threading

logo = "          _____            _____                    _____          \n         /\    \          /\    \                  /\    \         \n        /::\____\        /::\____\                /::\    \        \n       /:::/    /       /:::/    /               /::::\    \       \n      /:::/    /       /:::/    /               /::::::\    \      \n     /:::/    /       /:::/    /               /:::/\:::\    \     \n    /:::/    /       /:::/    /               /:::/  \:::\    \    \n   /:::/    /       /:::/    /               /:::/    \:::\    \   \n  /:::/    /       /:::/    /      _____    /:::/    / \:::\    \  \n /:::/    /       /:::/____/      /\    \  /:::/    /   \:::\ ___\ \n/:::/____/       |:::|    /      /::\____\/:::/____/  ___\:::|    |\n\:::\    \       |:::|____\     /:::/    /\:::\    \ /\  /:::|____|\n \:::\    \       \:::\    \   /:::/    /  \:::\    /::\ \::/    / \n  \:::\    \       \:::\    \ /:::/    /    \:::\   \:::\ \/____/  \n   \:::\    \       \:::\    /:::/    /      \:::\   \:::\____\    \n    \:::\    \       \:::\__/:::/    /        \:::\  /:::/    /    \n     \:::\    \       \::::::::/    /          \:::\/:::/    /     \n      \:::\    \       \::::::/    /            \::::::/    /     \n       \:::\____\       \::::/    /              \::::/    /       \n        \::/    /        \::/____/                \::/____/        \n         \/____/          ~~                                       [v1.0.0] <initial release>\n                                                                 "

def second_task():
    if os.name == "nt":
        os.system("python -m http.server 80")
    else:
        os.system("sudo python -m http.server 80")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

current_authIP:str =  ""
with open("temp", "r") as tmp:
    current_authIP = tmp.read() + "/api/v1/ip"

os.system("curl " + current_authIP + " > temp")

with open("temp", "r") as tmp:
    current_authIP = tmp.read().replace(" ", "")

new_boot:str = "SERVERNAME=0:Lego Universe Gaming (US 1),PATCHSERVERIP=0:localhost,AUTHSERVERIP=0:{0},PATCHSERVERPORT=1:80,LOGGING=1:100,DATACENTERID=5:150,CPCODE=1:89164,AKAMAIDLM=7:0,PATCHSERVERDIR=0:luclient,UGCUSE3DSERVICES=7:1,UGCSERVERIP=0:cache.legouniverse.com,UGCSERVERDIR=0:3dservices,PASSURL=0:https://account.lego.com/en-us/SendPassword.aspx?Username=,SIGNINURL=0:https://account.lego.com/en-us/SignIn.aspx?ReturnUrl=http://universe.lego.com/en-us/myaccount/default.aspx,SIGNUPURL=0:http://universe.lego.com/en-us/myaccount/registration/default.aspx,REGISTERURL=0:https://secure.universe.lego.com/en-us/myaccount/subscription/embeddedlandingpage.aspx?username=,CRASHLOGURL=0:http://services.lego.com/cls.aspx,LOCALE=0:en_US,MANIFESTFILE=0:trunk.txt,TRACK_DSK_USAGE=7:1,HD_SPACE_FREE=5:50180,HD_SPACE_USED=5:16787,USE_CATALOG=7:1".format(current_authIP)

second_worker = threading.Thread(target=second_task)
second_worker.setDaemon(True)

# try:
os.remove("boot.cfg")
with open("boot.cfg", "x") as file:
    file.write(new_boot)
    file.close()

# except Exception:
#     print("error occured deleting/creating boot.cfg default file.")

clear()
# print("Offically licensed client, signed [{0}]".format(random.randint(100000, 300000)))
# print("Copyright: Lego Universe Gaming @ 2021")
# print("Outbound to: " + current_authIP)

print(logo)
print("--------------------------------------------------\nConnected to: {0}".format(current_authIP))

print("\nThis window should close automatically when the game ends, if it does not please close it manually.")

print("\n\nGnome live-patch worker updates:")
second_worker.start()


os.system("legouniverse.exe")
exit()