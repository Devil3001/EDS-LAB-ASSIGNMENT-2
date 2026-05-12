lst = [10, 25, 30, 45, 50]
key = int(input("Enter number to search: "))

found = False
lent=len(lst)
for i in range(lent):
    if lst[i] == key:
        print("Element found at position:", i + 1)
        found = True
        break

if not found:
    print("Element not found")
