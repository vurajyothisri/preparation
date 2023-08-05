def find_indexs(lis,string):
    
    flag=True
    for i in range(len(lis)-1):
        
        if lis[i]==string:
            print("The Entered String is at position in the list is:",i+1)
            flag=False
    if (flag):
        print("string not found")        




List_values=["heloo","kavya","pooja","hi123","123"] 
string_value=input("Enter the string To find the Index:")   
find_indexs(List_values,string_value)