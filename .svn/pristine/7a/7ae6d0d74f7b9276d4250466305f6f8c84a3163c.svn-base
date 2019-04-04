#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from curses import panel
from os import *
from tool import *
from info_generale import *
from display_proc import *
from conf_curses import *
from display_reseau import *

def signal_handler(signal, frame):#{
    os.system('clear')
    os.system('stty sane')
    print('Ctrl+c pressed, end of the script.')
    sys.exit(0)
#}
signal.signal(signal.SIGINT, signal_handler)

infos_hardware_choos = {
    '1' : "cpu",
    '2' : "memory",
    '3' : "disk"
}

def display_submenu_info1():#{
    choice = 0
    
    while choice < 256 and choice != ord('4'):#{
        screen = init_curses("Hardware information")
        screen.addstr(9, 2, "Please select your choice with numpad 1 to 4", curses.color_pair(2))
        screen.addstr(11, 4, "1 - Display CPU information", curses.color_pair(2))
        screen.addstr(12, 4, "2 - Display memory", curses.color_pair(2))
        screen.addstr(13, 4, "3 - Display memory left", curses.color_pair(2))
        screen.addstr(14, 4, "4 - Exit", curses.color_pair(2))
        screen.refresh()
        choice = screen.getch()
        if choice < 53 and choice > 48 and choice != ord('4'):#{
            curses.endwin()
            system("clear")
            infos_hardware(infos_hardware_choos[chr(choice)])
            system("setterm -term linux -back blue -fore white")
            raw_input("for close press enter")
            system("setterm -term linux -back black -fore white")
        #}
    #}
    curses.endwin()
    return 1
#}

submenu_generale = {
    '1' : version_os,
    '2' : uptime,
    '3' : version_kernel,
    '4' : display_submenu_info1,
    '5' : limit_open_file,
    '6' : limit_open_proc,
    '7' : installed_package
}

def display_info_generale():#{
    choice = 0

    while choice < 256 and choice != ord('8'):#{
        screen = init_curses("generale informations")
        screen.addstr(9, 2, "Please select your choice with numpad 1 to 8", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(11, 4, "1 - Operating system", curses.color_pair(2))
        screen.addstr(12, 4, "2 - Uptime", curses.color_pair(2))
        screen.addstr(13, 4, "3 - Kernel version", curses.color_pair(2))
        screen.addstr(14, 4, "4 - Hardware informations", curses.color_pair(2))
        screen.addstr(15, 4, "5 - Limit of open files", curses.color_pair(2))
        screen.addstr(16, 4, "6 - Limit of open Processes", curses.color_pair(2))
        screen.addstr(17, 4, "7 - Installed package", curses.color_pair(2))
        screen.addstr(18, 4, "8 - Exit", curses.color_pair(2))
        screen.refresh()
        choice = screen.getch()
        if choice < 57 and choice > 48 and choice != ord('8'):#{
            if choice != ord('4'):#{
                curses.endwin()
                system("clear")
            #}
            res = submenu_generale[chr(choice)]()
            if res == 0:
                system("setterm -term linux -back blue -fore white")
                raw_input("for close, press enter")
                system("setterm -term linux -back black -fore white")
        #}
    #}
    curses.endwin()
#}

menu_minitel = {
   '1': display_info_generale,
   '2': display_info_reseau,
   '3': display_info_proc
}

def init_minitel():#{
    choice = 0
    
    while choice < 256 and choice != ord('4'):#{
        screen = init_curses("0")
        screen.addstr(9, 2, "Please select your choice with numpad 1 to 4", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(11, 4, "1 - Generale informations", curses.color_pair(2))
        screen.addstr(12, 4, "2 - Network", curses.color_pair(2))
        screen.addstr(13, 4, "3 - Processes", curses.color_pair(2))
        screen.addstr(14, 4, "4 - Exit", curses.color_pair(2))
        fill_line(screen, 8)
        screen.refresh()
        choice = screen.getch()
        if choice < 53 and choice > 48 and choice != ord('4'):#{{
            curses.endwin()
            system("clear")
            menu_minitel[chr(choice)]()
        #}
    #}
    system("clear")
    os.system('setterm -term linux -back black -fore white')
    curses.endwin()
#}
logo()
init_minitel()
