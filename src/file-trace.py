#coding=utf-8
import os

def getFileTraceByDir(fileDir):
    fileDirs = []
    for root,dirs,files in os.walk(fileDir):
        fileDirs.extend(getFileTraceByRoot(files, root))
    return fileDirs

def getFileTraceByRoot(fileNames, root):
    fileDirs = []
    for name in fileNames:
        fileDirs.append(root + "/" + name)
    return fileDirs
    
files = getFileTraceByDir("/Users/tzduan/AndroidStudioProjects/SuperCalculator/app/src/main/java/")

print(files)