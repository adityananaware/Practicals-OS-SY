from multiprocessing import Process, Semaphore, Value
import time


def producer(empty, full, data):
    for i in range(5):
        empty.acquire()          # Wait if buffer is full
        data.value += 1
        print(f"Produced: {data.value}")
        full.release()           # Signal that an item is available
        time.sleep(1)


def consumer(empty, full, data):
    for i in range(5):
        full.acquire()           # Wait if buffer is empty
        print(f"Consumed: {data.value}")
        empty.release()          # Signal that buffer is empty
        time.sleep(1)


if __name__ == "__main__":

    # Initialize semaphores
    empty = Semaphore(1)
    full = Semaphore(0)

    # Shared integer variable
    data = Value('i', 0)

    # Create producer and consumer processes
    producer_process = Process(
        target=producer,
        args=(empty, full, data)
    )

    consumer_process = Process(
        target=consumer,
        args=(empty, full, data)
    )

    # Start processes
    producer_process.start()
    consumer_process.start()

    # Wait for completion
    producer_process.join()
    consumer_process.join()

    print("Producer and Consumer have completed successfully.")
