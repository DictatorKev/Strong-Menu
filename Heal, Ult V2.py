import tkinter as tk
from logging import root
from tracemalloc import start
from pymem import Pymem
import time
import keyboard
import os
from tkinter import*


def new_window():
    master1 = tk.Tk()
    master1.geometry("400x200")
    master1.title("League Bot")
    tk.Label(master1, text="Precentage").grid(row=0)
    tk.Label(master1, text="Key").grid(row=1)
    tk.Label(master1, text="Cooldown").grid(row=2)
    tk.Label(master1, text="Dynamic health address").grid(row=3)
    tk.Label(master1, text="Static health address").grid(row=4)

    
    f1 = tk.Entry(master1)
    f2 = tk.Entry(master1)
    f3 = tk.Entry(master1)
    f4 = tk.Entry(master1)
    f5 = tk.Entry(master1)
    
    f1.grid(row=0, column=1)
    f2.grid(row=1, column=1)
    f3.grid(row=2, column=1)
    f4.grid(row=3, column=1)
    f5.grid(row= 4, column=1)
    def hell():
        pm = Pymem("League of Legends.exe")
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
    tk.Button(master1, text='Quit', command=master1.quit).grid(row=6, column=0, sticky=tk.W, pady=4)
    tk.Button(master1, text='Take the input', command=hell).grid(row=6, column=1, sticky=tk.W, pady=4)
    tk.Button(master1, text="Health", command=new_window2).grid(row=6, column=2, sticky=tk.W, pady=4)
    tk.mainloop()




def new_window2():
    master = tk.Tk()
    master.geometry("400x200")
    master.title("League Bot")
    tk.Label(master, text="Health").grid(row=0)
    tk.Label(master, text="Key").grid(row=1)
    tk.Label(master, text="Cooldown").grid(row=2)
    tk.Label(master, text="Dynamic health address").grid(row=3)
    m1 = tk.Entry(master)
    m2 = tk.Entry(master)
    m3 = tk.Entry(master)
    m4 = tk.Entry(master)
    m1.grid(row=0, column=1)
    m2.grid(row=1, column=1)
    m3.grid(row=2, column=1)
    m4.grid(row=3, column=1)

    def hell2():
        pm = Pymem("League of Legends.exe")
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



    tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Take the input', command=hell2).grid(row=5, column=1, sticky=tk.W, pady=4)
    tk.Button(master, text="Precentage", command=new_window).grid(row=5, column=2, sticky=tk.W, pady=4)
    tk.mainloop()



def show_entry_fields():
    pm = Pymem("League of Legends.exe")

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
master.geometry("400x200")
master.title("League Bot")



tk.Label(master, 
         text="Health").grid(row=0)
tk.Label(master, 
         text="Key").grid(row=1)
tk.Label(master, 
         text="Cooldown").grid(row=2)
tk.Label(master, text="Dynamic health address").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Take the input', command=show_entry_fields).grid(row=5, column=1, sticky=tk.W, pady=4)
tk.Button(master, text="Precentage", command=new_window).grid(row=5, column=2, sticky=tk.W, pady=4)
tk.mainloop()
