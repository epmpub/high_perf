import math
import time

from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


from multiprocessing import Process

PRIMES = [112272535095293] * 100


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_processing():
    with ProcessPoolExecutor() as executor:
        result = executor.map(is_prime, PRIMES)

 
if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread ,cost:", end-start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread ,cost:", end-start, "seconds")

    start = time.time()
    multi_processing()
    end = time.time()
    print("multi_processing ,cost:", end-start, "seconds")

