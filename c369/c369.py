    


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

def hex_color(lst): 
    return "#" + "".join(["0" + y if len(y) < 2 else y for y in [hex(x).replace("0x", "").upper() for x in lst]])

#as string [0][1]
def hexNumber(fstHex,sndHex):
    if(ord(fstHex) > 57):
        fstHex = (ord(fstHex) - ord('@') + 9)
    if(ord(sndHex) > 57):
        sndHex = (ord(sndHex)-ord('@') + 9)
    return (int(fstHex)*16)+(int(sndHex)%16)

def tupleHex(str):
    return hexNumber(str[1],str[2]),hexNumber(str[3],str[4]),hexNumber(str[5],str[6])


'''
Learning of today:
entry: a = [(2,3),(4,5)]
result = (6,8)

possile:
reduce(lambda x,y: (x[0]+y[0],x[1]+y[1],z[2]+z[2]), a)

[sum(x) for x in zip(*a)] //compression
zip(a) = [((2, 3),), ((4, 5),)]
zip(*a) = [(2,4),(3,5)] -> operator * unzip de list 
'''
def blend(list):
    temp = [tupleHex(x) for x in list]
    fst,snd,thd = [int(round(sum(x)/len(list),0)) for x in zip(*temp)]
    return hexcolor(fst,snd,thd)



def main():
    print "Tests: " + '\n'
    # print hexcolor(255,99,71)
    # print hexcolor(184, 134, 11)
    # print hexcolor(189, 183, 107)
    # print hexcolor(224, 0, 205)
    print blend({"#000000", "#778899"})
    # print blend2({"#000000", "#778899"})
    # print blend({"#E6E6FA", "#FF69B4", "#B0C4DE"})
    #TODO: Differences between python2 round and python3 round. its the key.
    print tupleHex("#000000"), tupleHex("#778899")
    print " Aim", tupleHex("#3B444C")
    print "Goal", tupleHex("#3C444C")

   

if __name__ == '__main__':
    main()
