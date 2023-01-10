import dcV3

filename = input("Please enter the location for requirement.txt: ")

for item in dcV3.comparisonPackage(filename):
    print(item)