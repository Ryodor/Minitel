#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import os
from datetime import timedelta
from termcolor import colored

def version_os():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/etc/issue', 'r')
    fileRead = fileOpen.readlines()
    print colored(fileRead[0].rstrip('\n'), 'cyan', 'on_blue')
    fileOpen.close()
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def uptime():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    with open('/proc/uptime', 'r') as f:#{
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    #}
    print colored(uptime_string, 'cyan', 'on_blue')
    os.system('setterm -term linux -back black -fore white')    
    return (0)
#}

def version_kernel():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/proc/version')
    fileRead = fileOpen.read()
    print colored(fileRead.rstrip(), 'cyan', 'on_blue')
    fileOpen.close()
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def infos_hardware(choos):#{
    os.system('setterm -term linux -back blue -fore white')   
    os.system('clear')
    if choos == "cpu":
        fileOpen = open('/proc/cpuinfo')
        fileRead = fileOpen.read()
        print colored(fileRead.rstrip(), 'cyan' ,'on_blue')
        fileOpen.close()
    elif choos == "memory":
        os.system('free | grep "Mem"')
    elif choos == "disk":
        os.system('df -h | grep "/dev/"')
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}
    
def limit_open_file():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/proc/sys/fs/file-nr')
    fileRead = fileOpen.read()
    print colored(fileRead.replace(chr(9), " ").rstrip(), 'cyan', 'on_blue')
    fileOpen.close()
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def limit_open_proc():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/proc/sys/kernel/pid_max')
    fileRead = fileOpen.read()
    print colored(fileRead.rstrip(), 'cyan', 'on_blue')
    fileOpen.close()
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def installed_package():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    os.system("dpkg-query -f '${binary:Package}\n' -W")
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}
