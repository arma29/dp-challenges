'''
PEP 484 over PEP3107
'''

def leaps(a,b):
    boolean = False
    if(b < a or b-a == 0):
        return 0
    if(a%4 == 0):
        boolean = True
    if(a%100 == 0):
        boolean = False
    if( (a%900) == (200 or 600) ):
        boolean = True
    #Like a ternary conditional operator
    return (1 if boolean else 0)

def main():
    print 

if __name__ == "__main__":
    main()