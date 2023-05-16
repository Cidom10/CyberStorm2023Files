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

args = sys.argv
msg = ""
sentinel = bytearray([0, 255, 0, 0, 255, 0])

# To exit with/without a message cleanly. 
def exit():
    global msg
    sys.exit(msg)



def storage(c):
    global sentinel
    offset = c['offset']
    interval = c['interval']
    method = c['bit']

    hidden = bytearray()
    sys.stdin = open(c['hidden'])
    for k in sys.stdin.buffer.read():
        hidden.append(k)
    
    sys.stdin.close()
    
    wrapper = bytearray()
    sys.stdin = open(c['wrapper'])
    for k in sys.stdin.buffer.read():
        wrapper.append(k)
    
    # Calculate the total number of bytes needed to store the hidden message,
    # including the sentinel value and any additional padding required
    total_bytes_needed = len(hidden) + len(sentinel) + (len(hidden) % interval)
    
    # Check that the wrapper image is large enough to store the hidden message
    if len(wrapper) < total_bytes_needed:
        global msg
        msg = "Error: Wrapper image is too small to store hidden message."
        exit()

    i = 0

    if(method):
        while(i < len(hidden)):
            for j in range(8):
                byte = int(bin(wrapper[offset]), 2)
                byte &= int('11111110', 2)
                byte |= ((hidden[i] & int('10000000', 2)) >> 7)
                try:
                    hidden[i] <<= 1
                except:
                    hidden[i] = int(bin(hidden[i] << 1)[3:], 2)
                wrapper[offset] = byte
                offset += interval
            i += 1
        
        i = 0
        while(i < len(sentinel)):
            for j in range(8):
                byte = int(bin(wrapper[offset]), 2)
                byte &= int('11111110', 2)
                byte |= ((sentinel[i] & int('10000000', 2)) >> 7)
                try:
                    sentinel[i] <<= 1
                except:
                    sentinel[i] = int(bin(sentinel[i] << 1)[3:], 2)
                wrapper[offset] = byte
                offset += interval
            i += 1
    else:
        while(i < len(hidden)):
            wrapper[offset] = hidden[i]
            offset += interval
            i += 1
        
        i = 0
        while(i < len(sentinel)):
            wrapper[offset] = sentinel[i]
            offset += interval
            i += 1
    
    sys.stdout.buffer.write(bytearray(wrapper))



def extract(c):
    global sentinel
    offset = c['offset']
    interval = c['interval']
    method = c['bit']
    
    wrapper = bytearray()
    hidden = bytearray()
    
    sys.stdin = open(c['wrapper'])
    for k in sys.stdin.buffer.read():
        wrapper.append(k)
    
    wrapper = bytearray(wrapper)

    if(method):
        while(offset < len(wrapper)):  
            b = 0
            inc = offset

            for j in range(8):
                byte = int(bin(wrapper[offset]), 2)
                ander = (byte & 1)
                b |= ander
                if(j < 7):
                    b <<= 1
                    offset += interval

            if(b == sentinel[0]):
                array = bytearray()
                    
                for i in range(0, len(sentinel)):
                    b2 = 0
                    for j in range(8):
                        byte = int(bin(wrapper[inc]), 2)
                        b2 |= (byte & 1)
                        if(j < 7):
                            b2 <<= 1
                            inc += interval
                    array.append(b2)
                        
                    if(array[i] != sentinel[i]):
                        # print(array)
                        break                        
                    inc += interval
                if(array == sentinel):
                    sys.stdout.buffer.write(bytearray(hidden))
                    exit()

            hidden.append(b)
            offset += interval

    else:
        while(offset < len(wrapper)):
            b = wrapper[offset]
            # print(chr(b))
            if(b == sentinel[0]):
                array = bytearray()
                inc = offset
                for i in range(0, len(sentinel)):
                    array.append(wrapper[inc])
                    if(array[i] != sentinel[i]):
                        break
                    inc += interval
                if(array == sentinel):
                    sys.stdout.buffer.write(bytearray(hidden))
                    exit()
            hidden.append(b)
            offset += interval




def main(argc, args):
    c = {
                'store': True,
                'bit': True,
                'offset': 0,
                'interval': 1,
                'wrapper': "",
                'hidden': ""
                }
    

    for dash in args[1:]:
        match(dash[0:2]):
            case "-s":
                pass
            case "-r":
                c['store'] = False
            case "-b":
                pass
            case "-B":
                c['bit'] = False
            case "-o":
                c['offset'] = int(dash[2:])
            case "-i":
                c['interval'] = int(dash[2:])
            case "-w":
                c['wrapper'] = dash[2:]
            case "-h":
                c['hidden'] = dash[2:]
            case _:
                global msg
                msg = "Invalid option: " + dash[0:2]
                exit()

    if(c['store']):
        storage(c)
    else:
        extract(c)

    # print(type(c['interval']))

    # print(f'Store: {c['store']} \nBit: {c['bit']}\nOffset: {c['offset']}\nInterval: {c['interval']}\nWrapper: {c['wrapper']}\nHidden: {c['hidden']}')




# print(sentinel)
main(len(args), args)