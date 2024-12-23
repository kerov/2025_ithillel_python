import time
import logging


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        if exc_type is not None:
            logging.error(f'An error occured: {exc_value}')
        logging.info(f'The method executed in {self.execution_time} seconds.')


loop_size = 10000


def double_loop():
    for i in range(loop_size):
        for j in range(loop_size):
            continue


def long_loop():
    for i in range(loop_size * loop_size):
        continue


def sleep_method():
    time.sleep(2)


def main():
    with TimerContext():
        double_loop()

    with TimerContext():
        long_loop()

    with TimerContext():
        sleep_method()


main()
