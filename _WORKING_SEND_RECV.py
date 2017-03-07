#Riku "Mox" Ketonen
#Raspberry Pi, Laser transmission
#Morse protocol with Initiate / End signals

from gpiozero import *
from time import sleep

led = LED(17)
ledloop = 0

t = 1
t_initiate  = 4.0 * t
t_dit       = 0.33 * t
t_daah      = 1.0 * t
t_down      = 0.5 * t
t_space     = 0.5 * t
t_linebreak = 1.0 * t
t_end       = 6.0 * t
t_quit      = 1.5 * t

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

def linebreak():
    led.on()
    sleep(t_linebreak)


def blink():
    led.on()
    led.off()
    sleep(t_blink)
    led.on()


try:
    while (True):

        led.on()
        cleartext = input("Write a message to send: ")
        asc2morse = ""
        cleartext = cleartext.upper()

        #Cleartext to Morse
        while (i < len(cleartext)):
            asc2morse = asc2morse + morseAlphabet[cleartext[i]] + " "
            i = i+1

        print("Cleartext to send ", cleartext)
        print("Morse to send ", asc2morse)
        i = 0

        initiate()
    
        while (i < len(asc2morse)):

            if (asc2morse[i]) == ".":
                dit()
            elif (asc2morse[i]) == "-":
                daah()
            elif (asc2morse[i]) == " ":
                space()
                
            i = i+1
        i = 0

        end()
        
        sleep(t_quit)
        
except KeyboardInterrupt:
    pass


#Riku "Mox" Ketonen
#Raspberry Pi, Laser transmission
#Morse protocol with Initiate / End signals

from gpiozero import * #Lazymode.
from time import sleep
 
ldr         = LightSensor(4) 	#Pin GPIO4
loop        = 0					#Unused loop?
upcount     = 0					#Initializing
downcount   = 20				#Because we can!

#Timings and Tics
t           = 1
tic_dit     = 20 * t  #t=2 -> 50-60 upcount
tic_daah    = 80 * t  #t=2 -> 180-200 upcount
tic_ini     = 380 * t #t=2 -> 750ish upcount
tic_end     = 550 * t #t=2 -> 1200ish upcount
tic_space   = 90 * t #t=2 -> 200ish downcount
tic_linebreak = 110 * t
tic_break   = 175 * t #t=2 -> 350ish downcount

morse_recv = ""					#Morse n shizzle					
letter = ""					#Halp me variable
message = ""					#You're my only hope
i = 0
 
						#Inversed aakkoset purkamiseen
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
 
try:
    while (True):
       
        upcount = 0
        downcount = 0
        
        while (ldr.value) < 0.2:					#Lasketaan kauanko valo on päällä
            sleep(0.01)							#Hidastetaan lukutahtia taas...
            upcount = upcount + 1
            if (upcount > 1800):
                break

        if (upcount > tic_end):
            message = message + "\n\n--- End message ---"
            print(message)
            print("\nEND TRANSMISSION")
            message = ""
            upcount = 0

        if (upcount > tic_ini):
            print("\nINITIATE\n")
            message = ""
            message = message + "--- Begin message --- \n\n"
            upcount = 0

        if (upcount > tic_daah):
            #print("DAAH")
            letter = letter + "-"
            upcount = 0

        if (upcount > tic_dit):
            #print("DIT")
            letter = letter + "."
            upcount = 0

        upcount = 0
       
        while (ldr.value) >= 0.2:					#Lasketaan kauanko valo on pois päältä
            sleep(0.01)							#Hidastetaan lukutahtia taas...
            downcount = downcount + 1
            if (downcount > 1800):
                downcount = 0
                break

        if (downcount > tic_break):
            #print("\n")
            message = message + inverseMorseAlphabet[letter] + "\n"
            letter = ""
            downcount = 0

        if (downcount > tic_linebreak):
            #print(downcount)
            #print(tic_linebreak)
            #print("Linebreak")
            message = message + inverseMorseAlphabet[letter]
            message = message + " "
            letter = ""
            downcount = 0


        if (downcount > tic_space):
            #print("SPACE")
            message = message + inverseMorseAlphabet[letter]
            letter = ""
            downcount = 0 
        							#Asetetaan arvot nolliin seuraavaa viestiä varten
        downcount   = 0
        
       
except KeyboardInterrupt:
    pass