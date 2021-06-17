import queue
import threading
import time
import tarfile
import os


address = "/home/vango/archives/"
address_unpack = "/home/vango/unpack/"


def task(name):
    global queue_tarfile
    print(name, 'start')

    while not queue_tarfile.empty():
        os.chdir(path=address)
        tarfile_gz = tarfile.open(name=queue_tarfile.get())
        time.sleep(5)
        tarfile_gz.extractall(path=address_unpack)
        queue_tarfile.task_done()
        print(name)


queue_tarfile = queue.Queue()
catalog = os.listdir(path=address)
for file in catalog:
    queue_tarfile.put(file)

threads = []
for i in range(0, 3):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()
