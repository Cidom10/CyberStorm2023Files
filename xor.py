# Group: PSITTACOSAURUS
# Members:
#   Ben Meister
#   Samman Regmi
#   Trisha Carter
#   Calvin Idom
#   Cameron McCarthey
#   Nabinta Niraula
#   Reese Seals

import sys
import os

SWITCH = False       # True for key, False for key2
key = []
new = []
cipher = []
key = []

path = os.getcwd()

if(SWITCH):
    key_loc = path + "/key.bmp"
else:
    key_loc = path + "/key.bmp"


for line in sys.stdin.buffer.read():
    cipher.append(line)
    
sys.stdin = open(key_loc)

for line in sys.stdin.buffer.read():
    key.append(line)
    

cipher = bytearray(cipher)
key = bytearray(key)


for i in range(0, len(cipher)):
    new.append(cipher[i] ^ key[i % len(key)])

sys.stdout.buffer.write(bytearray(new))