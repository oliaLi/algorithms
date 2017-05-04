# Create a function which will check if the number is prime or not.
# Function takes one simple parameter, n, and outputs a boolean, either True or False.

def isPrime(n):
    i = 2
    if n < 2:
        return False
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True