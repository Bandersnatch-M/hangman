# Chapter 5. Practice challenge 6. "Set and frozenset"
# There a three main ways to creat a set:

# 1. Using {} notation, for example:
print("Examples of using sets by {} notation:")

# Examples:
number = {1,2,3}
print (number)
fruits = {"apple", "Banana"}
print (fruits)
letters = {'a', 'n', 'c'}
print(letters)
"""!!!You can not use {} notation to creat empty "set"!!!"""

# 2. Calling "set" on iterable
"""You can call the built-in function set on any iterable to create a set out of the elements of that iterable.
Notable examples include ranges, strings, and lists."""
print("   ")
print("Examples of calling set on iterable:")

# Examples:
num = set(range(3))
print(num)
var = set([100, "degrees", "!"])
print(var)
f = {44, 'year', '%'}
print(f)

"""Notice that calling set on a string produces a set with the characters of the string,
not a set containing the whole string."""
print("   ")
print("Examples of calling set a string:")

# Examples:
mis = {"mississipi"}
print(mis)
miss = set("mississipi")
print(miss)

# 3. Comparison "set" and "list"
print("   ")
print("Examples of calling an empty set and 'add' function:")

a = set()
print(a)
a.add(10)
a.add(20)
a.add(10)
print(a)
# If you add to "set" the same element it won't be added there, becouse it is the feature of the "set":
# The set can not has two same elements. 

# Comparison with "list"
print("   ")
print("Comparison 'set' to 'list' function")
b = list()
b.append(10)
b.append(20)
b.append(10)
print(a)
print(b)
