def isPrime(n: int) -> bool:
    """
    https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    # Any prime number > 3 would be of the form 6n+- 1
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        counter = 0
        for i in range(L, R + 1):
            if isPrime(bin(i).count("1")):
                counter += 1
        return counter
