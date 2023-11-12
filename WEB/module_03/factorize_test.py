from factorize import normal_factorize, multiprocess_factorize

if __name__ == '__main__':
    RNG = 5
    normal = normal_factorize(*[i for i in range(RNG)])

    multi = multiprocess_factorize(*[i for i in range(RNG)])

    assert [*normal] == [*multi]
