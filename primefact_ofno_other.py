#PE- prob 3
#othermethod-1
#takes 0.0012 secs

import time

a = time.clock()

num = 600851475143
factor = 2


while factor * factor < num:
    while num % factor == 0:
        num = num / factor
    factor += 1

b = time.clock()

print num
print b-a
