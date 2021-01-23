# Use python lists and make an list of numbers.
# Write a function which returns sum of the list of numbers

def add(list1):
    sum,len_list1=0,len(list1)
    for i in range (0,len_list1):
        sum=sum+list1[i]
    return sum

list_values=[int(i) for i in input().split(' ')]
print(add(list_values))
