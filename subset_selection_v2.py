"""
Subset Selection Problem
Problem Statement:
Find all the subsets from a set of numbers whose sum is zero.

Constraint: Subset size must be 5
Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

"""

#this code is with sorting



# Step 1: Library inclusion                             
import random as r

# Step 2: Parameter Setting
Set         = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
SetSize     = 5
ResultList  = set()    # Store Result List i.e. list of sets whose sum is zero
Iterations  = 1000   # Number of Inerations


# Step3: Start Program

# Loop till number of Iterations
for i in range(Iterations):
    # Select number of elements from Set
    Chromosome = r.sample(Set,SetSize)
    Chromosome.sort()

    # Sum the number of elements in the Chromosome
    if sum(Chromosome) == 0:
        ResultList.add(tuple(Chromosome))

# Print all the sets whose sum is zero
for r in ResultList:
	print (r)

# Print total sets
print ("\nTotal Sets: ", len(ResultList))