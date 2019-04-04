import threading
from threading import Thread


def print_numbers():
    for i in range(1, 11):
        print(i)


ct = threading.current_thread()
print(ct.name)
nt = Thread(target=print_numbers)
nt.start()
print("\nNo. of threads = ", threading.active_count())

# nt.join()

print("\nThe End\n")
