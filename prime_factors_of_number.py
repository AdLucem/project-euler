
#K.W
#project euler - problem 3

"""To compute the prime factors of a number"""

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
while True:
    
    #to find smallest prime factor of no
    i = 2
    while i < n**0.5 :  #?? smallest prime factor <= sqrt of no? check
        if n%i == 0 and prime_check(i)==1 :
            p_lpf = n/i  #p_lpf --> potential largest prime factor
            break
        else:
            i+=1

    if prime_check(p_lpf) == 1 :  #to check if p_lpf is prime
        lpf = p_lpf
        break
    else:
        n = p_lpf  #to find prime factors of p_lpf
        
b = time.clock()
print "Largest prime factor = ",lpf
print b-a



    
    









