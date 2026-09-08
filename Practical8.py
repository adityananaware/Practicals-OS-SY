# Simulate First Come First Serve (FCFS) Scheduling

import threading
import time
import random
from queue import Queue


# Class used to represent a process
class Process:

    # Constructor of the Process class
    def __init__(self, pid, burst_time):
        self.pid = pid                  # Store the Process ID
        self.burst_time = burst_time    # Store the time required by process


# Create a queue to store processes
# FCFS works according to the order in which processes enter the queue
fcfs_queue = Queue()

# Create a semaphore to control access to the CPU
# Value 1 means only one process can use the CPU at a time
cpu_lock = threading.Semaphore(1)


# Function executed by each thread
def process_execution(process):

    # Add the process to the FCFS queue
    fcfs_queue.put(process)

    # Display process arrival information
    print(
        f"Process {process.pid} arrives with burst time "
        f"{process.burst_time:.2f}"
    )

    # Keep checking until it is the process's turn
    while True:

        # Check whether this process is first in the queue
        if fcfs_queue.queue[0] == process:

            # Acquire the CPU lock
            # Only one process can execute at a time
            cpu_lock.acquire()

            # Display that the process has started execution
            print(f"Process {process.pid} starts execution")

            # Simulate the process execution
            # The process runs for its burst time
            time.sleep(process.burst_time)

            # Display that the process has completed execution
            print(f"Process {process.pid} finishes execution")

            # Remove the completed process from the queue
            fcfs_queue.get()

            # Release the CPU lock
            cpu_lock.release()

            # Exit the loop because this process is completed
            break

        else:

            # If it is not this process's turn,
            # wait for a short time and check again
            time.sleep(0.01)


# This block runs only when this Python file is executed directly
if __name__ == "__main__":

    # Create 5 processes
    # Process IDs will be 0, 1, 2, 3 and 4
    # Each process gets a random burst time between 0.5 and 1.5 seconds
    processes = [
        Process(i, random.uniform(0.5, 1.5))
        for i in range(5)
    ]

    # Create one thread for each process
    threads = [
        threading.Thread(
            target=process_execution,
            args=(p,)
        )
        for p in processes
    ]

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Display completion message
    print("FCFS scheduling simulation completed.")
