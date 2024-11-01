# Function to find seocnd largest in a list
def second_largest_in_list(num_list):
    list_size = len(num_list)
    
    # Bubble sorting algorithm
    for i in range(len(num_list)):
        for j in range(len(num_list) - i - 1):
            
            if(num_list[j] > num_list[j+1]):
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    
    
    # Find the second largest
    max_num = num_list[0]
    for i in range(list_size):
        if(max_num != num_list[i]):
            second_max = num_list[i]
            break
        
    return second_max


input_as_string = input("Enter elements of the list separated by space: ")  
  
# Converting input string to a list of integers  
num_list = input_as_string.split()
# Using list comprehension to create the list
num_list = [int(num) for num in num_list]  
  

print(f"The second largest number in the list {num_list} is ", end="")
print(second_largest_in_list(num_list))