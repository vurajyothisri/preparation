def reverse_string_with_numbers(input_string):
    letters = []
    numbers = []
    
    for char in input_string:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(char)
    
    reversed_string = ''
    num_index = 0
    
    for char in input_string:
        if char.isalpha():
            reversed_string += letters.pop()
            print("reversee:",reversed_string)
        elif char.isdigit():
            reversed_string += numbers[num_index]
            print("numberss:",reversed_string)
            num_index += 1
    
    return reversed_string

input_string = "a1b2f3"
output_string = reverse_string_with_numbers(input_string)
print("Input:", input_string)
print("Output:", output_string)
