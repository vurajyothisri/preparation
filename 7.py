def sum_differece(number_list):
    odd_sum=0
    even_sum=0
    for i in range(len(number_list)):
        if i%2==0:
            even_sum+=number_list[i]
        else:
            odd_sum+=number_list[i]
    print(odd_sum)
    print(even_sum)        
    print(abs(odd_sum-even_sum))            

       
    
   



sum_differece([10,20,30,40,50,60,70])
