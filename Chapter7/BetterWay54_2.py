from threading import Lock
import time
class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        counter.increment(1)

from threading import Thread

how_many = 10**7
counter = LockingCounter()

threads = []
start = time.time()
for i in range(5):
    thread = Thread(target=worker,
                    args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
end = time.time()
print(f'카운터 값은 {expected}여야 하는데, 실제로는 {found} 입니다')
print(end - start)
