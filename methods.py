import re

def contains_number(string):
    return any(char.isdigit() for char in string)

def getPackagesDetails(filename):
    returnNameVersionExpressions = []

    #Load requirement files.
    f = open(filename,'r')
    storage = f.read().replace(";","").split('\n')

    #Create a list to store the name, version and expressions
    returnNameVersionExpressions = [None] * len(storage)
    regex = r"[^(>=)|(<)|(==)|(~=)|(<=)|(>)|\w|\d\.\,\;\ ]"

    for idx,item in enumerate(storage):
        if not re.search(regex,item):
        #if('>=' in item or '>' in item or '<' in item or '~=' in item or '==' in item):
        #split the package name and version 
            nameVersion = re.split('<=|>=|>|<|~=|==|,.',item)
            print(nameVersion)
            #split the version into major,minor and patch
            index = 0
            while(index < len(nameVersion)):
                if re.match('[0-9]',nameVersion[index]):
                    majorminorpatch = re.split('\.',nameVersion[index])
                    for id,numbers in enumerate(majorminorpatch):
                        if re.match('[0-9]',str(numbers)):
                            majorminorpatch[id] = int(numbers)
                    nameVersion[index] = majorminorpatch        
                index += 1
            returnNameVersionExpressions[idx]= nameVersion   
        #identify the expressions
            if ">=" in item:
                returnNameVersionExpressions[idx].append("moreThanEqualTo")
            elif ">" in item:
                returnNameVersionExpressions[idx].append("more")
            if "~=" in item:
                returnNameVersionExpressions[idx].append("tildeEqual")
            if "<=" in item:
                returnNameVersionExpressions[idx].append("lessThanEqualTo") 
            elif "<" in item:
                returnNameVersionExpressions[idx].append("less")
            if "==" in item:
                returnNameVersionExpressions[idx].append("equal")
        else:
            returnNameVersionExpressions[idx] = [item,"invalidSymbol"]

    print('i am here')
    print(returnNameVersionExpressions)
    print('i am here 2')
    return returnNameVersionExpressions

def findIndex(stringArr, keyString):
    for index,item in enumerate(stringArr):
        if keyString in item:
            return index