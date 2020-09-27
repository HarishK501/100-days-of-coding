# you are given an unsorted array containing 0s, 1s and 2s.
# sort the array in minimum time without using extra space

sample_array = [0,0,2,1,2,2,0,1,2,0,0,1,1,2,2]
# output should be => sample_array = [0,0,0,0,0,1,1,1,1,2,2,2,2,2,2]

# Here, we will pass through the array twice
# On the first pass, we will have a pointer to the place where we can place 0. When we encounter a 0 anywhere later in the list, we will replace values and move the pointer to one position next.
# So at the end of first pass, we will have placed all zeros in their position
# At the second pass, we will start the iteration from the position of the pointer and then continue the same process. So all 1's will be sorted and thus 2's will be sedimented at the end of the list

# Complexity < O(2n) Since we have two iterations and in the second iteration, we are starting in the middle(not from the start again)
print("\nOriginal array: ",sample_array)
start_value = my_pointer = 0
my_iterator = 0

while(my_iterator < 2):  # this loop runs two times
    for i in range(my_pointer, len(sample_array)):  
        if sample_array[i] == start_value:
            temp = sample_array[my_pointer]
            sample_array[my_pointer] = sample_array[i]
            sample_array[i] = temp
            del(temp)
            my_pointer += 1
        elif start_value < sample_array[i]:
            if not sample_array[my_pointer] != start_value: 
                my_pointer = i
    my_iterator += 1
    start_value += 1

print("\nSorted array: ",sample_array)
