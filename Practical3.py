# Import the threading module.
# This module allows us to create and work with threads.
import threading

# Import the time module.
# We will use time.sleep() to pause a thread for some seconds.
import time


# This function contains the work that each thread will perform.
# thread_id = unique number of the thread
# sleep_time = number of seconds the thread will wait
def worker(thread_id, sleep_time):

    # Display a message when the thread starts its work.
    print(f"[Thread-{thread_id}] Starting work...")

    # Pause the current thread for the given number of seconds.
    # For example, Thread-0 sleeps for 1 second,
    # Thread-1 sleeps for 2 seconds, etc.
    time.sleep(sleep_time)

    # Display a message after the thread completes its work.
    print(
        f"[Thread-{thread_id}] "
        f"Work completed after {sleep_time} second(s)."
    )


# This function demonstrates the complete lifecycle of threads.
def thread_lifecycle_demo():

    # Display the title of our program.
    print("=== Thread Lifecycle Demo ===\n")

    # Create an empty list.
    # We will store all the thread objects in this list.
    threads = []


    # Create 5 threads.
    # range(5) gives numbers from 0 to 4.
    for i in range(5):

        # Create a Thread object.
        t = threading.Thread(

            # target tells the thread which function it should execute.
            # Here, every thread will execute the worker() function.
            target=worker,

            # args passes arguments to the worker() function.
            # i = thread ID
            # i + 1 = sleeping time
            args=(i, i + 1),

            # Give the thread a meaningful name.
            # Names will be Worker-0, Worker-1, etc.
            name=f"Worker-{i}"
        )

        # Add the newly created thread to the threads list.
        threads.append(t)

        # is_alive() checks whether the thread is currently running.
        # The thread has only been CREATED, not STARTED yet,
        # so it will normally return False.
        print(
            f"[Main] {t.name} created, "
            f"Alive? {t.is_alive()}"
        )


    # Print a blank line to make the output easier to read.
    print()


    # Start all the threads one by one.
    for t in threads:

        # start() starts the execution of the thread.
        # After this, the worker() function begins running.
        t.start()

        # Check whether the thread is currently alive.
        # While the thread is running, this will normally be True.
        print(
            f"[Main] {t.name} started, "
            f"Alive? {t.is_alive()}"
        )


    # Print a blank line for better output formatting.
    print()


    # Wait for all threads to complete their work.
    for t in threads:

        # join() makes the main thread wait
        # until the current thread has finished.
        t.join()

        # After join() returns, this thread has completed.
        # Therefore, is_alive() should be False.
        print(
            f"[Main] {t.name} finished, "
            f"Alive? {t.is_alive()}"
        )


    # This message is displayed after all 5 threads have finished.
    print("\nAll threads have completed their work.")


# This condition checks whether this Python file
# is being executed directly.
if __name__ == "__main__":

    # Call the function that demonstrates
    # thread creation and the thread lifecycle.
    thread_lifecycle_demo()
