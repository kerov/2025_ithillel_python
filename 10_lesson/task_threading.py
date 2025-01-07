import random
import threading


def fill_list_with_randoms(random_list: list[int], size: int = 10_000):
    random_list.extend(random.randint(1, 1000) for _ in range(size))


def calculate_sum(random_list: list[int]):
    result = sum(random_list)
    print(f"Sum = {result}")


def calculate_avg(random_list: list[int]):
    result = sum(random_list) / len(random_list)
    print(f"Avg = {result}")


def main():
    random_list: list[int] = []
    thread_1 = threading.Thread(
        target=fill_list_with_randoms, args=(random_list,))
    thread_2 = threading.Thread(target=calculate_sum, args=(random_list,))
    thread_3 = threading.Thread(target=calculate_avg, args=(random_list,))

    thread_1.start()
    thread_1.join()

    thread_2.start()
    thread_3.start()

    thread_2.join()
    thread_3.join()


main()
