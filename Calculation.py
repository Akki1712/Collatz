from numba import jit
import time

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return primes

def is_prime_sieve(n, primes):
    return primes[n]

cal_num = 1000000
num_it_2 = []

@jit(nopython=True)
def collatz_1(n: int) -> int:
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

start_time = time.time()

number_list = list(range(2, cal_num))
num_it_2 = [collatz_1(i) for i in number_list]

limit = max(num_it_2)  # Set the limit based on the maximum value in num_it_2
primes = sieve_of_eratosthenes(limit)

prime = [length for length in num_it_2 if is_prime_sieve(length, primes)]
notprime = [length for length in num_it_2 if not is_prime_sieve(length, primes)]

end_time = time.time()
print("Number of Prime Lengths:", len(prime))
print("Number of Non-Prime Lengths:", len(notprime))

print("Ratio of Non-Prime to Prime Lengths:", len(notprime) / len(prime))

print("Maximum Collatz Sequence Length:", max(num_it_2))

execution_time = end_time - start_time
print("Time taken:", execution_time, "seconds")
