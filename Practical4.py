# Measure execution time for sequential vs threaded execution

import threading
import time


# Function that represents a task performed by a worker
def worker(id, delay):
    print(f"Task {id} starting")

    # Pause the task for the given number of seconds
    time.sleep(delay)

    print(f"Task {id} finished")


# Function to demonstrate sequential execution
def sequential_demo():
    # Record the starting time
    start = time.time()

    # Run 5 tasks one after another
    for i in range(5):
        worker(i, i + 1)

    # Record the ending time
    end = time.time()

    # Calculate and display total execution time
    print(f"Sequential execution time: {end - start:.2f} seconds\n")


# Function to demonstrate threaded execution
def threaded_demo():
    # List used to store all created threads
    threads = []

    # Record the starting time
    start = time.time()

    # Create and start 5 threads
    for i in range(5):
        # Create a thread that will execute the worker function
        # args=(i, i+1) passes id and delay to worker()
        t = threading.Thread(target=worker, args=(i, i + 1))

        # Store the thread in the list
        threads.append(t)

        # Start the thread
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Record the ending time
    end = time.time()

    # Calculate and display total execution time
    print(f"Threaded execution time: {end - start:.2f} seconds\n")


# Program execution starts here
if __name__ == "__main__":

    # Demonstrate sequential execution
    print("=== Sequential Demo ===")
    sequential_demo()

    # Demonstrate threaded execution
    print("=== Threaded Demo ===")
    threaded_demo()
