#!/usr/bin/python
# -*- coding: UTF-8 -*-

#----------------------------------------

# 需求是建立三个线程输出 one two three four five 五个字母，需要包含线程名
# 实现第一步需要重写thread方法，并建立三个实例 分别是线程名、具体输出数据的实例、线程ID
# 实现第二步需要写清楚线程启动以及线程结束的过程
#

#----------------------------------------
# 建立3个线程
# 分别输出1，2，3，4，5
# 要求使用队列，还需要对线程进行控制，每次队列输出都需要lock

import Queue
import threading
import time


exitFlag = True


class Mythread(threading.Thread):

    def __init__(self, threadID, name, queue):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = queue

    def run(self):
        print 'Starting threading:%s' % self.name
        process(self.name, self.queue)  # 传参到process
        print 'Ending threading:%s' % self.name


def process(threadName, queue):
    while exitFlag:
        queuelock.acquire()
        if not workqueue.empty():
            data = queue.get()
            queuelock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queuelock.release()
        time.sleep(1)


threadlist = ['Thread-1', 'Thread-2', 'Thread-3']
namelist = ['one', 'two', 'three', 'four', 'five']
queuelock = threading.Lock()
workqueue = Queue.Queue(10)
threadID = 1
threads = []

for tname in threadlist:
    thread = Mythread(threadID, tname, workqueue)
    thread.start()
    threads.append(thread)
    threadID += 1

for word in namelist:
    workqueue.put(word)


while not workqueue.empty():
    pass


exitFlag = False
for t in threads:
    t.join()


print 'Exiting Main Thread'
