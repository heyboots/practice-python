def is_prime(x):
    if x < 2: # Check if number is less than 2 (excludes negative numbers, 0, 1
        return False
    elif x == 2: # Check if number is 2. Two is a jerk.
        return True
    elif x % 2 == 0: # Check if number is even, excludes half of all numbers.
        return False
    else:
        for j in range(3, int(x ** 0.5) + 1, 2): # Check modulo of every odd number between 3 (two was already checked) and the square root of x. Add one to account for rounding issues with int.
            if x % j == 0:
                return False
    return True # If code gets here number is prime.
