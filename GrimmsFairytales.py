import string
import re

grimms = open("grimms.txt","r")
stopwords = open("stopwords.txt", "r")
lnum = 0
mydict = {}
current_title = ''
ListOfStopwords = []

def Stopwords(stopwords):
    for line in stopwords:
        thisline = line.strip(string.punctuation + string.whitespace)
        thisline = re.sub(r'[^a-zA-Z0-9 ]','',thisline)
        for word in thisline.split():
            ListOfStopwords.append(word)

Stopwords(stopwords)

for line in grimms:
    lnum = lnum + 1
    if 9204 >= lnum >= 124:
        match = re.search(r'^[A-Z -\[\]0-9\.]+$', line)
        if match:
            current_title = line
        else:
            aline = line.strip(string.punctuation + string.whitespace)
            aline = re.sub(r'[^a-zA-Z0-9 ]','',aline)
            for word in aline.split():
                if word not in ListOfStopwords:
                    word.lower()
                    mydict.setdefault(word,{}).setdefault(current_title,[]).append(lnum)


def onewordquery(newq):
    if newq in mydict:
        newdict = mydict[newq]
        lineholder = 0
        for (k,v) in newdict.items():
            holder2 = 0
            for lineholder in v:
                if holder2 == 0:
                    print()
                    print(k)
                    holder2 += 1
                print(lineholder, linetext[lineholder-1].replace(newq,"**"+ newq.upper() +"**"))
    else:
        print('--')

def orquery(q1,q3):
        if q1 in mydict:
            print('Results for: ' +q1)
            print(onewordquery(q1))
        if q3 in mydict:
            print('Results for: ' +q3)
            print(onewordquery(q3))


def shortandquery(q1,q3):
        if q1 in mydict:
            newanddict = mydict[q1]
            set1 = set()
            for (k,v) in newanddict.items():
                set1.add(k)
        if q3 in mydict:
            newanddict2 = mydict[q3]
            set2 = set()
            for (k, v) in newanddict2.items():
                set2.add(k)
        set3 = set1.intersection(set2)
        andList = list(set3)
        i = 0
        if len(andList) != 0:
            while i < len(andList):
                andlineholder = 0
                for (k,v) in newanddict.items():
                    andholder = 0
                    if k == andList[i]:
                        for andlineholder in v:
                            if andholder == 0:
                                print() #Empty line for aesthetic purposes
                                print(k)
                                print(q1)
                                print() #Empty line for aesthetic purposes
                                andholder += 1
                            print(andlineholder, linetext[andlineholder - 1].replace(q1, "**" + q1.upper() + "**"))
                for (k,v) in newanddict2.items():
                    andholder2 = 0
                    if k == andList[i]:
                        for andlineholder in v:
                            if andholder2 == 0:
                                print() #Empty line for aesthetic purposes
                                print(k)
                                print(q3)
                                print() #Empty line for aesthetic purposes
                                andholder2 += 1
                            print(andlineholder, linetext[andlineholder - 1].replace(q3, "**" + q3.upper() + "**"))
                i = i+1

        else:
            print('--')

def mediumandquery(q1,q2,q3):
        if q1 in mydict:
            newanddict = mydict[q1]
            set1 = set()
            for (k,v) in newanddict.items():
                set1.add(k)
        if q2 in mydict:
            newanddict2 = mydict[q2]
            set2 = set()
            for (k, v) in newanddict2.items():
                set2.add(k)
        if q3 in mydict:
            newanddict3 = mydict[q3]
            set3 = set()
            for (k, v) in newanddict3.items():
                set3.add(k)
        set4 = set1.intersection(set2)
        set5 = set3.intersection(set4)
        andList = list(set5)
        i = 0
        if len(andList) != 0:
            while i < len(andList):
                andlineholder = 0
                for (k,v) in newanddict.items():
                    andholder = 0
                    if k == andList[i]:
                        for andlineholder in v:
                            if andholder == 0:
                                print() #Empty line for aesthetic purposes
                                print(k)
                                print(q1)
                                print() #Empty line for aesthetic purposes
                                andholder += 1
                            print(andlineholder, linetext[andlineholder - 1].replace(q1, "**" + q1.upper() + "**"))
                for (k,v) in newanddict2.items():
                    andholder2 = 0
                    if k == andList[i]:
                        for andlineholder in v:
                            if andholder2 == 0:
                                print() #Empty line for aesthetic purposes
                                print(k)
                                print(q2)
                                print() #Empty line for aesthetic purposes
                                andholder2 += 1
                            print(andlineholder, linetext[andlineholder - 1].replace(q2, "**" + q2.upper() + "**"))
                for (k,v) in newanddict3.items():
                    andholder3 = 0
                    if k == andList[i]:
                        for andlineholder in v:
                            if andholder3 == 0:
                                print() #Empty line for aesthetic purposes
                                print(k)
                                print(q3)
                                print() #Empty line for aesthetic purposes
                                andholder3 += 1
                            print(andlineholder, linetext[andlineholder - 1].replace(q3, "**" + q3.upper() + "**"))
                i = i+1

        else:
            print('--')


boo1 = True
linetext = []
myfile = open("grimms.txt", "r")

for aline in myfile:
    aline = aline.strip()
    linetext.append(aline)

print("Welcome to the Grimms' Fairy Tales search system!")
print() #Empty line for aesthetic purposes
print('To stop the query, please enter: "qquit".')
print() #Empty line for aesthetic purposes

while boo1:
    q = input('Please enter your query: ')
    q.strip()
    newq = q.lower()
    
    if q == 'qquit':
        print("Now exiting the Grimms' Fairy Tales search system.")
        break
    else:
        print() #Empty line for aesthetic purposes
        print('Query = ' + newq)
    qs = newq.split()
    if len(qs) == 1:
        if newq in ListOfStopwords:
            print('This search system does not support your query because it is a "stopword".')
        else:
            print(onewordquery(newq))
    elif len(qs) == 2:
        q1 = qs[0]
        q3 = qs[1]
        print(shortandquery(q1,q3))
    elif len(qs) == 3:
        if qs[1] == 'and':
            q1 = qs[0]
            q3 = qs[2]
            print(shortandquery(q1,q3))
        elif qs[1] == 'or':
            q1 = qs[0]
            q3 = qs[2]
            print(orquery(q1,q3))
        else:
            q1 = qs[0]
            q2 = qs[1]
            q3 = qs[2]
            print(mediumandquery(q1,q2,q3))
    else:
        print('This sort of query is not supported.')