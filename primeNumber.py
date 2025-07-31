import numpy as np

nums = np.arange(2, 51)
is_prime = np.ones(len(nums), dtype=bool)

for i in range(2, int(np.sqrt(50)) + 1):
    is_prime[nums % i == 0] = False
    is_prime[nums == i] = True  

primes = nums[is_prime]
print("Prime Numbers:", primes)
