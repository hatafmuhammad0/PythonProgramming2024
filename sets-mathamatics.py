set1 = {1,2,3,4,5}
set2 = {2,3,6,7,8}

# Union means combine
set3 = set1.union(set2)
# print(set3)

# Intersection means return a set with comman values in both sets
set4 = set1.intersection(set2)
# print(set4)

print(set1-set2) #! output : {1, 4, 5} Explain : It will return a set of values which is present in set 1 but not in set 2
print(set2-set1) #! output : {8, 6, 7} Explain : viseversa of above statement 



