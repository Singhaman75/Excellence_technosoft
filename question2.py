'''Setup a dict structure like this in python
Dict1: (this is a key, value pair of user id and username)
{
   “1” : “name1”,
   “2” : “name2”,
   “3” : “name3”
}  '''

num_of_users=int(input("enter no. of users"))
dict1,dict2,count={},{},1
for i in range(0,num_of_users):
    name=input("enter user name")
    score=int(input("enter exam score"))
    dict1.update({count:name})
    dict2.update({count:score})
    count=count+1
list1,count=[],1
for i in range(0,num_of_users):
    list1.append(dict2.get(count))
    count=count+1
value1=max(list1)
key1=list(dict2.keys())[list(dict2.values()).index(value1)]
print(f"{key1}:{value1}")
