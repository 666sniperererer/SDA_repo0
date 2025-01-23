import threading
import time
global start
start = time.time()

def iterate_print(iter):
    start = time.time()
    # A function prints the elements of a list
    for item in iter:
        print(item)
        time.sleep(1)

if __name__ == "__main__":
    # creating threads
    t1 = threading.Thread(target=iterate_print, args=(range(5),))  # writing out successive natural numbers
    t2 = threading.Thread(target=iterate_print, args=("Python",))  # writing the characters of the string

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    t1.join()
    t2.join()
    end = time.time()

    print("Done!")
    print(f"Trvalo to: {end-start} sekund")