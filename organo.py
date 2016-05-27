import os
from shutil import copyfile

def isSystemFile(name):
	"""
	Function to determine whether a file is a system file or not.
	@param name: the name of the file.
	@return isSystemFile: the boolean value whether the file is a system file or not.
	"""
	return name[0] == '.'


def getRelativePath(path, src):
	"""
	Gets the relative path of the path from the src.
	@param path: the absolute path whose relative path is to be found.
	@param src: the source directory from which the relative path is to be found.
	@return relativePath: the relative path.
	"""
	commonPath = os.path.commonprefix([path,src])
	relativePath = os.path.relpath(path, commonPath)
	if relativePath == '.':
		relativePath = ''
	return relativePath

def copyFiles(src, dst, maintainHierarchy):
	"""
	This function copies all the files in the src and its subfolders to the specified destination
	@param src: the source directory from where the files will be copied
	@param dst: the destination folder where the files will be copied
	@param maintainHierarchy: the boolean value whether or not to maintain the directory structure 
	                          in the destination folder
	"""
	for path, subdirs, files in os.walk(src):
		for name in files:
			if not isSystemFile(name):
				destination = dst
				if maintainHierarchy:
					destination = os.path.join(destination, getRelativePath(path, src))
				if not os.path.exists(destination):
					os.mkdir(destination)
				destination = os.path.join(destination,name)
				print('\n Copying file\n\tfrom: '+path + name +'\n\tto: '+ destination)
				copyfile(os.path.join(path, name), destination)



if __name__ == '__main__':

	maintainHierarchy = raw_input('\nDo you want to maintain the directory structure?\nEnter yes to confirm.\n-->')
	
	if maintainHierarchy == 'yes' or maintainHierarchy == 'Yes':
		maintainHierarchy = True
		print('\nThe directory structure will be maintained.')
	else:
		maintainHierarchy = False
		print('\nThe directory structure will not be maintained. Only the files will be copied to the destination.')


	src = raw_input('\nEnter the source directory \n(Leave blank to use current working directory)\n-->')
	if not src:
		src = os.getcwd()
	print('\nUsing ' + src + ' as the source')
	
	dst = raw_input('\nEnter the destination directory\n-->')

	if dst:
		copyFiles(src, dst, maintainHierarchy)
	else:
		print('\nDestination not specified. Exiting now.')