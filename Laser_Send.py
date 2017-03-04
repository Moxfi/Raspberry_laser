#Laser_Send
#by Riku "Mox" Ketonen
from gpiozero import *
from time import sleep
 
led = LED(17)
ledloop = 0
 
t = 2
t_dit       = 0.2 * t
t_daah      = 0.5 * t
t_down      = 0.9 * t
t_space     = 1.5 * t
t_break     = 2.0 * t
 
i = 0
morseAlphabet ={
	' ': '', 		"'": '.----.',
	'-': '-....-', 	'.': '.-.-.-',  
	'/': '-..-.', 	':': '---...',  
	';': '-.-.-.',	'?': '..--..',  
	'_': '..--.-',
	'0': '-----', 	'1': '.----',  
	'2': '..---', 	'3': '...--',  
	'4': '....-', 	'5': '.....',  
	'6': '-....', 	'7': '--...',  
	'8': '---..', 	'9': '----.',  
	'A': '.-', 		'B': '-...',  
	'C': '-.-.', 	'D': '-..',  
	'E': '.', 		'F': '..-.',  
	'G': '--.', 	'H': '....',  
	'I': '..', 		'J': '.---',  
	'K': '-.-', 	'L': '.-..',  
	'M': '--', 		'N': '-.',  
	'O': '---', 	'P': '.--.',  
	'Q': '--.-', 	'R': '.-.',  
	'S': '...', 	'T': '-',  
	'U': '..-', 	'V': '...-',  
	'W': '.--', 	'X': '-..-',  
	'Y': '-.--',	'Z': '--..',
	'Å': '.--.-',	'Ä': '.-.-',
	'Ö': '---.'
    }
 
def dit():
    led.off()
    sleep(t_dit)
    led.on()
    sleep(t_down)
 
def daah():
    led.off()
    sleep(t_daah)
    led.on()
    sleep(t_down)
 
def space():
    led.on()
    sleep(t_space)
 
def breaks():
    led.on()
    sleep(t_break)
 
#def
 
print (	"LED values: dit: ",t_dit, ", daah: ",t_daah, ", down: ",t_down, ", space: ",t_space)
 
try:
    while (True):
        cleartext = input("Lähetettävä viesti: ")
        cleartext = cleartext.upper()
		asc2morse = ""
       
        while (i < len(cleartext)):
            asc2morse += morseAlphabet[cleartext[i]] + " "
            i += 1
 
        print("Cleartext to send ", cleartext)
        print("Morse to send ", asc2morse)
        i = 0
        breaks()
 
        while (i < len(asc2morse)):
 
            if (asc2morse[i]) == ".":
                dit()
            elif (asc2morse[i]) == "-":
                daah()
            elif (asc2morse[i]) == " ":
                space()
            i = i+1
			
        i = 0
       
except KeyboardInterrupt:
    pass