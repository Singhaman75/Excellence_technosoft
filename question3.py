'''Assume we have list like this
[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
Basically a list of zero’s and one’s.
Write a python function to the number of maximum consecutive  one’s present in the array. 
E.g output for the above array would be 4
'''


input_list=[0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0]
maxx=0
count=0
for i in range(len(input_list)):
    if input_list[i]==1:
        for j in range(i,len(input_list)):
            if (input_list[j]!=0):
                count=count+1
                if count>maxx:
                    maxx=count
            else:
                    count=0

print(maxx)  

