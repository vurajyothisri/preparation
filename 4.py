'''
write a program that recieves a word A  and some text as input .you need to output the texts(without modifying them) in the ascending order of the number of occurences of Word A in the texts.The input is as follwes an integer m(BEtween 1 to 100,inclusive),follews by the worf A in the next line ,some texr in each of the m next line

note:the texts and word A containonly lower case latin letters(a,b,c,...z)  and blank spaces.The maximum size of the texts and the word A is 100 characters .every text has a different number of occurence of the word A
n
ote: you must print one text line without modifying the texts

'''

list_container=[]
m=int(input("Enter the no of lines "))

print("Enter the lines:")

for i in range(m):
    text=input(f'Enter the {i+1} line:')
    list_container.append(text)

dictionary_container={}

for i in list_container:
    if 'a' in i and len(i)<100:
        dictionary_container[i.count('a')]=i 
        
        
#items() function create list withe tuple values nad tupels contain key and value 
#when i use items to dictionary_container it will like this[(key,value),(key,values)]
#list can be sorted so i use th e sorted fmethod after that i convert into dic after tha i display values
sorted_dictinary=dict(sorted(dictionary_container.items()))
print("sorted llist:",sorted_dictinary)

for i in sorted_dictinary:
    print(sorted_dictinary[i])
