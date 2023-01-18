import re
import methods
import pkg_resources; 

def comparisonPackage(requirementTextfileName):
    returnMessage = []
    localPackages = [(e.project_name, e.version) for e in pkg_resources.working_set]
    localPackages = [list(x) for x in localPackages]

    for idx,package in enumerate(localPackages):
        majorminorpatch = re.split('\.',package[1])
        for index,item in enumerate(majorminorpatch):
            if re.match('[0-9]',str(item)):
                majorminorpatch[index] = int(item)
        localPackages[idx][1] = majorminorpatch

    incomingPackages = methods.getPackagesDetails(requirementTextfileName)

    for package in incomingPackages:
        print(package)
        validOrInvalid = False
        #if package name exsists in the localPackages then continue
        if any(package[0] in x for x in localPackages):
            index =methods.findIndex(localPackages,package[0])
            if(len(package) == 3 and len(localPackages[index][1]) == len(package[1])):
                    if "more" in package or "moreThanEqualTo" in package:
                        for id,item in enumerate(package[1]):
                            if  not re.match('[0-9]',str(item)) or not re.match('[0-9]',str(localPackages[index][1][id])):
                                validOrInvalid = 'UD' #Unable to determined
                            else:
                                if item < localPackages[index][1][id]:
                                    validOrInvalid = True
                                else:
                                    if item != localPackages[index][1][id]:
                                        break
                    if "less" in package or "lessThanEqualTo" in package:
                        for id,item in enumerate(package[1]):
                            if  not re.match('[0-9]',str(item)) or not re.match('[0-9]',str(localPackages[index][1][id])):
                                validOrInvalid = 'UD' #Unable to determined
                            else:
                                if item > localPackages[index][1][id]:
                                    validOrInvalid = True
                                else:
                                    if item != localPackages[index][1][id]:
                                        break
                    if "tildeEqual" in package:
                        for id,item in enumerate(package[1]):
                            if  not re.match('[0-9]',str(item)) or not re.match('[0-9]',str(localPackages[index][1][id])):
                                validOrInvalid = 'UD' #Unable to determined
                            else:
                                if id == len(package[1])-1:
                                    if package[1][id] <= localPackages[index][1][id]:
                                        validOrInvalid = True
                                else:
                                    if item == localPackages[index][1][id]:
                                        pass
                                    else:
                                        break
                    if "equal" in package or "moreThanEqualTo" in package or "lessThanEqualTo" in package or "tildeEqual" in package:
                        listofCheck = []
                        for id,item in enumerate(package[1]):
                            if item == localPackages[index][1][id]:
                                listofCheck.append(True)
                            else:
                                listofCheck.append(False)
                        if all(listofCheck):
                            validOrInvalid = True
            elif(len(package) == 5 and len(localPackages[index][1]) == len(package[1]) and len(localPackages[index][1]) == len(package[2])):
                firstCheck = False; #Check if the condition satisfies the first condition
                secondCheck = False; #Check if the condition satisfies the first condition
                if "more" and "less" in package or "moreThanEqualTo" and "less" in package or "lessThanEqualTo" and "more" in package or "moreThanEqualTo" in package or "lessThanEqualTo" in package:
                    for id,item in enumerate(package[1]): 
                        if  not re.match('[0-9]',str(item)) or not re.match('[0-9]',str(localPackages[index][1][id])):
                                validOrInvalid = 'UD' #Unable to determined
                        else:
                            if item < localPackages[index][1][id]:
                                firstCheck = True
                    for id,item in enumerate(package[2]):
                        if  not re.match('[0-9]',str(item)) or not re.match('[0-9]',str(localPackages[index][1][id])):
                                validOrInvalid = 'UD' #Unable to determined
                        else:
                            if item > localPackages[index][1][id]:
                                secondCheck = True
                
                if "moreThanEqualTo" in package:
                    listofCheck = []
                    for id,item in enumerate(package[1]):
                        if item == localPackages[index][1][id]:
                            listofCheck.append(True)
                        else:
                            listofCheck.append(False)
                    if all(listofCheck):
                        firstCheck = True
                
                if "lessThanEqualTo" in package:
                    listofCheck = []
                    for id,item in enumerate(package[2]):
                        if item == localPackages[index][1][id]:
                            listofCheck.append(True)
                        else:
                            listofCheck.append(False)
                    if all(listofCheck):
                        secondCheck = True

                if(firstCheck == True and secondCheck == True):
                    validOrInvalid = True
            else:
                if len(package) == 3:
                    if len(localPackages[index][1]) != len(package[1]):
                        validOrInvalid = 'VM'
                if len(package) == 5:
                    if len(localPackages[index][1]) != len(package[1]) or len(localPackages[index][1]) != len(package[2]) :
                        validOrInvalid = 'VM'
                    if len(package[1]) != len(package[2]):
                        validOrInvalid = 'RUD'   
                        
            if(validOrInvalid == True):
                returnMessage.append(package[0] + " is supported")
            elif(validOrInvalid == 'UD'):
                returnMessage.append(package[0] + " unable to determine")
            elif(validOrInvalid == 'VM'):
                returnMessage.append(package[0] + " version mismatch with local package")
            elif(validOrInvalid == 'RUD'):
                returnMessage.append(package[0] + " unable to determine the requirement")        
            else:
                returnMessage.append(package[0] + " is not supported")
        else:
            if("invalidSymbol"in package):
                returnMessage.append(package[0] + " Invalid Symbol")
            else:
                returnMessage.append(package[0] + " doesn't exist in localPackages")

    return returnMessage

#write few test cases 
#postive test case
#negative test case
#unit test case
#not able to handle correctly, gather them spefic we are not able to give an answer
#it should be handle by identify such cases and tell the user we are not able to determine.
#Check on calendar based versioning requirement.txt use range symbol

#handle jest test case
#detect ; colon in the
#check against host environment
#modified the major and minor and patch
#sudo code 
#async-timeout==4.0.2 ; 
#python_version >= "3.10" and python_version < "4.0"
#attrs==22.1.0 ; 
#python_version >= "3.10" and python_version < "4.0"
#jsonschema==4.17.1 ; python_version >= "3.10" and python_version < "4.0"
#numpy==1.23.5 ; python_version >= "3.10" and python_version < "4.0"
#packaging==21.3 ; python_version >= "3.10" and python_version < "4.0"
#pyparsing==3.0.9 ; python_version >= "3.10" and python_version < "4.0"
#pyrsistent==0.19.2 ; python_version >= "3.10" and python_version < "4.0"

#add
#the first thing list to have in local environment,and look into requirement.txt
#check against the list of local environment