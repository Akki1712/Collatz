import matplotlib.pyplot as plt
import time
from numba import njit

@njit(nopython=True)
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return primes

def is_prime_sieve(n, primes):
    if n < len(primes):
        return primes[n]
    return False

@njit(nopython=True)
def collatz_1(n: int) -> int:
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def get_collatz_ratios(cal_num_range):
    ratios = []
    percentages = []
    percentages_prime_no = []
    start_time = time.time()

    # Generate primes array up to twice cal_num_range
    primes = sieve_of_eratosthenes(2 * cal_num_range)

    for cal_num in range(10, cal_num_range + 1, 100):
        num_it_2 = [collatz_1(i) - 1 for i in range(2, cal_num)]
        prime_lengths = [length for length in num_it_2 if is_prime_sieve(length, primes)]
        count_prime_length = len(prime_lengths)

        percentage_prime_length = count_prime_length / cal_num * 100

        count_prime = sum(1 for i in range(2, cal_num) if is_prime_sieve(i, primes))
        percentage_prime_number = count_prime / cal_num * 100

        percentages.append(percentage_prime_length)
        percentages_prime_no.append(percentage_prime_number)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.4f} seconds")
    return percentages, percentages_prime_no

cal_num_range = 1000000  
percentages, percentages_prime_no = get_collatz_ratios(cal_num_range)

# Plotting
plt.figure(figsize=(20, 10))

plt.subplot(1, 2, 1)
plt.plot(range(10, cal_num_range + 1, 100), percentages, marker='o', linestyle='-', color='green')
plt.title("Percentage of Prime Lengths")
plt.xlabel("Calculated Number Range")
plt.ylabel("Percentage of Prime Lengths")
plt.text(cal_num_range, percentages[-1], f'{percentages[-1]:.2f}%', ha='left', va='top', color="brown")

plt.subplot(1, 2, 2)
plt.plot(range(10, cal_num_range + 1, 100), percentages_prime_no, marker='o', linestyle='-', color='red')
plt.title("Percentage of Prime Numbers")
plt.xlabel("Calculated Number Range")
plt.ylabel("Percentage of Prime Numbers")
plt.text(cal_num_range, percentages_prime_no[-1], f'{percentages_prime_no[-1]:.2f}%', ha='left', va='bottom', color="blue")

plt.tight_layout()
plt.show()
