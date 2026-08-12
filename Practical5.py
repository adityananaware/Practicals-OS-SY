# Explain thread safety and synchronization when accessing shared variables

import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter

    for _ in range(1000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)
