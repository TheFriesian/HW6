#Create a list of numbers. Remove duplicate values. Print unique values.
import random

numbers = [random.randint(1,10) for _ in range(10)]
print (numbers)


unique_numbers = set(numbers)
print("Make the string unique: ",unique_numbers)


unique_at_generation = [num for num in numbers if numbers.count(num) == 1]
print ("HAve been unique fom the beginning: ",unique_at_generation)

#Given two lists of numbers, count how many numbers are present in both lists.

list1= [random.randint(1,10) for _ in range(10)]
print (numbers)

list2= [random.randint(1,10) for _ in range(10)]
print (numbers)

common_numbers = len(set(list1) & set(list2))
print(common_numbers)

#task3
text = """
3
Hello world
Hello Python
Python is amazing
"""
lines = text.strip().split("\n")[0:]
#print (lines)
words = set()
for line in lines:
    words.update(line.split())
print(len(words))

##########3
countries = {
    "Ukraine": ["Kyiv", "Lviv", "Dnipro"],
    "USA": ["Los Angeles", "Las Vegas"]
}

city_country = {}
for country, cities in countries.items():
    for city in cities:
        city_country[city] = country
print(city_country)

############4
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)
