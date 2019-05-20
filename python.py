#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS) #1 - 52 is the possible range

def getMode():
    while True: #keeps repeating until it is true
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #if the user inputs the correct requirements, the program moves on
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #if the user does not input the correct term then it prints this statement

def getMessage():
    print('Enter your message: ')
    return input() #grabbing user's message
    #message = input('Enter your message: ')

def getKey(): #this function forces the key range to be within 1 and 52
    key = 0
    while True: #keeps prompting user for key in range 1 - 52
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE): #if the key is within the requirements, the program moves on
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key #since its decrypting, the key goes in the opposite direction
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key)) #prints the final translated message by using mode, message, key