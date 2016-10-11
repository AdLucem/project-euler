#K.W
#project euler - problem 3

"""To compute the largest prime factor of a number by brute force"""

import math
import time
#---functions---

def prime_check(n) :

    i = 2
    flag = 1
    while i<math.sqrt(n) :
        if n%i==0 :
            flag = 0  #if num is div, num is non-prime. break
            break
        else:
            i+=1
        #if num is never div, num is prime. flag will be 1
    return flag


#---main---

n = long(raw_input("Enter number"))    #input number

a = time.clock()
pot_fact = n-1
while pot_fact>0 :

    if n%pot_fact == 0 and prime_check(pot_fact) == 1 :
        lpf = pot_fact
        break
    else:
        pot_fact -= 1
                   
b = time.clock()
print "Largest prime factor = ",lpf
print b-a
