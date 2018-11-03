plaintext =input("Enter Message")

alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key=3
cipher=''

for x in plaintext:
    if x in alph:
        cipher+=alph[(alph.index(x)+key)%len(alph)]

print("Encrypted Message is: " + cipher)