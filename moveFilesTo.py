# coding=utf-8
import json
import os
import sys
import shutil
import copy
import re



def mergeFileTo(filePath,fileName,targetDir):
	print filePath
	shutil.move(filePath,targetDir+'\\' + fileName)
	pass


g_suffixList = {'.wmv','.avi','.rmvb','.mp4','.mkv'}
def isSuffixMatch(fileName):
	global g_suffixList
	for sf in g_suffixList:
		if fileName.lower().endswith(sf):
			return True
			pass
		pass

	return False
	pass


def main():
	yourpath = ""

	# print os.path.abspath(os.path.join(yourpath, os.pardir))
	parentPath = os.getcwd()# os.path.abspath(os.path.join(yourpath, os.pardir))
	targetDir = parentPath + '\\Htarget'
	print targetDir


	dirList ={'ll','ebb','cc','mm','1.6','10.22','H','h2','h1','ju'}
	moveDirList = list()
	for s in dirList:
		s = parentPath  + s
		moveDirList.append(s)
		pass

	targetList = list()

	for root,dirs,files in os.walk(targetDir):
		for f in files:
			targetList.append(f)

	for dirPath in moveDirList:
		for root, dirs, files in os.walk(dirPath):
			for f in files:			
				filePath = os.path.join(root, f)
				if root == targetDir:
					continue
					pass

				if f in targetList:
					continue
					pass

				if not isSuffixMatch(f):
					continue
					pass
				try:
					mergeFileTo(filePath,f,targetDir)
				except Exception,e:
					print e
					print filePath + ' error'
					continue

if __name__ == '__main__':
  	main()