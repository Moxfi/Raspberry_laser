#CAESAR'S MESSENGER
#
#Mox
#Raspberry Pi, Laser transmission
#Morse protocol with Initiate / End signals
#Comments in english because Github, and it looks better :)
#

#Important imports, import * is for the lazy. Don't make a habit out of it.
from gpiozero import *
from time import sleep

#GPIO used for led
led = LED(17)

#Timings for Morse - use same "t" in the receiving end
#Changing t_ values breaks the receiving end
t = 1
t_initiate  = 4.0 * t
t_dit       = 0.33 * t
t_daah      = 1.0 * t
t_down      = 0.5 * t
t_space     = 0.5 * t
t_linebreak = 1.0 * t
t_end       = 6.0 * t
t_quit      = 1.5 * t

#Caesar's variables
#Keyset randomized for added "security" -- Breaks as soon as
#attacker gets a hold of it. Also vulnerable for word/letter analysis
#keyset = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 _?;:/.-'"
keyset = "A1S:NRWIH2;VEJCDYTXBO 6F'G.ÄMU?_K5Å/0QÖL98Z34-7P"
n = 10 #default rotation
j = 0
encoded = ""

#Other nice variables for Loops and Text2Morse
i = 0
morseAlphabet ={
	' ': '', 	"'": '.----.',
	'-': '-....-', 	'.': '.-.-.-',  
	'/': '-..-.', 	':': '---...',  
	';': '-.-.-.',	'?': '..--..',  
	'_': '..--.-',
	'0': '-----', 	'1': '.----',  
	'2': '..---', 	'3': '...--',  
	'4': '....-', 	'5': '.....',  
	'6': '-....', 	'7': '--...',  
	'8': '---..', 	'9': '----.',  
	'A': '.-', 	'B': '-...',  
	'C': '-.-.', 	'D': '-..',  
	'E': '.', 	'F': '..-.',  
	'G': '--.', 	'H': '....',  
	'I': '..', 	'J': '.---',  
	'K': '-.-', 	'L': '.-..',  
	'M': '--', 	'N': '-.',  
	'O': '---', 	'P': '.--.',  
	'Q': '--.-', 	'R': '.-.',  
	'S': '...', 	'T': '-',  
	'U': '..-', 	'V': '...-',  
	'W': '.--', 	'X': '-..-',  
	'Y': '-.--',	'Z': '--..',
	'Å': '.--.-',	'Ä': '.-.-',
	'Ö': '---.'
    }


#Define everything, sleep timings found in the variables above
def initiate():
    led.on()
    sleep(t_down)
    led.off()
    sleep(t_initiate)
    led.on()

def end():
    led.on()
    sleep(t_down)
    led.off()
    sleep(t_end)
    led.on()
    
def dit():
    led.on()
    sleep(t_down)
    led.off()
    sleep(t_dit)
    led.on()

def daah():
    led.on()
    sleep(t_down)
    led.off()
    sleep(t_daah)
    led.on()

def space():
    led.on()
    sleep(t_space)
    led.on()


#Main program starts here
try:
    while (True):

        #Preparing everything
        led.on()
        cleartext = input("Write a message to send: ")
        plaintext = cleartext.upper()
        n = int(input("n for rotation (0-47): "))
        encoded = ""
        asc2morse = ""

        #Caesar's cipher - Find symbol in keyset, replace with n+position
        while (j < len(plaintext)):
            encoded = encoded + keyset[int((n + (keyset.find(plaintext[j])))) % 48]
            j = j+1
        j = 0

        #Encoded to Morse
        while (i < len(encoded)):
            asc2morse = asc2morse + morseAlphabet[encoded[i]] + " "
            i = i+1

        #Print out all the interesting things
        print("n:", n)
        print("Plaintext:", plaintext)
        print("Encoded:",encoded)
        print("Morse to send:", asc2morse)
        i = 0

        #Initiate the transmission
        initiate()

        #asc2morse consists of dots, hyphens and spaces at this point
        #Go through asc2morse symbol by symbol, do things accordingly
        while (i < len(asc2morse)):
            if (asc2morse[i]) == ".":
                dit()
            elif (asc2morse[i]) == "-":
                daah()
            elif (asc2morse[i]) == " ":
                space()
            i = i+1
        i = 0

        #End the transmission
        end()

        #Sleep for t_quit amount of time to keep things under control
        sleep(t_quit)

#Because we want Ctrl-C to work at some point
except KeyboardInterrupt:
    pass
