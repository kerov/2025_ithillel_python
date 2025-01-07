def get_primes_amount(num: int) -> int:
    result = 0
    for i in num:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        results += 1

    return results


numbers = [40000, 400, 1000000, 700]

for i in numbers:
    print(i)

# NOTE: Well, this realization takes too much time...
#       Would be great if I can see less numbers earlier that great numbers :)

# TODO: Complete get_primes_amount function using concurrency approach
