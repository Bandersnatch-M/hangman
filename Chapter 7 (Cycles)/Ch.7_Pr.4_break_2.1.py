# Chapter 7. Cycles
# Practice 4. "break" instruction. Ex.2.1

lst = []
qs = "Enter a number: "
while True:
    print("Enter Q for escape ")
    a = input(qs)
    lst.append(a)
    if a == "Q":
        break
print(lst)
