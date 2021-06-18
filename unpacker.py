import queue
import threading
import tarfile
import os
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', action="store", help="the address of the folder containing the archives")
parser.add_argument('-au', '--address_unpack', action="store", help="the address where the archives will be unpacked")
parser.add_argument("-t", "--thread", action="store", type=int, help="number of threads used, default 1")
parser.add_argument("-p", "--pattern", action="store", help="your sample regex template, by default will unpack everything")
args = parser.parse_args()

address = args.address
address_unpack = args.address_unpack
number_threads = args.thread if args.thread else 1
pattern = args.pattern if args.pattern else r".*"


def task(name):
    global queue_tarfile
    print(name, 'start')

    while not queue_tarfile.empty():
        item = queue_tarfile.get()
        tarfile_gz = tarfile.open(name=item["catalog"])
        tarfile_gz.extract(item["element"], path=address_unpack)
        queue_tarfile.task_done()
        print(name)


queue_tarfile = queue.Queue()
catalog = os.listdir(path=address)
for archive in catalog:
    os.chdir(path=address)
    tar_gz = tarfile.open(name=archive)
    for file in tar_gz.getnames():
        result = re.search(pattern, file)
        if result:
            queue_tarfile.put({"catalog": archive, "element": file})


threads = []
for i in range(0, number_threads):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

