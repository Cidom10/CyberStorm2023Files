#######################################################################################################################
# Group Members: Reese Seals, Trisha Carter, Calvin Idom, Samman Regmi, Michael Herbert, Ben Meister, Cameron McCarthy
#######################################################################################################################

# imports
import sys

# variable initailization
count = 0
string = ""
binary = ""
support = ""
stuff=""

# 7-Bit
for line in sys.stdin:
    print(f'Binary Input: {line}\n')
    print("7-Bit:")
    binary += line.replace("\n", "").replace(" ", "")
    if (len(binary) % 7 == 0):
        stuff=binary
    else:
        padding = len(binary)%7
        while(padding>0):
            support+="0"
            padding-=1
        stuff= support + binary
    for t in stuff:
        if (count == 7):
            try:
                if (int(string,2)> 0 and int(string,2)<127):
                    print(chr(int(string, 2)), end="")
                string=f"{t}"
                count=0
            except:
                pass
        else:
            string+=t
        count+=1
    try:
        if (int(string,2)> 0 and int(string,2)<127):
            print(chr(int(string,2)), end="")
    except:
        pass

# 8-Bit
print("\n\n8-Bit:")
string=""
count=0
if (len(binary) % 8 == 0):
        binary=binary
else:
    padding = len(binary)%8
    while(padding>0):
        support+="0"
        padding-=1
    binary= support + binary
for t in binary:
    if (count == 8):
        try:
            if (int(string,2)> 0 and int(string,2)<127):
                print(chr(int(string, 2)), end="")
            string=f"{t}"
            count=0
        except:
            pass
    else:
        string+=t
    count+=1
try:
    if (int(string,2)> 0 and int(string,2)<127):
        print(chr(int(string,2)), end="")
except:
    pass
print("\n")
