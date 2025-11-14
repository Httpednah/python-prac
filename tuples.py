# 1. Replace the last value of tuples in a list

data1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result1 = [t[:-1] + (100,) for t in data1]
print("1:", result1)

# 2. Remove empty tuples from a list of tuples

data2 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
result2 = [t for t in data2 if t]
print("2:", result2)

# 3. Sort a tuple by its float element (descending)

data3 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
result3 = sorted(data3, key=lambda x: float(x[1]), reverse=True)
print("3:", result3)

# 4. Convert tuple of integers into an integer

t1 = (1, 2, 3)
result4a = int("".join(str(x) for x in t1))
print("4a:", result4a)

t2 = (10, 20, 40, 5, 70)
result4b = int("".join(str(x) for x in t2))
print("4b:", result4b)

# 5. Sum of all elements in each tuple

data5a = [(1, 2), (2, 3), (3, 4)]
result5a = [sum(t) for t in data5a]
print("5a:", result5a)

data5b = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
result5b = [sum(t) for t in data5b]
print("5b:", result5b)

# 6. Average value of numbers in a tuple of tuples

data6a = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)
result6a = [sum(t) / len(t) for t in data6a]
print("6a:", result6a)

data6b = (
    (1, 1, -5),
    (30, -15, 56),
    (81, -60, -39),
    (-10, 2, 3)
)
result6b = [sum(t) / len(t) for t in data6b]
print("6b:", result6b)

