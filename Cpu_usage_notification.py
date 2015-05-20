__author__ = 'Shivasankar G Sambandam'


import os
from shutil import make_archive
import psutil
import pynotify
import sched
import time

tim_calc = sched.scheduler(time.time, time.sleep)


def cpu_usage_calculator(sec):
    dictval = {}
    cpu_usage = psutil.cpu_percent()
    cpu_usage_times = psutil.cpu_times()
    cpu_usage_percent = psutil.cpu_times_percent(interval=1, percpu=False)
    cpu_usage_count = psutil.cpu_count()
    cpu_virtual_memory = psutil.virtual_memory()
    cpu_swap_memory = psutil.swap_memory()
    cpu_avail_memory = psutil.avail_phymem()
    cpu_avail_virtual_memory = psutil.avail_virtmem()
    users = psutil.users()
    print 'CPU Memory :', cpu_avail_memory,'\nVirturl Memory:', cpu_avail_virtual_memory, '\nswap Memory:', cpu_swap_memory,'\nCPU Usage:', cpu_usage, '\nCPU Usage Count:', cpu_usage_count, '\nCPU Usage Percentage', cpu_usage_percent,'\nCPU Cycle times:', cpu_usage_times, '\nCPU virtual Memory', cpu_virtual_memory
    dictval = {'CPU Memory ': cpu_avail_memory,'Virturl Memory': cpu_avail_virtual_memory, 'swap Memory:': cpu_swap_memory,'CPU Usage:': cpu_usage, 'CPU Usage Count:': cpu_usage_count, 'CPU Usage Percentage': cpu_usage_percent,'CPU Cycle times:': cpu_usage_times, 'CPU virtual Memory': cpu_virtual_memory}
    pynotify.init('Basic')
    Notify = pynotify.Notification('CPU Information', str(dictval))
    Notify.show()
    sec.enter(30, 1, cpu_usage_calculator, (sec,))

tim_calc.enter(30, 1, cpu_usage_calculator, (tim_calc,))
tim_calc.run()
