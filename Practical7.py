# Implement Reader and Writer Prioritization
import threading
import time
import random


# Shared data that both readers and writers will access
shared_data = 0

# Number of readers currently reading
read_count = 0

# Lock used to safely modify read_count
read_count_lock = threading.Lock()

# Lock used to protect the shared resource
resource_lock = threading.Lock()

# Lock used to give priority to writers
write_request = threading.Lock()


# Function executed by each reader thread
def reader(id):
    global read_count

    while True:

        # Reader first checks whether a writer is waiting
        # If a writer is waiting, the reader must wait
        write_request.acquire()
        write_request.release()

        # Safely increase the number of active readers
        with read_count_lock:
            read_count += 1

            # If this is the first reader,
            # lock the shared resource so that writers cannot enter
            if read_count == 1:
                resource_lock.acquire()

        # Reader reads the shared data
        print(f"Reader {id} reads shared_data = {shared_data}")

        # Simulate the time taken to read
        time.sleep(random.uniform(0.1, 0.5))

        # Safely decrease the number of active readers
        with read_count_lock:
            read_count -= 1

            # If this was the last reader,
            # release the shared resource for writers
            if read_count == 0:
                resource_lock.release()

        # Wait for a short random time before reading again
        time.sleep(random.uniform(0.1, 0.5))


# Function executed by each writer thread
def writer(id):
    global shared_data

    while True:

        # Writer requests access.
        # This prevents new readers from entering.
        write_request.acquire()

        # Writer gets exclusive access to the shared resource
        resource_lock.acquire()

        # Update the shared data
        shared_data += 1

        # Display the updated value
        print(f"Writer {id} updates shared_data to {shared_data}")

        # Simulate the time taken to write
        time.sleep(random.uniform(0.2, 0.6))

        # Release the shared resource
        resource_lock.release()

        # Allow readers/writers to try again
        write_request.release()

        # Wait before the writer performs another operation
        time.sleep(random.uniform(0.5, 1.0))


# Program execution starts here
if __name__ == "__main__":

    # Create 3 reader threads
    readers = [
        threading.Thread(target=reader, args=(i,))
        for i in range(3)
    ]

    # Create 2 writer threads
    writers = [
        threading.Thread(target=writer, args=(i,))
        for i in range(2)
    ]

    # Combine all reader and writer threads
    for t in readers + writers:

        # Make the threads daemon threads.
        # They will automatically stop when the main program ends.
        t.daemon = True

        # Start the thread
        t.start()

    # Let the simulation run for 10 seconds
    time.sleep(10)

    # Display the completion message
    print("Simulation finished.")
