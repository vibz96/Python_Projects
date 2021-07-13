from sys import *
import os
import hashlib

def FolderCreation(Dir):
	parent_dir = "C:/Users/Vaibhav/Desktop/Classes/Logic Building 039/Programs/"
	path = os.path.join(parent_dir,Dir)
	os.mkdir(path)


	for Folder, Subfolder, Filename in os.walk(path):
		print("Directory name is : " + Folder)
		actualpath = os.path.join(Folder, Dir)

	fd = open(actualpath+".java","w")
	fd.write("import java.util.*;\n\nclass "+argv[1]+"\n{\n\t public static void main(String arg[])\n\t{\n\t\t//Logic\n\t}\n}")
	fd = open(actualpath+".java", "r")
	print(fd.read())
	fd.close()


def main():
	directory = argv[1]
	FolderCreation(directory)


if __name__ == "__main__":
    main()