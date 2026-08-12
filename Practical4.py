# Measure execution time for sequential vs thread execution

import threading
import time


def worker(id, delay):
    print(f"Task {id} starting")
    time.sleep(delay)
    print(f"Task {id} finished")


def sequential_demo():
    start = time.time()

    for i in range(5):
        worker(i, i + 1)

    end = time.time()
    print(f"Sequential execution time: {end - start:.2f} seconds\n")


def threaded_demo():
    threads = []
    start = time.time()

    for i in range(5):
        t = threading.Thread(target=worker, args=(i, i + 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Threaded execution time: {end - start:.2f} seconds\n")


if __name__ == "__main__":
    print("=== Sequential Demo ===")
    sequential_demo()

    print("=== Threaded Demo ===")
    threaded_demo()
