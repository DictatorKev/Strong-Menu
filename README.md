# Bot for every Application

The Bot is now supporting every game.
Only thing to do is adding the game into the first section of the menu like "League of Legends.exe" and fill up the rest.


A bot that heals you automatically, uses pot or ult as soon as you need it (very fast reaction and is kept simple so it won't be detected)

Reading memory and executing keyboard-commands.

you like to heal by a specific amount of health?
May you get extra health if you heal at a specific point of your health, let's say under 20% or under exact 200 health?

just typ it in my script and it will automatically execute the command, so you can concentrate more on other things like dodging, focusing the right enemy, farming etc.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
What you need:
import tkinter as tk
from logging import root
from tracemalloc import start
from pymem import Pymem
import time
import keyboard
import os
from tkinter import*
Install those listet libraries.


You have to indicate :
- the required health to execute (either a number or the precentage).
- the key on your keyboard that will be pressed (example.. F for Heal)
- cooldown depending on your spell. note, you have to change the ult value individiually once the cooldown changes (doesn't include summoner spells since they always stay the same over the entire game).
- Static/Dynamic address of the source (can be found by using tools such as cheat engine, alternatives similar to cheat engine, google or reverse engineering the game but must be up to date!!) I'll be doing a tutorial soon, showing you the beste Way to use it.
https://github.com/Squalr/Squalr/releases/tag/2.3.13)
the program I'm using to get the address.

Please open the .py file with Python, so that the Terminal opens itself too.

