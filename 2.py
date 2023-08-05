'''
given array of integers where every element appears even number of times except one element which appear ood number of times
,write a program to find that odd occuring element .The equal elements must appear in pairs int the array but there cannot
be more than two consecutive occurence of an element 
'''

def find(list_value):
    presentornot=True
    unique_numbers=[]
    for i in list_value:
        numberoftimes_repeated=list_value.count(i)
        if numberoftimes_repeated%2!=0 and i not in unique_numbers:
            print("Number which is repeted odd times",i)
            unique_numbers.append(i)
            presentornot=False
        
    if(presentornot):
        print("No numbers repeated odd times")
    flag=True        
    n=0
    
    while n<len(list_value):
        index=(list_value.index(list_value[i]))
        indextwo=index+2
       
        if index!=len(list_value)-1 and indextwo!=len(list_value)-1 :
                 indexone=index+1 
                 if list_value[index]==list_value[indexone] and list_value[indexone]==list_value[indextwo]:
                       print("List is not eligible")
                       flag=False
                       break
            
               
        n+=1
        
            
            
            
        
            
    if (flag):
        print("List is eligible for second condition")
        
            
    
    

n=int(input("Enter no of numbers:"))
numbers=[]
while n>0:
    value=int((input("Enter the number:")))
    numbers.append(value)
    n-=1
    
find(numbers)    
    
    
    
    

'''
ack and Jill are playing a string game. Jack has given Jill two strings A and B. Jill has to derive a string C from A, by deleting elements from string A, such that string C does not contain any element of string B. Jill needs help to do this task. She wants a program to do this as she is lazy. Given strings A and B as input, give string C as Output.

Example 1:

Input:
tiger     -> input string A
ti          -> input string B
Output:
ger       -> Output string C
Explanation:
After removing “t” and “i” from “tiger”, we are left with “ger”.
So, the answer is “ger”.
Example 2:

Input:
processed     -> input string A
esd                -> input string B
Output:
proc               -> Output string C
Explanation:
After removing “e” “s” and “d” from “processed”, we are left with “proc”.
So, the answer is “proc”.
Example 3:

Input:
talent        -> input string A
tens          -> input string B
Output:
al              -> Output string C

code:
a='tiger'
b='ti'
c=''

for i in b:
    for j  in a:
        if j!=i and i not in c:
            c+=j
            
            
            
print(c)            
            
'''