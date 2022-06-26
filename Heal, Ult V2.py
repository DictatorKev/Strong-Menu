import tkinter as tk
from logging import root
from tracemalloc import start
from pymem import Pymem
import time
import keyboard
import os
from tkinter import*
import pyperclip



def new_window():
    master1 = tk.Tk()
    master1.geometry("400x200")
    master1.title("Strong-Menu")
    tk.Label(master1, 
         text="           Game, as example:  League of Legends.exe").grid(row=0)
    tk.Label(master1, text="Precentage").grid(row=1)
    tk.Label(master1, text="Key, as example: ctrl+shift+f or f").grid(row=2)
    tk.Label(master1, text="Cooldown of the spell").grid(row=3)
    tk.Label(master1, text="Dynamic health/Mana address").grid(row=4)
    tk.Label(master1, text="Static health/Mana address").grid(row=5)

    f = tk.Entry(master1)
    f1 = tk.Entry(master1)
    f2 = tk.Entry(master1)
    f3 = tk.Entry(master1)
    f4 = tk.Entry(master1)
    f5 = tk.Entry(master1)
    f.grid(row=0, column=1)
    f1.grid(row=1, column=1)
    f2.grid(row=2, column=1)
    f3.grid(row=3, column=1)
    f4.grid(row=4, column=1)
    f5.grid(row= 5, column=1)
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
    tk.mainloop()




def new_window2():
    master = tk.Tk()
    master.geometry("400x200")
    master.title("Strong-Menu")
    tk.Label(master, 
         text="           Game, as example:  League of Legends.exe").grid(row=0)
    tk.Label(master, text="Health/Mana").grid(row=1)
    tk.Label(master, text="Key, as example: ctrl+shift+f or f").grid(row=2)
    tk.Label(master, text="Cooldown of the spell").grid(row=3)
    tk.Label(master, text="Dynamic health/Mana address").grid(row=4)
    m = tk.Entry(master)
    m1 = tk.Entry(master)
    m2 = tk.Entry(master)
    m3 = tk.Entry(master)
    m4 = tk.Entry(master)
    m.grid(row=0, column=1)
    m1.grid(row=1, column=1)
    m2.grid(row=2, column=1)
    m3.grid(row=3, column=1)
    m4.grid(row=4, column=1)

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


master = tk.Tk()
master.geometry("700x200")
master.title("Strong-Menu")


tk.Label(master, 
         text="           Game, as example:  League of Legends.exe").grid(row=0)
tk.Label(master, 
         text="Health/Mana").grid(row=1)
tk.Label(master, 
         text="Key, as example: ctrl+shift+f or f").grid(row=2)
tk.Label(master, 
         text="Cooldown of the spell").grid(row=3)
tk.Label(master, text="Dynamic Health/Mana address").grid(row=4)

def quit():
    master.destroy(), new_window()  

e = tk.Entry(master)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e.grid(row=0, column=2)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Take the input', command=show_entry_fields).grid(row=5, column=1, sticky=tk.W, pady=4)
tk.Button(master, text="Precentage", command=quit).grid(row=5, column=2, sticky=tk.W, pady=4)
tk.mainloop()





