#K.W
#project euler- problem 4- it worked

"""to find the largest palindrome product of 3-digit numbers"""

import math


#---functions---

def palindr() :    #to generate 6-digit palindromes
    x = 9
    y = 9
    z = 9
    while x >= 1 :
        y = 9
        z = 9
        while y >= 0 :
            z = 9
            while z >= 0 :
                yield x*pow(10,5) + y*pow(10,4) + z*pow(10,3) + z*pow(10,2) + y*pow(10,1) + x
                z -= 1
            y -= 1
        x -= 1

def factor(n) :
    
    i=100.0
    flag = 0
    
    while i <= math.sqrt(n) and i>=100 :
        
        if n%i == 0 and len(str(int(n/i)))==3:
            flag = 1
            j = n/i
            ret_val = n,"=",i,"x",j
            break
        else:
            i+=1

    if flag == 0:
        return "no three digit factors"
    elif flag == 1:
        return ret_val


#---main---

done = 0
c = palindr()

while not done:
    n = next(c)
    f = factor(n)

    if f != "no three digit factors" :
        print f
        done = 1
    elif f == "no three digit factors" :
        done = 0

    

    





        





        

