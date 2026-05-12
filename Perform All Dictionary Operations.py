# Creating dictionary
student = {
    "roll": 101,
    "name": "Amit",
    "marks": 85
}

# Add element
student["grade"] = "A"

# Update value
student["marks"] = 90

# Access value
print("Name:", student["name"])

# Remove element
student.pop("roll")

# Keys and Values
print("Keys:", student.keys())
print("Values:", student.values())

print("Final Dictionary:", student)
