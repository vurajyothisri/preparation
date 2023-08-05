'''
Given two non-negative integers n1 and n2, where n1

For example:

Suppose n1=11 and n2=15.

There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

Example1:

Input:

11 — Vlaue of n1
15 — value of n2
Output:

4
Example 2:

Input:

101 — value of n1
200 — value of n2
Output:

72

'''
#code:
value1=101
value2=200
count=0
valll=[]
for i in range(value1,value2+1):
    j=str(i)
    print(j)
    for k in range(len(j)):
        for l in range(k+1,len(j)):
            if j[k]!=j[l]:
                valll.append(True)
            else:
                valll.append(False)
                
    print(valll)
    hii=all(valll)
    print("Hii:",hii)
    if(hii):
        count+=1
        print("Count increament:",count)
    valll.clear()    
        
print("Count: ",count)        
        
    
    
        
        
        
       

