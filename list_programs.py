'''Sum of List Elements:
Write a Python program to calculate the sum of all numeric items
in a given list.

list1 = [1,2,3,4,5,6,7,8,9,10]
sums=0
for i in list1:
    sums = sums+i
    

print(sums)
'''
#Maximum element in list
'''
list1 = [1,2,33,4,55,6,7,88,9,10]
maximum = 0

for i in list1:
    print(i)
    if i>maximum:
        maximum=i
    
print("Max:",maximum)

#Ways to find length of list
list1 = [1,2,33,4,55,6,7,1,2,88,9,10]
length = 0

for i in list1:
    length+=1
print("Length",length)


#To interchange first and last elements in a list

# Original list of numbers
list1 = [1, 2, 33, 4, 55, 6, 7, 1, 2, 88, 9, 10]
# Temporary list to hold the last element of list1
middle = [0]

# Store the last element of list1 in middle[0]
middle[0] = list1[-1] 
print("middle", middle)  # Output the last element of list1

# Change the last element of list1 to the first element
list1[-1] = list1[0] 
print("last", list1[-1])  # Output the new last element of list1

# Change the first element of list1 to the original last element (stored in middle[0])
list1[0] = middle[0] 
print("first", list1[0])  # Output the new first element of list1

# Print the final modified list
print(list1)
'''
'''
#To swap two elements in a list
#given list
list1 = [1, 2, 33, 4, 55, 6, 7, 1, 2, 88, 9, 10]

#swap 2 with 55 using index

index2=list1.index(2)
index55=list1.index(55)

list1[index2],list1[index55] = list1[index55],list1[index2]
print(list1)
'''
'''
#without using index method
list1 = [1, 2, 33, 4, 55, 6, 7, 1, 22, 88, 9, 10]
index22=0
index55=0

for i in list1:
    if i==22:
        break
    index22+=1
    
for i in list1:
    if i==55:
        break
    index55+=1

print("Before",list1)
list1[index22],list1[index55] = list1[index55],list1[index22]
print("After",list1)
'''

'''to check if element exists in list

list1 = [1, 2, 33, 4, 55, 6, 7, 1, 22, 88,55, 9,55, 10] #find 55
appears = 0

for i in list1:
    if i==55:
        appears=appears+1
    
print(f"55 found {appears} times")'''


    
        

