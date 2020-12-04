#!/usr/bin/env python3
import os
import sys
import shutil

def check_reboot():
	"""Returns True if the computer has a reboot command pending"""
	return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
	"""Returns True if there is not enough disk, False otherwise"""
	du = shutil.disk_usage(disk)
	# calculate the percentage of free space
	percent_free = 100 * du.free / du.total

	# calculate how many Gbs are percent_free
	gigabyte_free = du.free / 2**30
	if gigabyte_free < min_gb or percent_free < min_percent:
		return True
	return False

def chek_root_full():
	"""Returns True if root partition is full, False otherwise"""
	return check_disk_usage(disk='/', min_gb=2, min_percent=10)


def main():
	if check_reboot():
		print('Pending Reboot')
		sys.exit(1)
	if chek_root_full():
		print("root partition is full")
		sys.exit(1)
	print("Everything ok")
	sys.exit(0)
main()
