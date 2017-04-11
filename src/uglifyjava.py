#coding=utf-8
import re
import time
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

def protectString(matched, p, t, text):
    quotesText = matched
    matched = re.sub(p, t, matched)
    print(matched)
    print(quotesText)
    return text.replace("\""+ quotesText + "\"", "\""+ matched + "\"")

def replaceSlash(pattern, allText):
    allMatched = re.findall(pattern, allText)
    if allMatched:
            #替换引号中的双斜杠
            pattern2=re.compile(r'//')
            for matched in allMatched:
                allText = protectString(matched, pattern2, "/*")
            #替换引号中的空格
            pattern=re.compile(r'\s')
            for matched in allMatched:
                allText = protectString(matched, pattern, "//")
    else:
        print '没有找到引号'
    return allText

def uglifyJava(filename):
    f = open(filename, "r")
    fn = open(filename + "a", "w+")
    try:
        allText = f.read()
        #去除注释块
        allText = re.sub(r'\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/', "", allText)
        #替换引号中的//
        patternQ = re.compile(r'"(.*?)"')
        patternQ2 = re.compile(r'\'(.*?)\'')
        allText = replaceSlash(patternQ, allText)
        allText = replaceSlash(patternQ2, allText)
        #去除注释行
        allText = re.sub(r'\/\/[^\n]*', "", allText)
        #换成单一空格
        allText = re.sub(r'\s+', " ", allText)
        #字母间的空格替换
        allText = re.sub(r'\b\s\b', "//", allText)
        #去除空格
        allText = re.sub(r'\s', "", allText)
        #还原空格
        allText = re.sub(r'\/\/', " ", allText)
        #还原引号中的//
        allText = re.sub(r'\/\*', "//", allText)
        fn.write(allText)
    finally:
        f.close()
        fn.close()
    pass

startTime = time.time()
src = "/Users/tzduan/WorkSpace/Other/python/uglify-java/src/test"
files = getFileTraceByDir(src)
for fileName in files:
    uglifyJava(fileName)
totalTime = "丑化用时：" + str(time.time()-startTime)
print(totalTime)