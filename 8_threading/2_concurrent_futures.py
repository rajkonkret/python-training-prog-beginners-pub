import time
from concurrent.futures import ThreadPoolExecutor

a = 0


def task(value):
    global a
    for i in range(100_000_000):
        a += value


executor = ThreadPoolExecutor(max_workers=2)
start_time = time.perf_counter()
thread1 = executor.submit(task, 1)
thread2 = executor.submit(task, -1)
print(thread1.result(None))
print(thread2.result(None))
end_time = time.perf_counter()
executor.shutdown()

# context manager - alternatywny sposób użycia
# with ThreadPoolExecutor(max_workers=2) as executor:
#     start_time = time.perf_counter()
#     thread1 = executor.submit(task, 1)
#     thread2 = executor.submit(task, -1)
#     print(thread1.result(None))
#     print(thread2.result(None))
#     end_time = time.perf_counter()

print(f"Czas wykonania: {end_time - start_time} sek")
print(a)
