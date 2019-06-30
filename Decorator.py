import time
import os
from threading import Thread


def file_writer(filename, counter):
    print("Start t with PID {}".format(os.getpid()))
    time.sleep(10)
    with open(filename, 'a') as f:
        for line in range(counter):
            f.write("String number {} \n".format(str(counter)))


t = []
for count in range(10):
    t.append(Thread(target=file_writer, args=("File_number {}".format(count), count)))

for thr in t:
    thr.start()

for thr in t:
    thr.join()
