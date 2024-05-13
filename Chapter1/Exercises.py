# Write a short Python function, is multiple(n, m), 
# that takes two integer values and returns True if n is a multiple of m, 
# that is, n = mi for some integer i, and False otherwise.

def isMultiple(n, m):
    
    if (m%n) == 0:
        return True
    else:
        return False
    

# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def isEven(k):
    return (k & 1) == 0


# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    
    minNumber = maxNumber = data[0]
    
    for number in data[1:]:
        
        if number < minNumber:
            minNumber = number
        elif number > maxNumber:
            maxNumber = number
    
    return minNumber, maxNumber


# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sumOfAllSquares(n):
    
    sum = 0
    
    while n > 1:
        n -= 1
        sum += n**2
    
    return sum

def anotherWaySumOfAllSquares(n):
    return sum([x**2 for x in range(1, n)])


# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sumOfOddSquares(n):
    
    sum = 0
    
    while n > 0:
        
        n -= 1
        
        if n % 2 == 1:
            sum += n**2
            
    return sum

def anotherWaySumOfOddSquares(n):
    return sum([x**2 for x in range(1, n) if x % 2 == 1])