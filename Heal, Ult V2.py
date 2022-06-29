import tkinter as tk
from logging import root
from tracemalloc import start
from pymem import Pymem
import time
import keyboard
import os
from tkinter import*
import random
from tkinter.tix import *






def new_window():
    master1 = Tk()
    master1.geometry("550x240")
    tk.Label(master1, text="Hover over text for more information" ).grid(row=14, column=2, sticky=tk.W, pady=4)

    master1.title("Strong-Menu")
    pley=tk.Label(master1, 
         text="           Game, as example:  League of Legends.exe")
    play = tk.Label(master1, text="Precentage")
    play1 = tk.Label(master1, text="Key, as example: ctrl+shift+f or f")
    play2 = tk.Label(master1, text="Cooldown of the spell")
    play3 = tk.Label(master1, text="Dynamic health/Mana address")
    play4 = tk.Label(master1, text="Static health/Mana address")
    play5 = tk.Label(master1, text="Key,as example: K or W+A+S+D")
    pley.grid(row=0)
    play.grid(row=1)
    play1.grid(row=2)
    play2.grid(row=3)
    play3.grid(row=4)
    play4.grid(row=5)
    play5.grid(row=8)
    tip2= Balloon(master1)

    g2 = tk.Entry(master1)
    f = tk.Entry(master1)
    f1 = tk.Entry(master1)
    f2 = tk.Entry(master1)
    f3 = tk.Entry(master1)
    f4 = tk.Entry(master1)
    f5 = tk.Entry(master1)
    g2.grid(row=8, column=2)
    f.grid(row=0, column=2)
    f1.grid(row=1, column=2)
    f2.grid(row=2, column=2)
    f3.grid(row=3, column=2)
    f4.grid(row=4, column=2)
    f5.grid(row= 5, column=2)
    tip2.bind_widget(pley, balloonmsg="Example: League of Legends.exe, Counter-Strike: Global Offensive.exe,\n Opera.exe etc. Can all be found under the Task Manager.")
    tip2.bind_widget(play, balloonmsg="The position where to execute a spell or anything else you like.\n Example: Execute at 50% HP left, Heal at 40% HP, fill up mana at 30% mana.")
    tip2.bind_widget(play1, balloonmsg="Key that has to be executet at the specific point.\n Example: ctrl+shift+f at 50% HP, ctrl+shift+f at 40% HP, ctrl+shift+f at 30% mana.")
    tip2.bind_widget(play2, balloonmsg="Cooldown of the spell, so it doesn't overlap, spam the entire game or crash your pc \n VERY IMPORTANT, OTHERWISE THERE WILL BE 1000 EXECUTES IN A SECOND.\n IT#S GONNA FUCK YOU UP.")
    tip2.bind_widget(play3, balloonmsg="The hex of the address where my program should look at.\n Adding the address of your currentHealth will check your health 100 times a second and execute your spell once hitting your point.")
    tip2.bind_widget(play4, balloonmsg="The hex of your maximum health, mana or whatever(need to calculate the precentage).")
    tip2.bind_widget(play5, balloonmsg="Keys to execute, make you look like you are not afk and won't kick you out a session. \n is made with random int  as seconds so will be hard to get banned by that.")


    def keyboard_press3():
        while True:
            zeit = random.randint(1, 11)
            zeit2 = random.randint(1, 5)
            key = str(g2.get()).lower()
            time.sleep(zeit)
            keyboard.press_and_release(key)
            time.sleep(zeit2)
    def hell():
        Game = str(f.get())
        pm = Pymem(Game)
        Precentage = int(f1.get())
        print(Precentage)
        Key = f2.get().lower()
        print(Key)
        Cooldown = int(f3.get())
        print(Cooldown)
        real_hex = f4.get()
        real_hax = f5.get()
        real_hax2 = int(real_hax, 16)
        real_hex2 = int(real_hex, 16)
        while True:
            Stats1 = pm.read_int(real_hax2)
            Stats = pm.read_int(real_hex2)
            New_Stats = Stats1/100*Precentage
            print(Stats)
            try:
                if Stats < New_Stats:
                    keyboard.press_and_release(Key)
                    time.sleep(Cooldown)
            except:
                continue
    
    def quit2():
        master1.destroy(), new_window2()
    tk.Button(master1, text='Quit', command=master1.quit).grid(row=6, column=0, sticky=tk.W, pady=4)
    tk.Button(master1, text='Take the input', command=hell).grid(row=6, column=1, sticky=tk.W, pady=4)
    tk.Button(master1, text="Health", command=quit2).grid(row=6, column=2, sticky=tk.W, pady=4)
    tk.Button(master1, text="Anti-AFK", command=keyboard_press3).grid(row=9, column=1, sticky=tk.W, pady=4)
    tk.mainloop()




def new_window2():
    master = Tk()
    master.geometry("550x220")
    tk.Label(master, text="Hover over text for more information" ).grid(row=14, column=2, sticky=tk.W, pady=4)

    master.title("Strong-Menu")
    tip3 = Balloon(master)
    hii = tk.Label(master, text="           Game, as example:  League of Legends.exe")
    hii1 = tk.Label(master, text="Health/Mana")
    hii2 = tk.Label(master, text="Key, as example: ctrl+shift+f or f")
    hii3 = tk.Label(master, text="Cooldown of the spell")
    hii4 = tk.Label(master, text="Dynamic health/Mana address")
    hii5 = tk.Label(master, text="Key,as example: K or W+A+S+D")
    hii.grid(row=0)
    hii1.grid(row=1)
    hii2.grid(row=2)
    hii3.grid(row=3)    
    hii4.grid(row=4)
    hii5.grid(row=8)
    tip3.bind_widget(hii, balloonmsg="Example: League of Legends.exe, Counter-Strike: Global Offensive.exe,\n Opera.exe etc. Can all be found under the Task Manager.")
    tip3.bind_widget(hii1, balloonmsg="The position where to execute a spell or anything else you like.\n Example: Execute at 500 HP, Heal at 400 HP, fill up mana at 300mana.")
    tip3.bind_widget(hii2, balloonmsg="Key that has to be executet at the specific point.\n Example: ctrl+shift+f at 500 HP, ctrl+shift+f at 400 HP, ctrl+shift+f at 300 mana.")
    tip3.bind_widget(hii3, balloonmsg="Cooldown of the spell, so it doesn't overlap, spam the entire game or crash your pc \n VERY IMPORTANT, OTHERWISE THERE WILL BE 1000 EXECUTES IN A SECOND.\n IT#S GONNA FUCK YOU UP.")
    tip3.bind_widget(hii4, balloonmsg="The hex of the address where my program should look at.\n Adding the address of your currentHealth will check your health 100 times a second and execute your spell once hitting your point.")
    tip3.bind_widget(hii5, balloonmsg="Keys to execute, make you look like you are not afk and won't kick you out a session. \n is made with random int  as seconds so will be hard to get banned by that.")

    
    def keyboard_press4():
        while True:
            zeit = random.randint(1, 11)
            zeit2 = random.randint(1, 5)
            key = str(h.get()).lower()
            time.sleep(zeit)
            keyboard.press_and_release(key)
            time.sleep(zeit2)
    h = tk.Entry(master)
    m = tk.Entry(master)
    m1 = tk.Entry(master)
    m2 = tk.Entry(master)
    m3 = tk.Entry(master)
    m4 = tk.Entry(master)
    h.grid(row=8, column=2)
    m.grid(row=0, column=2)
    m1.grid(row=1, column=2)
    m2.grid(row=2, column=2)
    m3.grid(row=3, column=2)
    m4.grid(row=4, column=2)
    

    def hell2():
        Game = str(m.get())
        pm = Pymem(Game)
        Health = int(m1.get())
        print(Health)
        Key = m2.get().lower()
        print(Key)
        Cooldown = int(m3.get())
        print(Cooldown)
        real_hex = m4.get()
        real_hex2 = int(real_hex, 16)
        while True:
            Stats = pm.read_int(real_hex2)
            print(Stats)
            try:
                if Stats < Health:
                    keyboard.press_and_release(Key)
                    time.sleep(Cooldown)
            except:
                continue
    def quit1():
        master.destroy(), new_window()



    tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Take the input', command=hell2).grid(row=5, column=1, sticky=tk.W, pady=4)
    tk.Button(master, text="Precentage", command=quit1).grid(row=5, column=2, sticky=tk.W, pady=4)
    tk.Button(master, text="Anti-AFK", command=keyboard_press4).grid(row=9, column=1, sticky=tk.W, pady=4)
    tk.mainloop()



def show_entry_fields():
    Game = str(e.get())
    pm = Pymem(Game)

    
    Health = int(e1.get())
    print(Health)
    Key = e2.get().lower()
    print(Key)
    Cooldown = int(e3.get())
    print(Cooldown)
    real_hex = e4.get()
    real_hex2 = int(real_hex, 16)
    
    while True:
        Stats = pm.read_int(real_hex2)
        print(Stats)
        try:
            if Stats < Health:
                keyboard.press_and_release(Key)
                time.sleep(Cooldown)
        except:
            continue


master = Tk()
master.geometry("460x220")
master.title("Strong-Menu")
tk.Label(master, text="Hover over text for more information" ).grid(row=14, column=2, sticky=tk.W, pady=4)
game=tk.Label(master, text="  The Game")
tip= Balloon(master)
game2=tk.Label(master, 
         text="Health/Mana")
game3=tk.Label(master, 
         text="Key")
game4=tk.Label(master, 
         text="Cooldown of the spell")
game5=tk.Label(master, text="Dynamic Health/Mana address")
game6=tk.Label(master, text="Keys to execute")
game.grid(row=0)
game2.grid(row=1)
game3.grid(row=2)
game4.grid(row=3)
game5.grid(row=4)
game6.grid(row=8)





tip.bind_widget(game, balloonmsg="Example: League of Legends.exe, Counter-Strike: Global Offensive.exe,\n Opera.exe etc. Can all be found under the Task Manager.")
tip.bind_widget(game2, balloonmsg="The position where to execute a spell or anything else you like.\n Example: Execute at 500 HP, Heal at 400 HP, fill up mana at 300mana.")
tip.bind_widget(game3, balloonmsg="Key that has to be executet at the specific point.\n Example: ctrl+shift+f at 500 HP, ctrl+shift+f at 400 HP, ctrl+shift+f at 300 mana.")
tip.bind_widget(game4, balloonmsg="Cooldown of the spell, so it doesn't overlap, spam the entire game or crash your pc \n VERY IMPORTANT, OTHERWISE THERE WILL BE 1000 EXECUTES IN A SECOND.\n IT#S GONNA FUCK YOU UP.")
tip.bind_widget(game5, balloonmsg="The hex of the address where my program should look at.\n Adding the address of your currentHealth will check your health 100 times a second and execute your spell once hitting your point.")
tip.bind_widget(game6, balloonmsg="Keys to execute, make you look like you are not afk and won't kick you out a session. \n is made with random int  as seconds so will be hard to get banned by that.")





def keyboard_press():
    while True:
        zeit = random.randint(1, 11)
        zeit2 = random.randint(1, 5)
        key = str(g.get()).lower()
        time.sleep(zeit)
        keyboard.press_and_release(key)
        time.sleep(zeit2)

def quit():
    master.destroy(), new_window()  
g = tk.Entry(master)
e = tk.Entry(master)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
g.grid(row=8, column=2)
e.grid(row=0, column=2)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Take the input', command=show_entry_fields).grid(row=5, column=1, sticky=tk.W, pady=4)
tk.Button(master, text="Precentage", command=quit).grid(row=5, column=2, sticky=tk.W, pady=4)
tk.Button(master, text='Anti-AFK', command=keyboard_press).grid(row=9, column=1, sticky=tk.W, pady=4)


tk.mainloop()





