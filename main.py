# import pandas
table = [1, 2, 3]

for i in table:
    i += 1

try:
    val = int("not-an-integer")
except ValueError:
    print("Caught an exception")

x = 1 + 2
