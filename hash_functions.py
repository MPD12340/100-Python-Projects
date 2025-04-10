# hash_functions.py
# Contains functions for hashing and probing sequences

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def simpleHash(key):
    """A simple hashing function."""
    if isinstance(key, int):  # Integers hash to themselves
        return key
    elif isinstance(key, str):  # Strings are hashed by letters
        return sum(
            # Multiply the code for each letter by
            256 ** i * ord(key[i])  # 256 to the power of its position
            for i in range(len(key)))  # in the string
    elif isinstance(key, (list, tuple)):  # For sequences,
        return sum(
            # Multiply the simpleHash of each element
            256 ** i * simpleHash(key[i])  # by 256 to the power of its
            for i in range(len(key)))  # position in the sequence
    raise Exception(
        'Unable to hash key of type ' + str(type(key)))

def linearProbe(start, key, size):
    """Generator for linear probing sequence."""
    for i in range(size):
        yield (start + i) % size

def quadraticProbe(start, key, size):
    """Generator for quadratic probing sequence."""
    for i in range(size):
        yield (start + i*i) % size

def primeBelow(n):
    """Find the largest prime below n."""
    n -= 1 if n % 2 == 0 else 2  # Start with an odd number below n
    while (3 < n and not is_prime(n)):  # While n is bigger than 3 or
        n -= 2  # is not prime, go to next odd number
    return n

def doubleHashStep(key, size):
    """Determine step size for a given key."""
    prime = primeBelow(size)  # Find largest prime below array size
    return prime - (
        # Step size is based on second hash and
        simpleHash(key) % prime)  # is in range [1, prime]

def doubleHashProbe(start, key, size):
    """Generator to determine probe interval from a secondary hash of the key."""
    yield start % size  # Yield the first cell index
    step = doubleHashStep(key, size)  # Get the step size for this key
    for i in range(1, size):  # Loop over all remaining cells using
        yield (start + i * step) % size  # step from second hash of key
