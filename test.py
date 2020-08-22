# evaluate a boolean expression
eval('5 in [1, 2, 3]')
# False

eval('4 < 9')
# True

# evaluate a mathematical expression
eval('5 + 3')
# 8

eval('7 // 2')
# 3

# define a function - multiply_by_two 
def multiply_by_two(x):
    return 2 * x

# call the function with eval
eval('multiply_by_two(8)')
# 16


# list of products
products = ['chair', 'table', 'closet', 'lamp']

# create an enumerate object
enumerate_object = enumerate(products)

# obtain the next tuple from the enumerate object
it = next(enumerate_object)
print(type(it))

# (0, 'chair')
next(enumerate_object)
# (1, 'table')
next(enumerate_object)
# (2, 'closet')
next(enumerate_object)
# (3, 'lamp')


# list of products
products = ['chair', 'table', 'closet', 'lamp']

# list of tuples
# x = print(list(enumerate(products)))
print (list(enumerate(products))[0])
