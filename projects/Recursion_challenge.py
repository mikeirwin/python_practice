from Recursion_practice import build_bst



# Iterative function
def factorial(n):
    if n < 0:
        ValueError("Inputs 0 or greater only")
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result


# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)

# Iterative function
def fibonacci(n):
    if n < 0:
        ValueError("Input 0 or greater only!")

    fibs = [0, 1]

    if n <= len(fibs) - 1:
        return fibs[n]

    while n > len(fibs) - 1:
        fibs.append(fibs[-1] + fibs[-2])

    return fibs[-1]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)

# Recursive Function of similar execution
def fibonacci2(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)

fibonacci2(3)
# 2
fibonacci2(7)
# 13
fibonacci2(0)
# 0

"""
This function, sum_digits(), produces the 
sum of all the digits in a positive number 
as if they were each a single number
"""

# Linear - O(N)
def sum_digits(n):
    if n < 0:
        ValueError("Inputs 0 or greater only!")
    result = 0
    while n is not 0:
        result += n % 10
        n = n // 10
    return result + n


sum_digits(12)
# 1 + 2
# 3
sum_digits(552)
# 5 + 5 + 2
# 12
sum_digits(123456789)
# 1 + 2 + 3 + 4...
# 45
""" 
Recursive Version of similar functionality
<(^_^<) <(^_^)> (>^_^)> 
"""


def sum_digits(n):
    if n <= 9:
        return n
    while n > 9:
        last_digit = n % 10
        return sum_digits(n // 10) + last_digit


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)


# Iterative function to find minimum value
def find_minimum(my_list):
    minimum = None
    for element in my_list:
        if not minimum or (element < minimum):
            minimum = element
    return minimum


find_minimum([42, 17, 2, -1, 67])
# -1
find_minimum([])
# None
find_minimum([13, 72, 19, 5, 86])
# 5


# Recursive version of similar functionality
def find_min(my_list, min = None):
    if not my_list:
        return min

    if not min or my_list[0] < min:
        min = my_list[0]
    return find_min(my_list[1:], min)


# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)


# Iterative function to check if string is a Palindrome
def palindrome(my_string):
    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True


palindrome("abba")
# True
palindrome("abcba")
# True
palindrome("")
# True
palindrome("abcd")


# Here's a more efficient version
# Linear - O(N)
def is_palindrome(my_string):
    string_length = len(my_string)
    middle_index = string_length // 2
    for index in range(0, middle_index):
        opposite_character_index = string_length - index
    if my_string[index] != my_string[opposite_character_index]:
        return False
    return True


# My Recursive solution
def is_palindrome_r(string):
    if len(string) < 2:
        return True
    while string[0] != string[-1]:
        return False
    return is_palindrome_r(string[1:-1])


# test cases
print(is_palindrome_r("abba") == True)
print(is_palindrome_r("abcba") == True)
print(is_palindrome_r("") == True)
print(is_palindrome_r("abcd") == False)


# Multiplication, Shmultiplication
# Iterative approach to a multiplying function
def i_multiplication(num_1, num_2):
    result = 0
    for count in range(0, num_2):
        result += num_1
    return result


i_multiplication(3, 7)
# 21
i_multiplication(5, 5)
# 25
i_multiplication(0, 4)
# 0


# My Recursive solution:
def multiplication(num1, num2):
  result = 0
  if num1 == 0 or num2 == 0:
    return 0
  else:
    result += num1 + multiplication(num1, num2 - 1)
    return result


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)


# This algorithm will visit each node in the tree once,
# which makes it a linear runtime, O(N), where N
# is the number of nodes in the tree.

def depth(tree):
    result = 0
    # our "queue" will store nodes at each level
    queue = [tree]
    # loop as long as there are nodes to explore
    while queue:
        # count the number of child nodes
        level_count = len(queue)
        for child_count in range(0, level_count):
            # loop through each child
            child = queue.pop(0)
            # add its children if they exist
        if child["left_child"]:
                queue.append(child["left_child"])
        if child["right_child"]:
                queue.append(child["right_child"])
        # count the level
        result += 1
    return result


two_level_tree = {"data": 6, "left_child": {"data": 2}}

four_level_tree = {"data": 54, "right_child": {"data": 93, "left_child": {"data": 63, "left_child": {"data": 59}}}}


depth(two_level_tree)
# 2
depth(four_level_tree)
# 4


# My Recursive solution:
def depth(tree_node):
    if tree_node == None:
        return 0
    left_depth = depth(tree_node['left_child'])
    right_depth = depth(tree_node['right_child'])

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)

"""
End of File
"""

