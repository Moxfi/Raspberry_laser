#CAESAR'S MAILBOX
#
#Mox
#Raspberry Pi, Laser transmission
#Morse protocol with Initiate / End signals
#Comments in english because Github, and it looks better :)
#

#Important imports, but don't make a habit out of " import * "
from gpiozero import *
from time import sleep

#GPIO used for Lightsensor
ldr         = LightSensor(4)

#Timings, Tics and counting them
t           = 1
tic_dit     = 20 * t  #t=2 -> 50-60 upcount
tic_daah    = 80 * t  #t=2 -> 180-200 upcount
tic_ini     = 380 * t #t=2 -> 750ish upcount
tic_end     = 550 * t #t=2 -> 1200ish upcount
tic_space   = 80 * t #t=2 -> 200ish downcount
tic_linebreak = 110 * t
tic_break   = 175 * t #t=2 -> 350ish downcount

#Handling the message and loop variables
upcount     = 0	
downcount   = 20
letter = ""		
message = ""		
i = 0

#Caesar's variables
#Keyset randomized for added "security" -- Breaks as soon as
#attacker gets a hold of it. Also vulnerable for word/letter analysis
#keyset = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 _?;:/.-'"
keyset = "A1S:NRWIH2;VEJCDYTXBO 6F'G.ÄMU?_K5Å/0QÖL98Z34-7P"
n = 10 #default rotation
j = 0
decoded = ""
 
#Inversed Morse Alphabet for de-Morse
inverseMorseAlphabet ={
	'': ' ', 	'.----.': "'",
	'-....-': '-', 	'.-.-.-': '.',  
	'-..-.': '/', 	'---...': ':',  
	'-.-.-.': ';',	'..--..': '?',  
	'..--.-': '_',
	'-----': '0', 	'.----': '1',  
	'..---': '2', 	'...--': '3',  
	'....-': '4', 	'.....': '5',  
	'-....': '6', 	'--...': '7',  
	'---..': '8', 	'----.': '9',  
	'.-': 'A', 	'-...': 'B',  
	'-.-.': 'C', 	'-..': 'D',  
	'.': 'E', 	'..-.': 'F',  
	'--.': 'G', 	'....': 'H',  
	'..': 'I', 	'.---': 'J',  
	'-.-': 'K', 	'.-..': 'L',  
	'--': 'M', 	'-.': 'N',  
	'---': 'O', 	'.--.': 'P',  
	'--.-': 'Q', 	'.-.': 'R',  
	'...': 'S', 	'-': 'T',  
	'..-': 'U', 	'...-': 'V',  
	'.--': 'W', 	'-..-': 'X',  
	'-.--': 'Y',	'--..': 'Z',
	'.--.-': 'Å',	'.-.-': 'Ä',
	'---.': 'Ö'
}


#No fancy defines here unfortunately
#Just the main program 
try:
    while (True):

        #Reset Up/Downcounts
        upcount = 0
        downcount = 0

        #Checking the light value and determining how long it's UP
        while (ldr.value) < 0.2:    
            #Stabilize the counting
            sleep(0.01)		    
            upcount = upcount + 1
            #If light is stuck Up, break the loop
            if (upcount > 1800):
				upcount = 0
                break

        #If light is up for longer than tic_end, do
        #"End of Transmission" things
        if (upcount > tic_end):

            #We need to know the N for Caesar's
            n = int(input("n for rotation: "))
            print("Received:",message)

            #Caesar's cipher - Find symbol in keyset, replace with position-n
            while (j < len(message)):
                decoded = decoded + keyset[int(((keyset.find(message[j])) - (n))) % 48]
                j = j+1
            j = 0

            #Formatting output...
            print("\n--- Start message ---\n")
            print(decoded)
            print("\n--- End message ---")

            #Reset everything for the next message
            message = ""
            upcount = 0
            decoded = ""
            print("\n===> END TRANSMISSION\n")

        #if Light was up for tic_ini, but not for tic_end...
        if (upcount > tic_ini):
            #Initiate transmission
            print("\n===> INI TRANSMISSION \n")
            message = ""
            upcount = 0

        #Handle Daah
        if (upcount > tic_daah):
            letter = letter + "-"
            upcount = 0

        #Handle Dit
        if (upcount > tic_dit):
            letter = letter + "."
            upcount = 0

        #Light was up, it was handled, reset counter
        upcount = 0


        #Checking the light value and determining how long it's DOWN
        while (ldr.value) >= 0.2:
            #Stabilize the counting again
            sleep(0.01)
            downcount = downcount + 1
            #Break out if light's been down for a while
            if (downcount > 1800):
                downcount = 0
                break

        #Print empty line in the message
        if (downcount > tic_break):
            message = message + inverseMorseAlphabet[letter] + "\n"
            letter = ""
            downcount = 0

        #Actually handles REAL spaces in the message
        #Not linebreaks.
        if (downcount > tic_linebreak):
            message = message + inverseMorseAlphabet[letter]
            message = message + " "
            letter = ""
            downcount = 0

        #Only handles downtime between letters!
        if (downcount > tic_space):
            message = message + inverseMorseAlphabet[letter]
            letter = ""
            downcount = 0 

        #Prep for next
        downcount   = 0
        

#Escaping with Ctrl-C? Yes please.
except KeyboardInterrupt:
    pass
