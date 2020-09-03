# del and assert

a = [1, 2, 3]
print("list before deleting ")
print(a)
del a[1]
print(a)

# demonstrating use of assert
# prints AssertionError
assert 5 < 3, "5 is not smaller than 3"