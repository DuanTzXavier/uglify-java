#coding=utf-8
import re
import time

def protectString(matched,p,t):
    quotesText = matched
    matched = re.sub(p, t, matched)
    print(matched)
    print(quotesText)
    return all_the_text.replace("\""+ quotesText + "\"", "\""+ matched + "\"")

f = open("2.java", "r")
newFile = open("1-min.java", "w+")
time1 = time.time()
try:
    all_the_text = f.read()
    #去除注释块
    all_the_text = re.sub(r'\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/', "", all_the_text)

    #替换引号中的注释

    pattern=re.compile(r'"(.*?)"')
    allMatched = re.findall(pattern, all_the_text)
    if allMatched:
        pattern=re.compile(r'//')
        for matched in allMatched:
            all_the_text = protectString(matched, pattern, "/*")
            pass
    else:
        print 'not search'


    #去除注释行
    all_the_text = re.sub(r'\/\/[^\n]*', "", all_the_text)

    if allMatched:
        pattern=re.compile(r'\s')
        for matched in allMatched:
            all_the_text = protectString(matched, pattern, "//")
            pass
    else:
        print 'not search'

    #换成单一空格
    all_the_text = re.sub(r'\s+', " ", all_the_text)
    #字母间的空格替换
    all_the_text = re.sub(r'\b\s\b', "//", all_the_text)
    #去除空格
    all_the_text = re.sub(r'\s', "", all_the_text)
    #还原空格
    all_the_text = re.sub(r'\/\/', " ", all_the_text)
    #还原引号中的//
    all_the_text = re.sub(r'\/\*', "//", all_the_text)
    newFile.write(all_the_text)
finally:
    newFile.close()
    f.close()
print(time.time()-time1)
