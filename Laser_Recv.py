#Raspberry Pi: Laser recv into Morse into message
#by Mox

#Näytti kauniimmalta Notepad++:ssa

from gpiozero import * #Lazymode.
from time import sleep
 
ldr         = LightSensor(4) 	#Pin GPIO4
loop        = 0					#Unused loop?
upcount     = 0					#Initializing
downcount   = 20				#Because we can!

morse_recv = ""					#Morse n shizzle					
letter = ""						#Halp me variable
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
	'-.--': 'Y',	'--..': 'Z'
	'.--.-': 'Å',	'.-.-': 'Ä',
	'---.': 'Ö'
}
 
try:
 
    while (True):
       
        sleep(0.1) 								#Hidastetaan lukutahtia
 
        while (ldr.value) < 0.4:						#Lasketaan kauanko valo on päällä
            sleep(0.01)								#Hidastetaan lukutahtia taas...
            upcount = upcount + 1
            if upcount > 1500:
                break
 
        if ((upcount > 15) & (upcount < 55)):					#Luetaan Dit/Daah
            morse_recv += "."							#ja sijoitetaan piste tai viiva morse_recv:iin
        if ((upcount > 70) & (upcount < 100)):
            morse_recv += "-"
       
        while (ldr.value) > 0.6:						#Lasketaan kauanko valo on pois päältä
            sleep(0.01)								#Hidastetaan lukutahtia taas...
            downcount = downcount + 1
            if downcount > 1500:
                break
 
        if ((downcount > 400) & (downcount < 550)):				#Luetaan välit ja linebreakit
            morse_recv += " "
        if ((downcount >= 550) & (downcount < 1500)):
            morse_recv += "\n"
			
										#Kun morse_recv ei saa enää arvoja pieneen hetkeen...
        if ((downcount >= 1500)):
			if (len(morse_recv) > 0):
				while (i < len(morse_recv)): 			#Kelataan morse_recv läpi merkki kerrallaan
  
					if (morse_recv[i] != " "):  		#Käydään läpi dit ja daah:t, jotka muodostavat
						letter += morse_recv[i]   			#kokonaisen kirjaimen, joka siirretään letter-muuttujaan
  
					elif (morse_recv[i] == " "):  				#Jos merkki katkeaa välilyöntiin
						message += inverseMorseAlphabet[letter] 	#napataan letter:iä vastaava arvo inverseMorseAlphabet:sta
						letter = "" 					#tyhjennetään letter seuraavaa merkkiä varten
  
					else: 							#Jos viesti loppuu kesken, siirretään viimeiset arvot muuttujiin
						letter += morse_recv[i]
						message += inverseMorseAlphabet[letter]
					
					i += 1  						#siirrytään seuraavaan merkkiin morse_recv:ssä

				message += inverseMorseAlphabet[letter] 			#jostain syystä while-loop ei tallenna VIIMEISTÄ merkkiä, joten
												#se tehdään loopin ulkopuolella

				print(message)							#tulostetaan dekoodattu viesti
			
			else:
				print("RECV: null")
			
		upcount     = 0									#Asetetaan arvot nolliin seuraavaa viestiä varten
		downcount   = 20
		morse_recv = ""
		letter = ""
		message = ""
		i = 0
		
       
except KeyboardInterrupt:
    pass
