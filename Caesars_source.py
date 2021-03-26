keyset = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 _?;:/.-'"
n = 10
plaintext = "textgoeshere".upper()
j = 0
encoded = ""
decoded = ""


while (j < len(plaintext)):
       encoded = encoded + keyset[int((n + (keyset.find(plaintext[j])))) % 48]
       j = j+1

j = 0

while (j < len(encoded)):
       decoded = decoded + keyset[int(((keyset.find(encoded[j])) - (n))) % 48]
       j = j+1

j = 0

print("Plaintext:", "".join(plaintext))
print("Encoded:",encoded)
print("Decoded",decoded)
