import unittest
import dcV3
import pkg_resources; 

class mockObject:
    def __init__(self,project_name,version):
        self.project_name = project_name
        self.version = version


class testDependencyComparion(unittest.TestCase):
               
    def test_RequirementEqualSymbol(self):
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

    def test_RequirementMoreSymbol(self):
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

    def test_RequirementMinusSymbol(self):
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
  
    def test_RequirementTidleEqualSymbol(self):
        pkg_resources.working_set = [
            mockObject('numpy','1'), #numpy ~=1
            mockObject('numpy1','1.1'), #numpy1 ~=1.0
            mockObject('numpy2','1.0.1'), #numpy2 ~=1.0.0
            mockObject('numpy3','1.0.1'), #numpy3 ~=1.0.0
            mockObject('numpy4','1.1.1'), #numpy4 ~=1.0.1
            mockObject('numpy5','1.0.8'), #numpy5 ~=1.0.1
            mockObject('numpy6','1.0.0.post1'), #numpy6 ~= 1.0.0.post1
            mockObject('numpy7','1.0.0.post2'), #numpy7 ~= 1.0.0.post1
            mockObject('numpy8','1.0.0'), #numpy8 ~= abc
            mockObject('numpy9','2.0'), #numpy31<2
            mockObject('numpy10','2.0.0'), #numpy32<2.0
            mockObject('numpy11','2') #numpy33<2.0.0
            ] 
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementTildeEqualCases.txt'),
        ["numpy is supported",
        "numpy1 is supported",
        "numpy2 is supported",
        "numpy3 is supported",
        "numpy4 is not supported",
        "numpy5 is supported",
        "numpy6 is supported",
        "numpy7 unable to determine",
        "numpy8 unable to determine",
        "numpy9 version mismatch with local package",
        "numpy10 version mismatch with local package",
        "numpy11 version mismatch with local package"])
    
    def test_RequirementMoreAndLessSymbols(self):
        pkg_resources.working_set = [
            mockObject('numpy','2'), #numpy>1<3
            mockObject('numpy1','1.5'), #numpy1>1.1<2.0
            mockObject('numpy2','1.5.1'), #numpy2>1.1.2<2.0.0;
            mockObject('numpy3','1.0.1.post1'), #numpy3>1.0.0.post1<2.0.0.post1
            mockObject('numpy4','2022.10.12'), #numpy4>2022.10.11<2022.11.11;
            mockObject('numpy5','1.5.1'), #numpy5>Abc
            mockObject('numpy6','2.0.9'), #numpy6>2.0.0<2.1
            mockObject('numpy7','1.9.9'), #numpy7>1.9<2.1.0
            mockObject('numpy8','1.9.9'), #numpy8>3<1
            mockObject('numpy9','1.9'), #numpy9>2.0<1.8
            mockObject('numpy10','1.9.9'), #numpy10>2.0.1<1.8.9
            mockObject('numpy11','2.0'), #numpy11>1<3
            mockObject('numpy12','1.9.9'), #numpy12>1.8<2.0
            mockObject('numpy13','2'), #numpy13>1.8.9<2.0.1

            ] 
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementMoreAndLessCases.txt'),
        ["numpy is supported",
        "numpy1 is supported",
        "numpy2 is supported",
        "numpy3 is supported",
        "numpy4 is supported",
        "numpy5 unable to determine",
        "numpy6 unable to determine the requirement",
        "numpy7 unable to determine the requirement",
        "numpy8 version mismatch with local package",
        "numpy9 is not supported",
        "numpy10 is not supported",
        "numpy11 version mismatch with local package",
        "numpy12 version mismatch with local package",
        "numpy13 version mismatch with local package",])
    
    def test_RequirementDoesntExist(self):
        pkg_resources.working_set = [
            mockObject('numpy','1'),  #numpy< 2; 
            mockObject('numpy1','1.0'), #numpy1<1.1;
        ]
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementDoesntExist.txt'),
        ["test doesn't exist in localPackages","IMDA doesn't exist in localPackages",])
    
    def test_RequirementInvalidSymbol(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementInvalidSymbol.txt'),
        ["numpy+1.23.4 Invalid Symbol","six+1.23.5,<1.23.10 Invalid Symbol",])

if __name__ == '__main__':
    unittest.main()
