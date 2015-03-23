#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ahmed Assal'

import curses
import wordcountSequential as wcSeq
import wordcountMultiprocessing as wcMulti



screen = curses.initscr()
curses.noecho()
curses.curs_set(1)
curses.cbreak()
screen.keypad(True)

screen.addstr(0,0,"Current Mode: Command mode\n\n", curses.A_REVERSE)
screen.addstr("\tInsight Data Engineering Coding Challenge\n\n")
screen.addstr("\n\n\n")
screen.addstr("\t1-Run wordcount sequentially.\n")
screen.addstr("\t2-Run wordcount using Multiprocessing package.\n")
screen.addstr("\t3-Run wordcount using Multiprocessing package.\n")
screen.addstr("\n\n\n\n\n\n\n\n\n\n\n\n")
screen.addstr("\tPlease choose and option\n\n")
while True:
    event = screen.getch()
    if event == ord("q"):
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        break
    elif event == ord("1"):
        screen.addstr("\t\tInsight Data Engineering Coding Challenge\n\n")
        wcSeq.wordCountManager()
    elif event == ord("2"):
        screen.addstr("\t\tInsight Data Engineering Coding Challenge\n\n")
        wcMulti.wordCountManager()
curses.endwin()

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)