s1 = set()
print(type(s1))
s2 = set()
intersec_set =set()
union_set = set()
diff_set =set()
limit=1
while True:

    if limit == 0:
        break
   
    else:
        
        user_input= int(input("Enter set 1 elments"))
        
        s1.add(user_input)
        
        user_input2 = int(input("Enter set 2 elments"))
        s2.add(user_input2)
    limit = int(input("enter 0 to exit limit"))
    
    print(s1)
    print(s2)


intersec_set = s1.intersection(s2)
print("Intersection:",intersec_set)
union_set = s1.union(s2)
print("Union:",union_set)
