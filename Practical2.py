import multiprocessing
import time


# -----------------------------
# Shared Memory Example
# -----------------------------

def shared_memory_worker(shared_list, index, value):
    print(f"[Shared Memory] Process {index} is writing value {value}")

    # Write value into shared memory
    shared_list[index] = value

    # Wait for 1 second
    time.sleep(1)

    print(f"[Shared Memory] Process {index} reads value {shared_list[index]}")


def shared_memory_demo():

    print("===== Shared Memory Demo =====")

    # Create shared array of 5 integers
    shared_list = multiprocessing.Array('i', 5)

    processes = []

    for i in range(5):

        p = multiprocessing.Process(
            target=shared_memory_worker,
            args=(shared_list, i, i * 10)
        )

        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\nFinal Shared Memory:", list(shared_list))


# -----------------------------
# Message Passing Example
# -----------------------------

def sender(queue, value):

    print(f"[Sender] Sending : {value}")
    queue.put(value)


def receiver(queue):

    value = queue.get()
    print(f"[Receiver] Received : {value}")


def message_passing_demo():

    print("\n===== Message Passing Demo =====")

    queue = multiprocessing.Queue()

    processes = []

    for i in range(5):

        sender_process = multiprocessing.Process(
            target=sender,
            args=(queue, i * 100)
        )

        receiver_process = multiprocessing.Process(
            target=receiver,
            args=(queue,)
        )

        processes.append(sender_process)
        processes.append(receiver_process)

        sender_process.start()
        receiver_process.start()

    for p in processes:
        p.join()

    print("\nMessage Passing Completed.")


# -----------------------------
# Main Function
# -----------------------------

if __name__ == "__main__":

    shared_memory_demo()

    message_passing_demo()
