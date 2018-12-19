    


def numberHex(number):
    fst = number/16
    snd = number%16
    if(fst > 9):
        fst = chr(ord('@')+fst-9)
    if(snd > 9):
        snd = chr(ord('@')+snd-9)
    return str(fst)+str(snd)
            
#The method join() returns a string  separated
#by the str. 
#str.join(sequence)
def hexcolor(r,g,b):
    return "#"+ "".join([numberHex(x) for x in (r,g,b)])

#as string [0][1]
def hexNumber(fstHex,sndHex):
    if(ord(fstHex) > 57):
        fstHex = (ord(fstHex) - ord('@') + 9)
    if(ord(sndHex) > 57):
        sndHex = (ord(sndHex)-ord('@') + 9)
    return (int(fstHex)*16)+(int(sndHex)%16)

def tupleHex(str):
    return hexNumber(str[1],str[2]),hexNumber(str[3],str[4]),hexNumber(str[5],str[6])

def blend(list):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for elem in list:
        fst,snd,thd = tupleHex(elem)
        sum1 += fst
        sum2 += snd
        sum3 += thd
    return hexcolor(int(sum1/len(list)),
    int(sum2/len(list)), int(sum3/len(list)))

def hex_color(lst): 
    return "#" + "".join(["0" + y if len(y) < 2 else y for y in [hex(x).replace("0x", "").upper() for x in lst]])

def main():
    print "Tests: " + '\n'
    print hexcolor(255,99,71)
    print hexcolor(184, 134, 11)
    print hexcolor(189, 183, 107)
    print hexcolor(224, 0, 205)
    print hexNumber('E','0')
    print blend({"#000000", "#778899"})
    print blend({"#E6E6FA", "#FF69B4", "#B0C4DE"})
    

if __name__ == '__main__':
    main()
