# Given a list of integers and a number k, find the kth largest integer in the list. The integer will be stored in the kth_max variable.

# For example, with a list of 7 integers, if k = 2, then kth_max will be equal to the second-largest integer in the list. If k = 6, 
# kth_max will equal the 6th largest integer.

# My solution

i = 1
for x in test_list:
    if i == k:
        kth_max = max(test_list)
        break
    else:
        test_list.remove(max(test_list))
        i += 1
        
# Educative solution (way better and doesn't alter the list)

test_list.sort()
kth_max = test_list[-k]
