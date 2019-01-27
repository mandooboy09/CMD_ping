# PING TOOL
restart = 0
import os

while restart == 0:
    ipaddress = input("목적지 IP 주소 및 포트 입력: ")
    command = "ping " + ipaddress + " -t"
    os.system(command)
    input()
    os.system("CLS")