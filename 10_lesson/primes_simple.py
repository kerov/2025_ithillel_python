from multiprocessing import Process


def get_primes_amount(num: int,) -> int:
    result = 0
    for i in range(2, num + 1):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        if (counter == 2):
            result += 1
    print(f"for the number {num}, result {result}")


def main():
    numbers = [20, 40000, 400, 1000000, 700]

    for i in numbers:
        p = Process(
            target=get_primes_amount,
            kwargs={
                "num": i,
            },
        )
        p.start()


if __name__ == "__main__":
    raise SystemExit(main())
