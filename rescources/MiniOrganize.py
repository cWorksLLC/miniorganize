import os
import shutil
import time

path = input("where do you want to sort the files? [INCLUDE THE FULL PATH]")

list_ = os.listdir(path)

for file_ in list_: 
	name, ext = os.path.splitext(file_)

	ext = ext[1:]

	if ext == '': 
		continue

	if os.path.exists(path+'/'+ext): 
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
	else: 
		os.makedirs(path+'/'+ext) 
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)

print("if you see this, the process was done sucessfully. closing in 2 seconds.")
time.sleep(2)