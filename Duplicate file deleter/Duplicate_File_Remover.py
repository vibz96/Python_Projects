from sys import *
import os
import hashlib

def CalculateChecksum(path,blocksize = 1024):
	fd = open(path,'rb')#rb=read binary
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer)>0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()#returning heaxdecimal string


def DirectoryTraversal(path):
	print("Contents of the directory are")

	duplicate = {}	#Dictonary to hold checksum and file name

	for Folder,Subfolder,Filename in os.walk(path):
		print("Directory name is : "+Folder)
		for sub in Subfolder:
			print("Subfolder of :"+Folder + " is " +sub)
		for file in Filename:
			print("File name is :"+file)
			actualpath = os.path.join(Folder,file)
			hash = CalculateChecksum(actualpath)
			print(hash)

			if hash in duplicate:				#that checksum is already present
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash] = [actualpath]

	return duplicate


def DisplayDuplicate(duplicate):

	output = list(filter(lambda x: len(x)>1,duplicate.values()))

	if(len(output)>0):
		print("there are duplicate files")
	else:
		print("There are no duplicate files")
		return

	print("List of duplicate files :")
	i = 0
	iCnt = 0
	for result in output:
		iCnt+=1
		for path in result:
			iCnt+=1
			if iCnt>=2:
				print("%s\n"%path)
				i+=1
				os.remove(path)

	print("Duplicate file deleted are :"i)
		

def main():
	print("Directrory Traversal Script")

	if(len(argv) != 2):
		print("Error : Invalid number of arguments\n")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("It is directory cleaner script\n")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Provide the absolute path for target directory\n")
		exit()

	arr = {}
	arr = DirectoryTraversal(argv[1])
	# print(arr)

	DisplayDuplicate(arr)

if __name__ == "__main__":
	main()