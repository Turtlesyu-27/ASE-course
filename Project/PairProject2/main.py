import sys
import os
import re
import time
import threading

def replaceVerb(words, verbFile):
    d={}
    verbs=open(verbFile, 'r', encoding='utf-8').read()
    lines=verbs.split('\n')[0:-1]
    for line in lines:
        origin=line.split('->')
        chgs=origin[1]
        origin=origin[0].strip()
        chgs=chgs.split(',')
        for chg in chgs:
            chg=chg.strip()
            d[chg]=origin
    for i in range(len(words)):
        if(words[i] in d):
            words[i]=d[words[i]]

def charCount(words, path):
    print("File: %s"%(path))
    chrs='abcdefghijklmnopqrstuvwxyz'
    chrs+=str.upper(chrs)
    d={}
    for c in chrs:
        d[c]=0
    cnt=0
    for word in words:
        for c in word:
            if c in d:
                d[c]+=1
                cnt+=1
    l=sorted(d.items(), key = lambda x:x[1], reverse=True)
    if('n' not in ops):
        for e in l:
            print("%40s\t%f"%(e[0], round(100*e[1]/cnt, 2)))
            #print('%s %.2f%%'%(e[0], round(100*e[1]/cnt, 2)))
    else:
        for i, e in enumerate(l):
            if(i<int(ops['n'])):
                print("%40s\t%f"%(e[0], round(100*e[1]/cnt, 2)))

def phraseCount(words, path):
    num_words=int(ops['p'])
    print("File: %s"%(path))
    chrs='abcdefghijklmnopqrstuvwxyz'
    d_c={}
    for i, c in enumerate(chrs):
        d_c[c]=chrs[len(chrs)-i-1]

    d={}
    #words=re.findall(r'[a-zA-Z][a-zA-Z0-9]*|[,\'.-]', content)
    buffer=[]
    cnt=0
    separators=['.', '-', ',', '\'']
    for word in words:
        if(word in separators):
            buffer=[]
            cnt=0
        else:
            buffer.append(word)
            cnt+=1
            if(cnt==num_words):
                res=buffer[0]+' '
                for i in range(1, cnt):
                    res+=(buffer[i]+' ')
                if(res in d):
                    d[res]+=1
                else:
                    d[res]=1
                buffer=buffer[1:]
                cnt-=1
    l=sorted(d.items(), key = lambda x:(x[1], d_c[x[0][0]]), reverse=True)
    if('n' not in ops):
        for e in l:
            print("%40s\t%d"%(e[0], int(e[1])))
            #print('%s %.2f%%'%(e[0], round(100*e[1]/cnt, 2)))
    else:
        for i, e in enumerate(l):
            if(i<int(ops['n'])):
                print("%40s\t%d"%(e[0], int(e[1])))

def stopWord(words, stopfile):
    stop=open(stopfile, 'r', encoding='utf-8').read()
    stops=set(stop.split('\n')[0:-1])
    res=[]
    for word in words:
        if(word not in stops):
            res.append(word)
    return res

start = time.clock()
##get operations from command
##if -v file in command, then ops['v']=file
argv=sys.argv[1:]
ops={}
stk_op=[]
stk=[]
for arg in argv:
    if('-' in arg and len(arg)==2):
        stk_op.append(arg)
    else:
        stk.append(arg)
for i in range(len(stk_op)):
    ops[stk_op[i][1]]=stk[i]

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):

if('c' in ops):  ##choose to char count
    content=str.lower(open(ops['c'], 'r', encoding='utf-8').read()) ##turn content into lower case
    words=re.findall(r'[a-zA-Z][a-zA-Z0-9\']*|[,.-]', content) ##get all words and separaters use regular expression
    if('x' in ops):  ##delete stop words
        words=stopWord(words, ops['x'])
    if('v' in ops):  ##replace verb
        replaceVerb(words, ops['v'])
    charCount(words, ops['c'])
if('f' in ops): ##choose to count phrase, word count is length 1 phrase count
    if('p' not in ops): ##length of phrase
        ops['p']=1
    content=str.lower(open(ops['f'], 'r', encoding='utf-8').read())  ##turn content into lower case
    words=re.findall(r'[a-zA-Z][a-zA-Z0-9\']*|[,.-]', content)  ##get all words and separaters use regular expression
    if('x' in ops): ##delete stop words
        words=stopWord(words, ops['x'])
    if('v' in ops): ##replace verb
        replaceVerb(words, ops['v'])
    phraseCount(words, ops['f'])
if('d' in ops): ##repeat the operation 'f' for each file in dict 
    for f in os.listdir(ops['d']):
        f=ops['d']+'\\'+f ##file path
        ##rest is same with operation 'f'
        content=str.lower(open(f, 'r', encoding='utf-8').read())
        words=re.findall(r'[a-zA-Z][a-zA-Z0-9\']*|[,.-]', content)
        if('x' in ops):
            words=stopWord(words, ops['x'])
        if('v' in ops):
            replaceVerb(words, ops['v'])
        phraseCount(words, f)

# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

end = time.clock()

print("Total runtime is:",str(end-start))

