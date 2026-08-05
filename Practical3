import threading
import time


# Function executed by each thread
def worker(thread_id, sleep_time):
    print(f"[Thread-{thread_id}] Starting work...")
    time.sleep(sleep_time)
    print(f"[Thread-{thread_id}] Work completed after {sleep_time} second(s).")


def thread_lifecycle_demo():
    print("=== Thread Lifecycle Demo ===\n")

    threads = []

    # Create 5 threads
    for i in range(5):
        t = threading.Thread(
            target=worker,
            args=(i, i + 1),
            name=f"Worker-{i}"
        )

        threads.append(t)

        print(f"[Main] {t.name} created, Alive? {t.is_alive()}")

    print()

    # Start all threads
    for t in threads:
        t.start()
        print(f"[Main] {t.name} started, Alive? {t.is_alive()}")

    print()

    # Wait for all threads to finish
    for t in threads:
        t.join()
        print(f"[Main] {t.name} finished, Alive? {t.is_alive()}")

    print("\nAll threads have completed their work.")


if __name__ == "__main__":
    thread_lifecycle_demo()
