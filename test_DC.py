import unittest
import dcV3

class testDependencyComparion(unittest.TestCase):

    def test_RequirementValid(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementAllValid.txt'),
        ['numpy is valid','SQLAlchemy is valid','MarkupSafe is valid','six is valid'
        ,'pypiwin32 is valid','soupsieve is valid','certifi is valid'])
    
    def test_RequirementInvalid(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementAllInvalid.txt'),
        ['numpy is Invalid','SQLAlchemy is Invalid','MarkupSafe is Invalid','six is Invalid'
         ,'pypiwin32 is Invalid','soupsieve is Invalid','certifi is Invalid'])
    
    def test_RequirementDoesntExist(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementDoesntExist.txt'),
        ["test doesn't exist in localPackages","IMDA doesn't exist in localPackages",])
    
    def test_RequirementInvalidSymbol(self):
        self.assertEqual(dcV3.comparisonPackage('sampleRequirementforTestDC/requirementInvalidSymbol.txt'),
        ["numpy+1.23.4 Invalid Symbol","six+1.23.5,< 1.23.10 Invalid Symbol",])

if __name__ == '__main__':
    unittest.main()
