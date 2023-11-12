from multiprocessing import Pool
import logging
from time import time
import os

# from datetime import time


logger = logging.getLogger()
logger.info("starting prg")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# def func_run_time(func):
#     def wrapper(*args):
#         start_time = time()
#         result = func(*args)
#         func_run_time = time() - start_time
#         logger.info(f"func run time is : {func_run_time}")
#         return result
#     return wrapper


# @func_run_time
def factorize(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    logger.debug(f"{result=}")
    return result


def normal_factorize(*numbers):
    start_time = time()
    logger.info("running normal_factorize")
    result = map(factorize, numbers)
    func_run_time = time() - start_time
    logger.info(f"normal func run time is : {func_run_time}")
    return result


def multiprocess_factorize(*numbers):
    start_time = time()
    logger.info("running multiprocess_factorize")
    cpus = os.cpu_count()
    with Pool(processes=cpus) as pool:
        result = pool.map(factorize, numbers)

    func_run_time = time() - start_time
    logger.info(f"multiprozess func run time is : {func_run_time}")
    return result


if __name__ == "__main__":
    a, b, c, d = normal_factorize(128, 255, 99999, 10651060)
    e, f, g, h = multiprocess_factorize(128, 255, 99999, 10651060)

    assert a == e
    assert b == f
    assert c == g
    assert d == h

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]
