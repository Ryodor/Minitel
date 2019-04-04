#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from tool import *
import os

def init_curses(menu):#{
    screen = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.cbreak()
    curses.noecho()
    screen.keypad(True)
    screen.clear()
    screen.border(0)
    fill_space(screen)
    title(menu, screen)
    fill_line(screen, 8)
    footer(screen)
    return (screen)
#}

def footer(screen):#{
    max_y , max_x = screen.getmaxyx()
    screen.addstr(max_y - 2, 1, "(C) kabro_c, lorill_j, selatn_r, naze_g", curses.color_pair(2) | curses.A_BOLD)
    return (screen)
#}

def title(menu, screen):
    str1 = "M     M  I  N    N  I  TTTTTTT  EEEEE  L         3333         00"
    str2 = "M M M M  I  N N  N  I     T     E      L        3    3      0   0"
    str3 = "M  M  M  I  N  N N  I     T     EEEE   L            3      0     0"
    str4 = "M     M  I  N   NN  I     T     E      L        3    3      0   0    "
    str5 = "M     M  I  N    N  I     T     EEEEE  LLLLL     3333   0    00 "
    i = 0
    while i <len(str1):
        if str1[i] != " ":
            screen.addstr (2,i + 1, str(str1[i]) , curses.color_pair(4) | curses.A_BOLD)
        else:
            screen.addstr (2,i + 1, " " , curses.color_pair(1) | curses.A_BOLD)
        i += 1
    i = 0
    while i < len(str2):
        if str2[i] != " ":
            screen.addstr (3, i + 1,str(str2[i]), curses.color_pair(4) | curses.A_BOLD)
        else:
            screen.addstr (3,i + 1, " ", curses.color_pair(1) | curses.A_BOLD)
        i += 1
    i = 0
    while i < len(str3):
        if str3[i] != " ":
            screen.addstr (4,i + 1, str(str3[i]), curses.color_pair(4) | curses.A_BOLD)
        else:
            screen.addstr (4,i + 1, " ", curses.color_pair(1) | curses.A_BOLD)
        i += 1
    i = 0
    while i < len(str4):
        if str4[i] != " ":
            screen.addstr (5,i + 1, str(str4[i]), curses.color_pair(4) | curses.A_BOLD)
        else:
            screen.addstr (5,i + 1, " ", curses.color_pair(1) | curses.A_BOLD)
        i += 1
    i = 0
    while i < len(str5):
        if str5[i] != " ":
            screen.addstr (6,i + 1, str(str5[i]), curses.color_pair(4) | curses.A_BOLD)
        else:
            screen.addstr (6,i + 1, " ", curses.color_pair(1) | curses.A_BOLD)
        i += 1
    if menu != "0":
      screen.addstr (8,4, "Menu : " + str(menu), curses.color_pair(4) | curses.A_BOLD) 
