#!/usr/bin/env python3
import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
<<<<<<< HEAD
    # just added and remove one (1)
    free = (du.free / du.total * 100) -1 + 1
=======
    free = (du.free / du.total * 100) - 1 + 1
>>>>>>> 85a3098cabec0e905fa7ca77f9520b0915b285fc
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_cpu_usage() or not check_disk_usage('/'):
    print('ERROR! CPU usage is hight')
else:
    print('Everything is OK.')
