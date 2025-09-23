# dictionary = key : value

student = {
    "name" : "Test",
    "age" : 20,
    "married" : False,
    "grades": 22,
    "contact": ["242234424","242234424","242234424"]
}

student["contact"].append("2498631239")

for num in student["contact"]:
    print(num)

print(student["name"])
student["name"] = "kalana"
print(student["name"])

if "grades" in student:
    print(student["grades"])

for vaal in student.values():
    print(vaal)

for keys in student.keys():
    print(keys)

for key,val in student.items():
    print(f"key - {key} and value - {val}")