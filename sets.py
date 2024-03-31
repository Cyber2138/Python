set1 = {1,2,3,4,5,6}
set2 = {2,3,4,5,8}
print(set1, set2)
print('This is the union of two sets: ',set1.union(set2),'\n')
print('This is the intersection of two sets: ',set1.intersection(set2),'\n')
print('This is the difference of two sets: ',set1.difference(set2),'\n')
print('This is the symmetric difference of two sets: ',set1.symmetric_difference(set2),'\n')
print('This shows whether the two sets are disjoint : ',set1.isdisjoint(set2),'\n')
print('This shows whether the first set is the superset of the second set: ',set2.issubset(set1),'\n')
set2.add(1)
print(set2)
print(set1.pop())
print(set1)