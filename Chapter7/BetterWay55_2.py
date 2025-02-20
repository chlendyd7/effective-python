from queue import Queue
from threading import Thread

my_queue = Queue()
def consumer():
    print('소비자 대기')
    my_queue.get()
    print('소비자 완료')

thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
my_queue.put(object())
print('생산자 완료')
thread.join()
