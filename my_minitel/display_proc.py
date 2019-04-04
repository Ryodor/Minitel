#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from curses import *
from os import *
from tool import *
from proc import *
from conf_curses import *

def display_process():#{
    choice = 0
    page = 0
    
    while choice < 256 and choice != ord('q') and choice != ord('Q'):#{
        screen = init_curses("Process List")
        screen.addstr(9, 2, "Process List,  Press 'q' for exit", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(10,2, "Press '6' for next page and '4' for prev page", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(11,4, "[PID]", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(12,30, "[Name]", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(12,50, "[Page : " + str(page) + "]", curses.color_pair(2) | curses.A_BOLD)
        tab = page_proc(screen)
        i = 0
        while i < len(tab[page]):#{
            screen.addstr(14 + i,4, str(tab[page][i]['pid']), curses.color_pair(2))
            screen.addstr(14 + i,30, str(tab[page][i]['name']), curses.color_pair(2))
            i += 1
        #}
        screen.refresh()
        choice = screen.getch()
        if choice != ord('q') and choice != ord('Q'):#{
            if choice == ord('4') and page > 0:
                page -= 1
            elif choice == ord('6') and page < len(tab) - 1:
                page += 1
            curses.endwin()
            system("clear")
        #}
    #}
    curses.endwin()
    return (1)
#}

submenu_proc = {
    '1' : display_process,
    '2' : statuts_process,
    '3' : kill_process
}


def display_info_proc():#{
    choice = 0

    while choice < 256 and choice != ord('4'):#{
        screen = init_curses("Procesus")
        screen.addstr(9,2, "Please select your choice with numpad 1 to 4", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(11,4, "1 - Process list", curses.color_pair(2))
        screen.addstr(12,4, "2 - Get process infomation", curses.color_pair(2))
        screen.addstr(13,4, "3 - Kill a process", curses.color_pair(2))
        screen.addstr(14,4, "4 - Exit", curses.color_pair(2))
        screen.refresh()
        choice = screen.getch()
        if choice > 48 and choice < 53 and choice != ord('4'):#{
            curses.endwin()
            system("clear")
            res = submenu_proc[chr(choice)]()
            if res == 0:#{
                system("setterm -term linux -back blue -fore white")
                raw_input("for close press enter")
                system("setterm -term linux -back black -fore white")
            #}
        #}
    #}
    curses.endwin()
#}
