import queue
import threading
import tarfile
import os
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', action="store", help="kek")
parser.add_argument("-t", "--thread", action="store", type=int, help="werwerwer")
parser.add_argument("--pattern", action="store", help="werwerwer")
args = parser.parse_args()


address = "/home/vango/archives/"
address_unpack = "/home/vango/unpack/"
pattern = r"прп"


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
for i in range(0, 3):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

