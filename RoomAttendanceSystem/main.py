import os, sys, time
import tkinter as tk
import csv
import subprocess

def is_connectable(host):
    ping = subprocess.Popen(['ping','-w','2','-c','1',host], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0


with open('./ip.csv','r') as csvfile:
    iplist = csv.reader(csvfile, delimiter=',')
    
    for row in iplist:
        print(row[2])
        print(is_connectable(row[2]))
        if is_connectable(row[2]) :
            print(f'{row[0]}(id:{row[1]})は研究室にいます')
        else:
            print(f'{row[0]}(id:{row[1]})は研究室にいません')

