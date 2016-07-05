 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import os;

print os.name;
#	'posix'

print os.uname;
#	('Darwin', 'magceMac-mini.local', '15.5.0',
#	'Darwin Kernel Version 15.5.0: Tue Apr 19 18:36:36 PDT 2016;
#	root:xnu-3248.50.21~8/RELEASE_X86_64', 'x86_64')

print os.environ;
#	{'VERSIONER_PYTHON_PREFER_32_BIT': 'no', ...}

print os.getenv('PATH');
#	'/Library/Frameworks/Python.framework/Versions/2.7/bin:
#	/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:
#	/usr/sbin:/sbin'

print os.path.abspath('.');
#	'/Users/magce/learn/python/IO'

os.path.join('/Users/magce', 'testdir'); #show path
os.mkdir('/Users/magce/testdir');
os.rmdir('/Users/magce/testdir');

os.path.split('/Users/magce/testdir/file.txt');
#	('/Users/michael/testdir', 'file.txt')

os.path.splitext('/path/to/file.txt');
#	('/path/to/file', '.txt')

os.rename('test.txt', 'test.py');
os.remove('test.py');

[x for x in os.listdir('.') if os.path.isdir(x)]
# show dir

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# show py file
#	['OS.py', 'RW.py']

# copyfile() in shutil module



# search file & keyword
def search_file(path, text):
    res = []
    for item in [x for x in os.listdir(path)]:
        abspath = os.path.join(path, item);
        if os.path.isdir(abspath):
            res += search_file(abspath, text);
        elif text in item:
            res.append(abspath);
    return res;

def search(text):
    res = search_file(os.getcwd(), text);
    for r in res:
        print r;

# process

print 'Process (%s) start...' % os.getpid();
pid = os.fork();
if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid());
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid);
#   Process (876) start...
#   I (876) just created a child process (877).
#   I am child process (877) and my parent is 876.

# creat process
# from multiprocessing import Process;

# def run_proc(name):
#     print 'Run child process %s (%s)...' % (name, os.getpid())

# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Process(target=run_proc, args=('test',))
#     print 'Process will start.'
#     p.start()
#     p.join()
#     print 'Process end.'

#   Parent process 928.
#   Process will start.
#   Run child process test (929)...
#   Process end.


# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, (end - start))

# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'

#   Parent process 669.
#   Waiting for all subprocesses done...
#   Run task 0 (671)...
#   Run task 1 (672)...
#   Run task 2 (673)...
#   Run task 3 (674)...
#   Task 2 runs 0.14 seconds.
#   Run task 4 (673)...
#   Task 1 runs 0.27 seconds.
#   Task 3 runs 0.86 seconds.
#   Task 0 runs 1.41 seconds.
#   Task 4 runs 1.91 seconds.
#   All subprocesses done.

# from multiprocessing import Process, Queue
# import os, time, random

# # write data
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print 'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())

# # read data
# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue.' % value

# if __name__=='__main__':
#     # create queue sent to subprocess
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # start subprocess pw write
#     pw.start()
#     # start subprocess pr read
#     pr.start()
#     # wait pw over
#     pw.join()
#     # pr deadloop
#     pr.terminate()

