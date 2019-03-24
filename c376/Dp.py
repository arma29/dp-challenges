'''
PEP 484 over PEP3107
'''

import math

def multiplesBetweenRange(target,x,y):
    return (math.floor(y*1.0/target) - math.ceil(x*1.0/target) + 1.0)

    
def leaps(a,b):
    print (multiplesBetweenRange(4,a,b-1) - 
    multiplesBetweenRange(100,a,b-1) + 
    (multiplesBetweenRange(900,a-200,b-200-1) + multiplesBetweenRange(900,a-600,b-600-1)))

    return (multiplesBetweenRange(4,a,b-1) - 
    multiplesBetweenRange(100,a,b-1) + 
    (multiplesBetweenRange(900,a-200,b-200-1) + multiplesBetweenRange(900,a-600,b-600-1)))
    
def main():
    # print num_between(1234,5678,900,200)
    # print num_between(1234,5678,900,600)
    # print check900Condition(1234,5678)
    # print multiplesBetweenRange(900,1234,5678)
    leaps(2016, 2017) 
    leaps(2019, 2020) 
    leaps(1900, 1901) 
    leaps(2000, 2001) 
    leaps(2800, 2801) 
    leaps(123456, 123456) 
    leaps(1234, 5678) 
    leaps(123456, 7891011)

if __name__ == "__main__":
    main()