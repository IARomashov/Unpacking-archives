import queue
import threading
import time
import tarfile
import os
import argparse

import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', action="store", help="the address of the folder containing the archives")
parser.add_argument('-au', '--address_unpack', action="store", help="the address where the archives will be unpacked")
parser.add_argument("-t", "--thread", action="store", type=int, help="number of threads used")
args = parser.parse_args()

address = args.address
address_unpack = args.address_unpack
number_threads = args.thread if args.thread else 1


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
for i in range(0, number_threads):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()
