#Find prime numbers
def optimus(start, end):
    primes = []
    def prime_is(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(start, end + 1):
        if prime_is(num):
            primes.append(num)
    
    return primes
start = 10
end = 50
print(optimus(start, end))
