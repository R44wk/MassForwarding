#import sshtunnel
#from sshtunnel import open_tunnel
from time import sleep
import os
import subprocess
import sys
from xml.etree import ElementTree
import xml.etree.ElementTree as ET




def banner():
    print (
"""\n\t
            \033[1;33mDoing '{}' conections wait a bit\033[0;m
----------------------------------------------------------------------
                            |
-------------+              |    +----------+               +---------
    LOCAL    |        SSH   |    |    GW    |      LOCAL    | PRIVATE
    CLIENT   | <===============> |    SSH   | <===========> | SERVER
-------------+              |    +----------+               +---------
                            |
                                                            \033[;35mBy: R4wk\033[0;m
----------------------------------------------------------------------
""".format(len(rports)))

"""
ssh = input(r"Intro Server SSH: ")
sshp = input("Intro PORT Server SSH: ")
user = input(r"Intro USER server SSH: ")
pswd = input(r'server PASSWORD server SSH: ')
rhost = input("Intro IP Host remote: ")
ports = input("Intro ports to forwarding separte for coma (Ex. 22,80,445): ")"""


"""
#Sacando ip de xml
rhost = "172.16.42.2"
file_xml = "/home/r4wk/Downloads/scan.xml"
iplist = []
with open(file_xml,'r') as f:
    tree = ElementTree.parse(f)
#for node in tree.findall('.//port'):
for node in tree.findall('./host/address'): #obteniendo IPAddress
    ip = node.attrib.get('addr')
    if ip:
        iplist.append(ip)
rip = set(iplist) 

if rhost in rip:
    print (rhost, "si")
"""

#SGetting ports from xml
file_xml = "/home/r4wk/Documents/scan.xml"
lista = []
with open(file_xml,'r') as f:
    tree = ElementTree.parse(f)
for node in tree.findall('.//port'):
    port = node.attrib.get('portid')
    if port:
        lista.append(port)
rports = set(lista) 


ssh = "0.tcp.ngrok.io"
sshp = 443
user = "root"
pswd = "p@ssw0rd"
rhost = "10.49.128.199"
rports = "22,80,445,53,5900,8080,443"
rports = rports.split(",")

banner()

for i in rports:

    os.system("sshpass -p {0} ssh -f -N -L {1}:{2}:{1} {3}@{4} -p {5}".format(pswd,i,rhost,user,ssh,sshp))
    print ("\n\tPort forwarding: 127.0.0.1:{0} <<--->> {1}:{0}\n".format(i,rhost))
    
print ("\n\tActive conexions:\n\n")
os.system("netstat -nlpt4 | grep -i \"ssh\"")

while (True):
    print ("\n\n\t\033[1;33m{0} conection done. Press 'q' for exit and close conections: \033[0;m".format(len(rports)))
    option = input("\t\033[;35m~# \033[0;m")
    if option == "q":
        os.system("killall -9 ssh")
        break
else:
    print ("Try again")
    


"""
for i in rports:
    i=int(i)
    
    with open_tunnel(
        ('ssh',sshp),
        ssh_username=user,
        ssh_password=pswd,
        remote_bind_address=(rhost, i),
        local_bind_address=('127.0.0.1', i)
        )as server:
            server.start()
            print ("Conection to tunnel {} <-> {}:{}".format(server.local_bind_address,rhost,i))
            while True:
                sleep(1)         
"""    
    
