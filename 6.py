def difference(numbers_list,index_value):
    if index_value==0:
        result=numbers_list[0]-numbers_list[1]
        return abs(result)
    elif index_value==len(numbers_list)-1:
        result=numbers_list[index_value-1]-numbers_list[index_value]
        return abs(result)
    else:
        val1=abs(numbers_list[index_value-1]-numbers_list[index_value])
        val2=abs(numbers_list[index_value+1]-numbers_list[index_value])
        result=val1+val2
        return abs(result)




n=int(input("enter the number of integers:"))
numbers=input("Enter the values: ") 
input_value=numbers.split(" ")

integer_list=[int(j) for j in input_value]
m=int(input("enter the index values: "))

print("value= ",difference(integer_list,m))