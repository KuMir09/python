a=[5,6,"ab"]
print(dir(a))
print(a.__dir__.__doc__)


file = open("demo.txt") # OPEN
print(dir(file))
print(file.write.__doc__)