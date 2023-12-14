print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encryption")
    message = input('enter your message: ')
    key = int(input('enter key(1-94): '))
    encrypted_text = ''
    for i in range(len(message)):
        temp = (ord(message[i])+key)
        if(temp > 126):
            temp = temp-127+32
            encrypted_text += chr(temp)
    print('encrypted'+encrypted_text)
    main()
    
#------------------------------------------------------------------------------------------------------------------#
def decryption():
    print("decryption")
    print("Message can only be Lower or Uppercase alphabet")
    encrp_msg = input("Enter encrypted Text: ")
    decrp_key = int(input("Enter key(1-94): "))

    decrypted_text = ""

    for i in range(len(encrp_msg)):
        temp = (ord(encrp_msg[i]) - decrp_key)
        if(temp < 32):
            temp = temp + 127 - 32
        decrypted_text += chr(temp)

    print("Decrypted Text: " + decrypted_text)
#-----------------------------------------------------------------------------------------------------------------#
        
if __name__ == "__main__":
    main()