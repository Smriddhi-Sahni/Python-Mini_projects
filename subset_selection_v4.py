"""
Subset Selection Problem
Problem Statement:
Find all the subsets from a set of numbers whose sum is zero.

Constraint: Subset size must be 5
Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

"""
#this is another shorter approach of the same problem
#it uses string instead of sets



import random as r
str=[-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
print("the subsets with sum 0 are:")
c=0
for k in range (0,1000):
    a= r.sample(str, 5)
    a.sort()
    if (sum(a)==0):
      c=c+1
      print(a)
print("total number of subsets that sum to 0 in 1000 samples",c)