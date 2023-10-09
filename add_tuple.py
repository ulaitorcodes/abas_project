def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    
    # Ensure that each tuple has at least 2 elements
    a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    # Calculate the sum of the first and second elements of the tuples
    sum_first = a[0] + b[0]
    sum_second = a[1] + b[1]

    return (sum_first, sum_second)

# Test cases
tuple_a = (1, 89)
tuple_b = (88, 11)

# passing the both turples as arguments
new_tuple = add_tuple(tuple_a, tuple_b)

print(new_tuple)  #Expectd Output: (89, 100)

print(add_tuple(tuple_a, (1, )))  #Expected Output: (90, 89)
print(add_tuple(tuple_b, ()))  #Expected Output: (88, 11)


'''
    The above code defines the add_tuple function and provides some test cases to demonstrate its usage. 
    It correctly handles cases where the input tuples may have less than 2 elements by using a default value of 0.
'''