import os
import shutil

base = "./CorrectedLaySumTestSet2020/"
copybase = "./struct/"

for file_name in os.listdir(base):

	dir_name = file_name[0: (len(file_name) - 9)]
	
	exists = os.path.isdir(copybase + dir_name)
	print(exists)

	if exists:
		shutil.copyfile(base + file_name, copybase + dir_name + "/" + file_name)
	else:
		os.mkdir(copybase + dir_name)
		shutil.copyfile(base + file_name, copybase + dir_name + "/" + file_name)
	