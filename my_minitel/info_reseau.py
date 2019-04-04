#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import os
import sys

def get_ip():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/var/lib/dhcp/dhclient.eth0.leases', 'r')
    fileRead = fileOpen.readlines()
    res = fileRead[2]
    fileOpen.close()
    res = res.replace("fixed-address", " ").strip()
    print res.replace(";", " ").strip()
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def is_interface():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/proc/net/dev', 'r')
    fileRead = fileOpen.readlines()
    i = 2
    while i < len(fileRead):#{
        y = 0
        while y < 6:#{
            print fileRead[i][y],
            sys.stdout.softspace=0
            y += 1
        #}
        print ""
        i += 1
    #}
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def get_debit():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    fileOpen = open('/proc/net/dev', 'r')
    fileRead = fileOpen.readlines()
    print "interface | Receive Debit |                                     Transmit Debit"
    i = 2
    while i < len(fileRead):#{
        y = 0
        while y < 74 :#{
            if y < 6:
                print fileRead[i][y],
            elif y < 15:
                print fileRead[i][y],
            elif y > 64 : 
                print fileRead[i][y],
            else: 
                print " ",
            sys.stdout.softspace=0
            y += 1
        #}
        print ""
        i += 1
    #}
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def routes():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    os.system("route -n")
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}
