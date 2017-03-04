#Morse RECV n DECODE
#by Riku "Mox" Ketonen

#ennalta asetettu muuttuja "VIRELABSIIN KESAKSI TOIHIN?"
morse_recv = "...- .. .-. . .-.. .- -... ... .. .. -.  -.- . ... .- -.- ... ..  - --- .. .... .. -.  ..--.."
letter = ""
message = ""
i = 0

#käännetty versio morseaakkosista, numeroista sekä välimerkeistä
inverseMorseAlphabet ={
	'': ' ', 		'.----.': "'",
	'-....-': '-', 	'.-.-.-': '.',  
	'-..-.': '/', 	'---...': ':',  
	'-.-.-.': ';',	'..--..': '?',  
	'..--.-': '_',
	'-----': '0', 	'.----': '1',  
	'..---': '2', 	'...--': '3',  
	'....-': '4', 	'.....': '5',  
	'-....': '6', 	'--...': '7',  
	'---..': '8', 	'----.': '9',  
	'.-': 'A', 		'-...': 'B',  
	'-.-.': 'C', 	'-..': 'D',  
	'.': 'E', 		'..-.': 'F',  
	'--.': 'G', 	'....': 'H',  
	'..': 'I', 		'.---': 'J',  
	'-.-': 'K', 	'.-..': 'L',  
	'--': 'M', 		'-.': 'N',  
	'---': 'O', 	'.--.': 'P',  
	'--.-': 'Q', 	'.-.': 'R',  
	'...': 'S', 	'-': 'T',  
	'..-': 'U', 	'...-': 'V',  
	'.--': 'W', 	'-..-': 'X',  
	'-.--': 'Y',	'--..': 'Z'

}


while (i < len(morse_recv)): 				#Kelataan morse_recv läpi merkki kerrallaan
  
  if (morse_recv[i] != " "):  				#Käydään läpi dit ja daah:t, jotka muodostavat
    letter += morse_recv[i]   				#kokonaisen kirjaimen, joka siirretään letter-muuttujaan
  
  elif (morse_recv[i] == " "):  			#Jos merkki katkeaa välilyöntiin
    message += inverseMorseAlphabet[letter] #napataan letter:iä vastaava arvo inverseMorseAlphabet:sta
    letter = "" 							#tyhjennetään letter seuraavaa merkkiä varten
  
  else: 									#Jos viesti loppuu kesken, siirretään viimeiset arvot muuttujiin
    letter += morse_recv[i]
    message += inverseMorseAlphabet[letter]
  
  
  i += 1  									#siirrytään seuraavaan merkkiin morse_recv:ssä

message += inverseMorseAlphabet[letter] 	#jostain syystä while-loop ei tallenna VIIMEISTÄ merkkiä, joten
											#se tehdään loopin ulkopuolella

print(message)								#tulostetaan dekoodattu viesti
