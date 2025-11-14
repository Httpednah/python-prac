# 1. Find the length of a set
my_set = {1, 2, 3, 4, 5}
print("1 Length of the set:", len(my_set))


# 2. Add member(s) to a set
my_set = {1, 2, 3}
# Add a single element
my_set.add(4)
# Add multiple elements
my_set.update([5, 6, 7])

print("2 Updated set after adding elements:", my_set)


# 3. Remove item(s) from a given set
my_set = {1, 2, 3, 4, 5}
# Remove an item (error if not found)
my_set.remove(3)
# Discard an item (no error if not found)
my_set.discard(10)

print("3 Set after removal:", my_set)


# 4. Create an intersection of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
print("4 Intersection of sets:", intersection)


# 5. Create a union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print("5 Union of sets:", union_set)


# 6. Create a set difference
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}

difference = set1.difference(set2)
print("6 Difference (set1 - set2):", difference)


# 7. Find the maximum and minimum values in a set
my_set = {10, 25, 3, 48, 7}

print("7 Maximum value in the set:", max(my_set))
print("7 Minimum value in the set:", min(my_set))