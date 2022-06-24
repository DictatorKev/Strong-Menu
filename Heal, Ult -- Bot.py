from pymem import Pymem
import time
import keyboard 

pm = Pymem("League of Legends.exe")


health = 500 #the player changing health as int or float
key =  "D" #the key to press
address = 0x1A825A34 #the address of your own health with changes (for specific numbers to heal)
address_precentage = 0x1A825A34 #for heal/ult at for example 20% health
cooldown = 300 #the cooldown in seconds of the choosen spell. Int as well as float and goes on seconds.



while True: 
    Stats = pm.read_int(address) #either you take the "precentage" or "address". address if you know when to heal and address_precentage if you want to heal at 20% health or whatever you like.
    #precentage = pm.read_int(address_precentage)
    #precentage = address_precentage/100*20   # must be changed to the precentage you need.
    #print(precentage)
    print(Stats)
    


    if Stats < health: #if your health is less than xxx.. Heal, Ult, use Pot or whatever (int and float). Change health to precentage if you need otherwise.
        try:
            keyboard.press_and_release(key) #what key it is on
            time.sleep(cooldown) #depending on your cooldowns. VERY IMPORTANT TO BE RIGHT!!!!!!!!!!!!!!!!!!!!!
            #breaking the script
        except:
            continue








