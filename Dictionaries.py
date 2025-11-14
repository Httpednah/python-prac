# 1. Concatenate the following dictionaries to create a new one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Using dictionary unpacking
dic4 = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:")
print(dic4)
print()

# 2️ Print all distinct values in a list of dictionaries
data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

unique_values = set(val for dic in data for val in dic.values())
print("Unique Values:", unique_values)
print()

# 3️ Combine two dictionaries by adding values for common keys
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined = Counter(d1) + Counter(d2)
print("Combined Dictionary with Added Values:")
print(combined)
print()

# 4️ Get the top three items in a shop
shop_items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# Sort by value descending and get top 3
top_three = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top Three Items:")
for item, price in top_three:
    print(item, price)
print()

# 5️ Filter dictionary based on values (marks > 170)
students = {'Cierra Vega': 175, 'Alden Cantrell': 180,
            'Kierra Gentry': 165, 'Pierre Cox': 190}

filtered = {name: marks for name, marks in students.items() if marks > 170}
print("Marks greater than 170:")
print(filtered)
print()

# 6️  Extract list of values from list of dictionaries for a given subject
records = [{'Math': 90, 'Science': 92},
           {'Math': 89, 'Science': 94},
           {'Math': 92, 'Science': 88}]

science_scores = [d['Science'] for d in records]
math_scores = [d['Math'] for d in records]

print("Science scores:", science_scores)
print("Math scores:", math_scores)