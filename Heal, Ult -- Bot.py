from pymem import Pymem
import time
import keyboard 

pm = Pymem("League of Legends.exe")

between = input("would you like to heal at a specific healthpoint or precentage? Type either \"Health\" or \"%\"").lower()	



if between == "health":
    health = int(input("At what healthpoint would you like to heal, use pot or Ult at?(only integers)"))
    key1 = input("What key would you like to execute?(only letters)").lower()
    cooldown1 = int(input("What is the cooldown in seconds for the spell?(only integers and pots are always at 16 seconds!!!!)")) #Pots are always at 16 seconds!!!!
    address1 = input("What is the address of your dynamic health?(only integers and either static or dynamic)")
    the_hex = int(address1, 16)
    while True:
        Stats = pm.read_int(the_hex)
        print(Stats)
        try:
            if Stats < health:
                keyboard.press_and_release(key1)
                time.sleep(cooldown1)
        except:
            continue

elif between == "%":
    precentage = int(input("At what precentage would you like to heal, use pot or Ult at?(only integers)"))
    key = input("What key would you like to execute?(only letters)").lower()
    cooldown = int(input("What is the cooldown in seconds for the spell?(only integers and pots are always at 16 seconds!!!!)")) #Pots are always at 16 seconds!!!!
    address2 = input("What is the address of your dynamic health?(only integers and either static or dynamic)")
    address = input("What is the address of your static health?(only integers and either static or dynamic)")
    the_hex1 = int(address2, 16)
    the_hex2 = int(address, 16)
    while True:
        Stats1 = pm.read_int(the_hex1)
        Stats = pm.read_int(the_hex2)
        New_Stats = Stats/100*precentage
        print(Stats1)
        try:
            if Stats1 < New_Stats:
                keyboard.press_and_release(key)
                time.sleep(cooldown)
                print("Script will pause till cooldown is back")
        except:
            continue 







