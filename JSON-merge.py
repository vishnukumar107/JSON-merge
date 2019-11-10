import json
import os

#let the max file size be 1MB we can also modify according to our needs
maxFilesize=1024000

#function to load a JSON file in python 
def getJSON(findPathName):
    with open(findPathName,'r',encoding='utf-8') as fp:
        return json.load(fp)

#funcion to merge the JSON array
def mergefunc(m1,m2):
    m={}
    for i,k in m1.items():
        for j,l in m2.items():
            if(i==j):
                for x in l:
                    k.append(x)
    return m1

#main function
#m1 and m2 are variables to store dictionaries
def jsonmerge(folderPath,inputBaseName,outputBaseName,maxFilesize):
    filesize=0
    global outputFilecount
    outputFilecount+=1
    noOffiles=len(os.listdir(folderPath))
    inputCount=1
    path=folderPath+inputBaseName+str(inputCount)+'.json'
    m1=getJSON(path)
    filesize+=os.path.getsize(path)
    for i in range(1,noOffiles):
        inputCount+=1
        path=folderPath+inputBaseName+str(inputCount)+'.json'
        if os.path.exists(path):
            m2=getJSON(path)
            filesize+=os.path.getsize(path)
            if(filesize>maxFilesize):
                print("Max size of the file is reached")
                return m1
            else:
                m1=mergefunc(m1,m2)
    outputpath=folderPath+outputBaseName+str(outputFilecount)+'.json'
    with open(outputpath, "w") as outfile: 
        json.dump(m1, outfile,indent=2,ensure_ascii=False)

outputFilecount=0
#example inputs are given,change accordingly
folderName='data/'
inputbasename='data'
outputbasename='merge'
jsonmerge(folderName,inputbasename,outputbasename,maxFilesize)

#addional function
# jsonmerge(folderName,inputbasename,outputbasename,maxFilesize)



