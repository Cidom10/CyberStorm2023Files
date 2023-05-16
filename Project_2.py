#######################################################################################################################
# Group Members: Reese Seals, Trisha Carter, Calvin Idom, Samman Regmi, Michael Herbert, Ben Meister, Cameron McCarthy
#######################################################################################################################
# imported the system library
import sys

# Created an Function that encryptes Messages with a key
def Library(key, message):

    # if message isn't a character between a-z on the ascii table
    # return message, example: return an " "(space) if passed through function
    if (ord(message.lower())<97 or ord(message.lower())>122):
        return message
    
    # Check if message is captialized 
    if (message.upper() == message):
        # add the number corresponding to letter, ex: a = 0, b=1..
        New = ord(key.lower()) + ord(message.lower())-97
        # if New overflows past 122 on ascii table, restart at 97 and add the remaining amount
        if (New >122):
            New = New -26
        # return the character in upper case form
        return chr(New).upper()
    
    # if not captialized, proceed with normal function Like above
    else:
        New = ord(key.lower()) + ord(message.lower())-97
        if (New >122):
            New = New -26
        return chr(New)

# Function to Decipyer any message with given key
def Decription(key, message):

    # Check if message and key equal each other
    # if they do, the character has to be 'a' or 'A'
    if (ord(message.lower())==ord(key.lower())):
        if (message.upper() == message):
            return chr(97).upper()
        return chr(97)
    
    # Check if message is a character a-z, 
    # if not, then return the message as it is 
    if (ord(message.lower())<97 or ord(message.lower())>122):
        return message
    
    # Check if message is uppercase
    # then proceed with protocol
    if (message.upper() == message):

        # if the key ascii value is less than message ascii value
        # aka no overflow, then just add the corrponding value onto a
        # ascii value to get the orginal message
        if (ord(key.lower())<ord(message.lower())):
            New= abs(ord(message.lower())-ord(key.lower()))+97

        # figure out the overflow amount
        # then add it to 'a' ascii value to get orginal message
        else:
            New = 123-ord(key.lower())+ord(message.lower())
        # uppercase the end result
        return chr(New).upper()
    
    # if it isn't captialized then proceed with normal protocol
    # just don't uppercase the end result
    else:
        if (ord(key.lower())<ord(message.lower())):
            New= abs(ord(message.lower())-ord(key.lower()))+97
        else:
            New = 123-ord(key.lower())+ord(message.lower())
        return chr(New)


while(1):
    try:
        # create an output string, a counter, and the length of the key
        Output = ""
        count = 0
        if (len(sys.argv) > 2):
            argument = sys.argv[2]

            # check if encrypting
            if (sys.argv[1] == '-e'):

                # take input if not given
                # or take input from stdin and put into word variable
                word = input("")
                
                # for each indiviual letter in the input, encrypt it
                for value in word:
                    # when the key word ends, reset it
                    if (count == len(argument)):
                        count =0
                    # if theres an space in key, skip to the next character
                    while(sys.argv[2][count] == " "):
                        count+=1
                    if (value == " "):
                        Output+=" "
                    else:
                        # add the encrypted character to output
                        Output+=Library(sys.argv[2][count], value)
                        # increment to the next key letter
                        count+=1
                
                # print out the final result
                print(Output)

            # check if decryption
            # works exact same as encryption
            # except use the decryption library
            if (sys.argv[1] == '-d'):
                word = input("")
                for value in word:
                    if (count == len(argument)):
                        count =0
                    while(sys.argv[2][count] == " "):
                        count+=1
                    if (value == " "):
                        Output+=" "
                    else:
                        Output+=Decription(sys.argv[2][count], value)
                        count+=1
                print(Output)
        else:
            print("make sure to put -e or -d and put an key after")
    except EOFError:
        exit(0)