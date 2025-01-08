from multiprocessing import Process, Queue
import time


def get_primes_amount(num: int, result_queue: Queue) -> int:
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

    result_queue.put((num, result))


def main():
    numbers = [20, 40000, 400, 1000000, 700]

    processes = []
    result_queue = Queue()

    for i in numbers:
        p = Process(
            target=get_primes_amount,
            kwargs={
                "num": i,
                "result_queue": result_queue
            },
        )
        p.start()
        processes.append(p)

    timeout = 100
    start_time = time.time()

    while processes:
        if time.time() - start_time > timeout:
            for p in processes:
                if p.is_alive():
                    p.terminate()
                    print(f'Stop the {p} process')
            break
        if not result_queue.empty():
            num, result = result_queue.get()
            print(f"For the number {num}, result: {result}")

        processes = [p for p in processes if p.is_alive()]


if __name__ == "__main__":
    raise SystemExit(main())
