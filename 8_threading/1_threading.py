from threading import Thread
from time import perf_counter

a = 0


def task(value):
    global a
    for i in range(100_000_000):
        a += value


start_time = perf_counter()

t1 = Thread(target=task, args=(1,))
t2 = Thread(target=task, args=(-1,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f"Czas wykonania: {end_time - start_time} sek")
print(a)
