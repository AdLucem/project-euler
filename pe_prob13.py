#project euler problem 13

#---input---

file_list = open("file_list.txt","a+")
string = file_list.readlines()
l = []

for letter in string:    #converting into a 50x100 matrix
    sub_l = list(letter)
    l.append(sub_l)

#---main---
l_sum=[]
for loopvar in range(0,52) :
    l_sum.append(0)
    
carry = 0
for i in range(0,50) :
    s = carry
    for j in range(0,100) :
        s += int(l[j][i])
    l_sum[i] = s%10
    print "Totsum=",s,
    carry = s/10
    print "Sum(",i+1,") =",s%10," Carry=",carry

left = 50
while carry!=0 :
    l_sum[left] = carry%10
    print "Sum(",left+1,") =",carry%10
    carry /= 10
    left += 1
  

for k in range(51,41,-1) :
    print l_sum[k],
    
print


    
    

    
        
