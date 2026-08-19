# Simulate Producer-Consumer bounded buffer
# using Mutex (Lock) and Semaphores

import threading
import time
import random


# Maximum number of items that can be stored in the buffer
BUFFER_SIZE = 5

# Shared buffer
# Producer adds items to it and Consumer removes items from it
buffer = []


# Mutex (Lock)
# It allows only one thread at a time to access the buffer
mutex = threading.Lock()


# Semaphore to count empty spaces in the buffer
# Initially, all BUFFER_SIZE spaces are empty
empty_slots = threading.Semaphore(BUFFER_SIZE)


# Semaphore to count filled spaces in the buffer
# Initially, there are no items in the buffer
full_slots = threading.Semaphore(0)


# Producer function
# The producer creates items and puts them into the buffer
def producer(id, items_to_produce):

    # Repeat the process for the required number of items
    for item in range(items_to_produce):

        # Wait until there is an empty space in the buffer
        empty_slots.acquire()

        # Lock the buffer so that only this thread can access it
        mutex.acquire()

        # Add the produced item to the buffer
        buffer.append(item)

        # Display the produced item and current buffer
        print(f"Producer {id} produced {item} | Buffer: {buffer}")

        # Unlock the buffer
        mutex.release()

        # Increase the number of filled slots
        full_slots.release()

        # Wait for a random time before producing the next item
        time.sleep(random.uniform(0.1, 0.5))


# Consumer function
# The consumer takes items from the buffer
def consumer(id, items_to_consume):

    # Repeat the process for the required number of items
    for _ in range(items_to_consume):

        # Wait until at least one item is available
        full_slots.acquire()

        # Lock the buffer so that only this thread can access it
        mutex.acquire()

        # Remove the first item from the buffer
        item = buffer.pop(0)

        # Display the consumed item and current buffer
        print(f"Consumer {id} consumed {item} | Buffer: {buffer}")

        # Unlock the buffer
        mutex.release()

        # Increase the number of empty spaces
        empty_slots.release()

        # Wait for a random time before consuming the next item
        time.sleep(random.uniform(0.1, 0.5))


# This block runs only when this Python file is executed directly
if __name__ == "__main__":

    # Total number of items to produce and consume
    num_items = 10

    # Create a producer thread
    # id = 1 and it will produce 10 items
    prod_thread = threading.Thread(
        target=producer,
        args=(1, num_items)
    )

    # Create a consumer thread
    # id = 1 and it will consume 10 items
    cons_thread = threading.Thread(
        target=consumer,
        args=(1, num_items)
    )

    # Start the producer thread
    prod_thread.start()

    # Start the consumer thread
    cons_thread.start()

    # Wait for the producer thread to finish
    prod_thread.join()

    # Wait for the consumer thread to finish
    cons_thread.join()

    # Display final message
    print("All items produced and consumed.")
