#second program - secret message
import os

def rename_files():

#list all the files in the prank folder
	file_list = os.listdir("/home/karan/pydev/prank/")
	#print(file_list)
	saved_path = os.getcwd()
	print("current working directory is"+saved_path)
	os.chdir("/home/karan/pydev/prank")
#remove all the numbers in the begining of the file name
	for file_name in file_list:
		print("old name->"+file_name)
		print("new name->"+file_name.translate(None,"0123456789"))
		os.rename(file_name, file_name.translate( None, "0123456789"))


rename_files()