# def fun(x,y):
#     print(f"x={x},y={y}")
#     res = x/y

# res = fun(100,20)
# print("result=",res)
#***
## To know how many processes/threads are running to execute by :
## python, import os, print(dir(os)), os.getpid
## to know how many threads---> python, import threading, print(dir(threading))--->active_count(no of active threads)

#os.system() used to run commands in python; Ex- os.system("mkdir sample") , os.system("removedirs sample")

#***
# import os
# def fun(x,y):
#     print(f"x={x},y={y}")
#     print(os.getpid())
#     res = x/y

# print(os.getpid())
# res = fun(100,20)
# print("result=",res)

#***


"""
to get the max salary of employee table---> having 20L records, which is bearing more pressure CPU,RAM.. Answer is both [[[CPU BOUND JOB]]]
multi_processing method
request to rds instance ---> to get 20 records from department table..

You are in INDIA.. accessing from US-WEST-2 .... network [[[MEMORY/DATA/STORAGE/NETWORK/OUTSIDE BOUND JOB]]]
Task: remote server: /department(it takes 2 sec), /employee_salary(3), /emp_address(4)..... total time 9 secs
process--- thr1, thr2, thr3,....

thr1(/department(it takes 2 sec))--> while working/doing thr1 execution it will raise a request to thr2
thr2(/employee_salary(3))
thr3(/emp_address(4))
So here total time taken is 4 secs
"""
import os
import threading
def fun(x,y):
    print(f"x={x},y={y}")
    print(os.getpid())
    print(threading.current_thread())
    res = x/y

print(os.getpid())
print(threading.active_count())
print(threading.current_thread())
res = fun(100,20)
print("result=",res)