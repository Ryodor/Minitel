#!/usr/bin/python3
# -*-coding:utf-8 -*
import curses
from os import *
import sys
import time
from proc import *

def fill_line(screen, y):#{
    x = 1
    max_y , max_x = screen.getmaxyx()
    while x < (max_x - 1):#{
        screen.addstr(y, x, "_", curses.color_pair(1) | curses.A_BOLD)
        x += 1
    #}
#}
    
def fill_space(screen):#{
    max_y, max_x = screen.getmaxyx()
    y = 1
    while y < (max_y - 1):#{
        x = 1
        while x < (max_x - 1):#{
            screen.addstr(y, x, ' ', curses.color_pair(1))
            x += 1
        y += 1
        #}
    #}
#}
        
def page_proc(screen):#{
    list_proc = get_process()
    i = 0
    page_tab = []
    max_y, max_x = screen.getmaxyx()
    while i < len(list_proc):#{
        y = 0
        tab = []
        while i < len(list_proc) and y < max_y - 17 and max_y > 16:#{
            tab.append(list_proc[i])
            i += 1
            y += 1
        page_tab.append(tab)
        #}
    #}
    return page_tab
#}

def logo():#{
    screen = curses.initscr()
    max_y, max_x = screen.getmaxyx()
    curses.start_color()
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.cbreak()
    screen.clear()
    screen.border(0)
        #1
    screen.addstr(((max_y - 2) / 2) - 7, ((max_x - 2) / 2) - 15, "          _sudZUZ#Z#XZo=_", curses.color_pair(4) | curses.A_BOLD)
        #2
    screen.addstr(((max_y - 2) / 2) - 6, ((max_x - 2) / 2) - 15, "      _jmZZ2!!~---~!!X##wa", curses.color_pair(4) | curses.A_BOLD)
        #3
    screen.addstr(((max_y - 2) / 2) - 5, ((max_x - 2) / 2) - 15, "   .<wdP~~            -!YZL,", curses.color_pair(4) | curses.A_BOLD)
        #4
    screen.addstr(((max_y - 2) / 2) - 4 , ((max_x - 2) / 2) - 15, "  .mX2'       _%aaa__     XZ[.", curses.color_pair(4) | curses.A_BOLD)
        #5
    screen.addstr(((max_y - 2) / 2) - 3, ((max_x - 2) / 2) - 15, "  oZ[      _jdXY!~?S#wa   ]Xb;", curses.color_pair(4) | curses.A_BOLD)
        #6
    screen.addstr(((max_y - 2) / 2) - 2, ((max_x - 2) / 2) - 15, " _#e'     .]X2(     ~Xw:  )XXc", curses.color_pair(4) | curses.A_BOLD)
        #7
    screen.addstr(((max_y - 2) / 2) - 1, ((max_x - 2) / 2) - 15, ".2Z'      ]X[.       xY:  ]oZ(", curses.color_pair(4) | curses.A_BOLD)
        #8
    screen.addstr((max_y - 2) / 2, ((max_x - 2) / 2) - 15, ".2#;      )3k;     _s!~   jXf'", curses.color_pair(4) | curses.A_BOLD)
        #9
    screen.addstr(((max_y - 2) / 2) + 1, ((max_x - 2) / 2) - 15, " 1Z>      -]Xb/    ~    --#2(", curses.color_pair(4) | curses.A_BOLD)
        #10
    screen.addstr(((max_y - 2) / 2) + 2, ((max_x - 2) / 2) - 15, " -Zo;       +!4ZwaaaauZZXY'", curses.color_pair(4) | curses.A_BOLD)
        #11
    screen.addstr(((max_y - 2) / 2) + 3, ((max_x - 2) / 2) - 15, "  *#[,        ~-?!!!!!!-~", curses.color_pair(4) | curses.A_BOLD)
        #12
    screen.addstr(((max_y - 2) / 2) + 4, ((max_x - 2) / 2) - 15, "   XUB;.", curses.color_pair(4) | curses.A_BOLD)
        #13
    screen.addstr(((max_y - 2) / 2) + 5, ((max_x - 2) / 2) - 15, "    )YXL,,", curses.color_pair(4) | curses.A_BOLD)
        #14
    screen.addstr(((max_y - 2) / 2) + 6, ((max_x - 2) / 2) - 15, "      +3#bc,", curses.color_pair(4) | curses.A_BOLD)
        #15
    screen.addstr(((max_y - 2) / 2) + 7, ((max_x - 2) / 2) - 15, "        -)SSL,,", curses.color_pair(4) | curses.A_BOLD)
        #16
    screen.addstr(((max_y - 2) / 2) + 8, ((max_x - 2) / 2) - 15, "          ~~~~~", curses.color_pair(4) | curses.A_BOLD)
    screen.refresh()
    time.sleep(4)
    curses.endwin()
#}
