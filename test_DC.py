import unittest
import dcV3
import pkg_resources; 

class mockObject:
    def __init__(self,project_name,version):
        self.project_name = project_name
        self.version = version


class testDependencyComparion(unittest.TestCase):
               
    def test_RequirementValidEqual(self):
        pkg_resources.working_set = [
            mockObject('numpy','1'),  #numpy== 1;numpy==2; 
            mockObject('numpy1','1.0'), #numpy1==1.0;
            mockObject('numpy2','1.0.0'), #numpy2==1.0.0;
            mockObject('numpy3','1.0.0.post1'), #numpy2==1.0.0;
            mockObject('numpy4','2022.10.11'),#numpy4==2022.10.11;
            mockObject('numpy5','1.0.0'), #numpy5==Abc
            mockObject('numpy11','1'), #numpy11==2
            mockObject('numpy12','1.9'), #numpy12==2.0
            mockObject('numpy13','1.9.9'), #numpy13==2.0.0
            mockObject('numpy21','3'), #    numpy21==2
            mockObject('numpy22','2.1'), #numpy22==2.0
            mockObject('numpy23','2.1.3'), #numpy23==2.0.0
            mockObject('numpy31','2.0'), #numpy31==2
            mockObject('numpy32','2.0.0'), #numpy32==2.0
            mockObject('numpy33','2')] #numpy33==2.0.0
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementEqualCases.txt'),
        ["numpy is supported",
        "numpy is not supported",
        "numpy1 is supported",
        "numpy2 is supported",
        "numpy3 is supported",
        "numpy4 is supported",
        "numpy5 is not supported",
        "numpy11 is not supported",
        "numpy12 is not supported",
        "numpy13 is not supported",
        "numpy21 is not supported",
        "numpy22 is not supported",
        "numpy23 is not supported",
        "numpy31 version mismatch with local package",
        "numpy32 version mismatch with local package",
        "numpy33 version mismatch with local package"])

    def test_RequirementValidMore(self):
        pkg_resources.working_set = [
            mockObject('numpy','2'),  #numpy> 1; 
            mockObject('numpy1','1.1'), #numpy1>1.0;
            mockObject('numpy2','1.0.1'), #numpy2>1.0.0;
            mockObject('numpy3','1.0.0.post1'), #numpy3>1.0.0.post1;
            mockObject('numpy4','2022.10.12'),#numpy4>2022.10.11;
            mockObject('numpy5','1.0.0'), #numpy5>Abc
            mockObject('numpy21','1'), #    numpy21>2
            mockObject('numpy22','1.8'), #numpy22>2.0 
            mockObject('numpy23','1.9.8'), #numpy23>2.0.0
            mockObject('numpy31','2.0'), #numpy31>2
            mockObject('numpy32','2.0.0'), #numpy32>2.0
            mockObject('numpy33','2')] #numpy33>2.0.0
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementMoreCases.txt'),
        ["numpy is supported",
        "numpy1 is supported",
        "numpy2 is supported",
        "numpy3 unable to determine",
        "numpy4 is supported",
        "numpy5 unable to determine",
        "numpy21 is not supported",
        "numpy22 is not supported",
        "numpy23 is not supported",
        "numpy31 version mismatch with local package",
        "numpy32 version mismatch with local package",
        "numpy33 version mismatch with local package"])

    def test_RequirementValidMinus(self):
        pkg_resources.working_set = [
            mockObject('numpy','1'),  #numpy< 2; 
            mockObject('numpy1','1.0'), #numpy1<1.1;
            mockObject('numpy2','1.0.0'), #numpy2<1.0.1;
            mockObject('numpy3','1.0.0.post1'), #numpy2<1.0.1.post1;
            mockObject('numpy4','2022.10.11'),#numpy4<2022.10.12;
            mockObject('numpy5','1.0.0'), #numpy5<Abc
            mockObject('numpy21','2'), #    numpy21<1
            mockObject('numpy22','1.9'), #numpy22<1.8 
            mockObject('numpy23','1.9.9'), #numpy23<1.9.8
            mockObject('numpy31','2.0'), #numpy31<2
            mockObject('numpy32','2.0.0'), #numpy32<2.0
            mockObject('numpy33','2')] #numpy33<2.0.0
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementMinusCases.txt'),
        ["numpy is supported",
        "numpy1 is supported",
        "numpy2 is supported",
        "numpy3 unable to determine",
        "numpy4 is supported",
        "numpy5 unable to determine",
        "numpy21 is not supported",
        "numpy22 is not supported",
        "numpy23 is not supported",
        "numpy31 version mismatch with local package",
        "numpy32 version mismatch with local package",
        "numpy33 version mismatch with local package"])
    
    def test_RequirementInvalid(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementAllInvalid.txt'),
        ['numpy is Invalid','SQLAlchemy is Invalid','MarkupSafe is Invalid','six is Invalid'
         ,'pypiwin32 is Invalid','soupsieve unable to determine','certifi is Invalid'])
    
    def test_RequirementDoesntExist(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementDoesntExist.txt'),
        ["test doesn't exist in localPackages","IMDA doesn't exist in localPackages",])
    
    def test_RequirementInvalidSymbol(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementInvalidSymbol.txt'),
        ["numpy+1.23.4 Invalid Symbol","six+1.23.5,< 1.23.10 Invalid Symbol",])

if __name__ == '__main__':
    unittest.main()
