# dictionary used to store data values in key:value pairs
# they are unorders, mutable(changeable) & don't allow duplicates

names = ["Maria", "Gendalf", "Batman"]
profs = ["programmer", "wizard", "superhero"]

my_dict = {}
for i in range(len(names)):
    my_dict[names[i]] = profs[i]
print(my_dict)

for key, value in zip(names,profs):
    my_dict[key] = value
print(my_dict)