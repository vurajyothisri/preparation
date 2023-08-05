'''

sum of dignal elements in a matrix
'''

matrix=[]
sum=0
print("Enter the 10 number for each line with space")
for i in range(10):
    values=input(f'Enter the {i+1} line:')
    #spilting the input
    input_list=values.split(" ")
    print(input_list)
    # legth of the input to find user enter only 10 values
    if len(input_list)==10:
        sub_list=[int(j) for j in input_list]
        print(sub_list)  
        matrix.append(sub_list)
    else:
        print("Insufiicient numbers")
        break
        
    
    
#sum of the diagnol element
for k in range(len(matrix)) :
    for l in range(len(matrix)):
        if k==l:
            sum=sum+matrix[k][l]
            
print("sum:",sum)            