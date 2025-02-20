from threading import Thread
import select
import socket
import time

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count = self.count + offset

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # 센서를 읽는다
        counter.increment(1)

from threading import Thread

how_many = 10**7
counter = Counter()
start = time.time()

threads = []
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
