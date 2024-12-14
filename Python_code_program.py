
program = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

def encrypt(plaintext, secret_key):
  cipher_text = ""
  for character in plaintext:
        if character.isalpha():
           character = character.lower()
           char_index = alphabet.index(character)
           new_index = (char_index + secret_key) % 26
           cipher_char = alphabet[new_index].upper()
        else:
           cipher_char = character

        cipher_text += cipher_char

  print("Your ciphered text is: " + cipher_text)

def decrypt(ciphertext, secret_key):
  plaintext = ""
  for character in ciphertext:
        if character.isalpha():
           character = character.lower()
           char_index = alphabet.index(character)
           new_index = (char_index - secret_key) % 26
           plain_char = alphabet[new_index]
        else:
           plain_char = character

        plaintext += plain_char

  print("Your unciphered text is: " + plaintext)

start = True
name = ("")
password = ("lmao")
keycode = 3
fire = True

while program:

    if start == True:
        print("Hello!")
        name = input("Enter your name: ")
        
    start = False

    if name == ("admin"):

     print("Welcome " + name +".....") 
     print("What would you like to do.")
     print("1. change password")
     print("2. change code")
     print("3. logout")
     menuinput = int(input(":"))
     if menuinput == 1:
                password = input("what would you like to change the password to?: ")

     elif menuinput == 2:
                keycode = int(input("what would you like to change the keycode to?: "))

     elif menuinput == 3:
                print("Goodbye!")
                start = True
     else:
                print ("sorry error")

     menuinput = 0
    elif name != ("admin"):

        if  fire == True:
            firewall = input("Please enter password: ")
        fire = False
    
        if firewall == password:
            print("Welcome " + name +"!") 
            print("What would you like to do.")
            print("1. encrypt a message")
            print("2. decrypt a message")
            print("3. logout")
            menuinput = int(input(":"))

            if menuinput == 1:
                plaintext = input("Enter the message you want to encrypt: ")
                encrypt(plaintext, keycode)  


            elif menuinput == 2:
                ciphertext = input("Enter the message you want to decrypt: ")
                decrypt(ciphertext, keycode)  

            elif menuinput == 3:
                print("Goodbye!")
                start = True
            else:
                print ("sorry error")
                
        else:
            print("Sorry but the password is incorrect. Try again bro...")
            fire = True

program = False