# import time
# def fun1():
#     print("********fun1 started*********")
#     for i in range(10):
#         time.sleep(1)
#         print("working on fun1")
#     print("********fun1 completed*********")

# def fun2():
#     print("********fun2 started*********")
#     for i in range(10):
#         time.sleep(1)
#         print("working on fun2")
#     print("********fun2 completed*********")

# fun1()
# fun2()

#how much time taken to complete the above job

# import time
# def fun1():
#     print("********fun1 started*********")
#     for i in range(5):
#         time.sleep(1)
#         print("working on fun1")
#     print("********fun1 completed*********")

# def fun2():
#     print("********fun2 started*********")
#     for i in range(5):
#         time.sleep(1)
#         print("working on fun2")
#     print("********fun2 completed*********")

# t1=time.time()
# fun1()
# fun2()
# t2=time.time()
# print("time taken to complete the job=",t2-t1)


#use threading

# print("program started with")
# import time
# import os
# import threading
# print("program started with=", threading.active_count())
# def fun1():
#     print("********fun1 started*********")
#     print(os.getpid())
#     print(threading.current_thread().name)
#     for i in range(5):
#         time.sleep(1)
#         print("working on fun1")
#     print("********fun1 completed*********")

# def fun2():
#     print("********fun2 started*********")
#     print(os.getpid())
#     print(threading.current_thread().name)
#     for i in range(5):
#         time.sleep(1)
#         print("working on fun2")
#     print("********fun2 completed*********")

# t1=time.time()
# thr1 = threading.Thread(target=fun1, name="thread1")
# thr2 = threading.Thread(target=fun2, name="thread2")
# thr1.start()
# thr2.start()
# print(threading.active_count())
# print(os.getpid())
# print(threading.current_thread())
# # fun1()
# # fun2()
# t2=time.time()
# print("time taken to complete the job=",t2-t1)



## To check whether threading is started, running and stopped. To check that 

import threading
print("program started with=", threading.active_count())
def fun1():
    print("********fun1 started*********")
    print(thr1.is_alive())
    print(threading.current_thread().name)
    for i in range(5):
        print("working on fun1")
    print("********fun1 completed*********")
    print(thr1.is_alive())


def fun2():
    print("********fun2 started*********")
    print(thr2.is_alive())
    print(threading.current_thread().name)
    for i in range(5):
        print("working on fun2")
    print("********fun2 completed*********")
    print(thr2.is_alive())

thr1 = threading.Thread(target=fun1, name="thread1")
thr2 = threading.Thread(target=fun2, name="thread2")
thr1.start()
thr2.start()
print(threading.active_count())
print(threading.current_thread())
print(thr1.is_alive())
print(thr2.is_alive())