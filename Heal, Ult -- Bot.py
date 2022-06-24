from pymem import Pymem
import time as sleep
import keyboard 

pm = Pymem("League of Legends.exe")


health =  #the target health as int or float
key =  "" #the key to press
address = "" #the address of the own health
cooldown =  #the cooldown in seconds of the choosen spell. Int as well as float and goes on seconds.


while True: 
    Stats = pm.read_int(address)
    #Static Address of the source
    #can be founde by reverse engineering the game or google
    print(Stats)
    
    
    
    if Stats < health: #if your health is less than xxx.. Heal, Ult, use Pot or whatever (int and float). 
        try:
            keyboard.press_and_release(key) #what key it is on
            sleep(cooldown) #depending on your cooldowns. VERY IMPORTANT TO BE RIGHT!!!!!!!!!!!!!!!!!!!!!
            #breaking the script
        except:
            continue



