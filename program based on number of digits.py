
import math


n = int(input("Enter a number: "))
digits = len(str(abs(n)))

if digits == 1:
    print("Square:", n ** 2)
elif digits == 2:
    print("Square Root:", math.sqrt(n))
elif digits == 3:
    print("Cube Root:", n ** (1/3))
else:
    print("Number has more than three digits")
