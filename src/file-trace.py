#coding=utf-8
import os

def fileName(fileDir):
    for root,dirs,files in os.walk(fileDir):
        print("root: " + root)
        print("dirs: ")
        print(dirs)
        print("files: ")
        print(files)


fileName("/Users/tzduan/WorkSpace/Other/python/uglify-java/src")