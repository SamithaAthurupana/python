# A dictionary in Python works with key-value pairs.
# Example: key : value

student = {
    "name" : "Test",              # String value
    "age" : 20,                   # Integer value
    "married" : False,            # Boolean value
    "grades": 22,                 # Integer value
    "contact": ["242234424","242234424","242234424"]  # List value inside dictionary
}

# Adding a new phone number to the 'contact' list
student["contact"].append("2498631239")

# Loop through each number in the 'contact' list and print it
for num in student["contact"]:
    print(num)

# Accessing a dictionary value using the key
print(student["name"])

# Updating a value in the dictionary
student["name"] = "kalana"
print(student["name"])

# Check if a key exists in the dictionary before using it
if "grades" in student:
    print(student["grades"])

# Loop through only the values in the dictionary
for vaal in student.values():
    print(vaal)

# Loop through only the keys in the dictionary
for keys in student.keys():
    print(keys)

# Loop through both keys and values in the dictionary
for key, val in student.items():
    print(f"key: {key} - value: {val}")
