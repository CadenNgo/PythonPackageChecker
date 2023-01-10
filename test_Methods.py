import unittest
import methods

class testUtilityMethods(unittest.TestCase):

    def test_FindIndexSucess(self):
        testList = [['numpy',[1,2,3]],['Mako',[3,2,2]]]
        self.assertEqual(methods.findIndex(testList,'numpy'),0)

    def test_FindIndexUnableToLocate(self):
        testList = [['numpy',[1,2,3]],['Mako',[3,2,2]]]
        self.assertEqual(methods.findIndex(testList,'Test'),None)

    def test_isNUmberTrue(self):
        self.assertEqual(methods.contains_number('numpy>1.23.5'),True)
    
    def test_isNUmberFalse(self):
        self.assertEqual(methods.contains_number('numpy'),False)

    def test_getPackagesDetails_detectMoreSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMore.txt')
        ,[['numpy',[1,23,5],'more'],['pypiwin32',[222],'more'],['soupsieve',[2,3,2,'post1'],'more'],
        ['certifi',[2022,6,15],'more']])

    def test_getPackagesDetails_detectMoreThanEqualToSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreThanEqualTo.txt')
        ,[['numpy',[1,23,5],'moreThanEqualTo'],['pypiwin32',[222],'moreThanEqualTo'],['soupsieve',[2,3,2,'post1'],'moreThanEqualTo'],
        ['certifi',[2022,6,15],'moreThanEqualTo']])
    
    def test_getPackagesDetails_detectLessSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementLess.txt')
        ,[['numpy',[1,23,5],'less'],['pypiwin32',[225],'less'],['soupsieve',[2,3,2,'post1'],'less'],
        ['certifi',[2022,6,15],'less']])
    
    def test_getPackagesDetails_detectHexMore(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementHexMore.txt')
        ,[['numpy',[1,23,5],'more'],['pypiwin32',[223],'more'],['soupsieve',[2,3,2,'post1'],'more'],
        ['certifi',[2022,6,15],'more']])
    
    def test_getPackagesDetails_detectEqualSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementEqual.txt')
        ,[['numpy',[1,23,5],'equal'],['pypiwin32',[223],'equal'],['soupsieve',[2,3,2,'post1'],'equal'],
        ['certifi',[2022,6,15],'equal']])
    
    def test_getPackagesDetails_detectMoreAndLessSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreAndLess.txt')
        ,[['numpy',[1,23,5],[2,0,0],'more','less'],['pypiwin32',[223],[230],'more','less'],
        ['soupsieve',[2,3,2,'post1'],[2,3,4,'post1'],'more','less'],['certifi',[2022,6,15],[2022,7,15],'more','less']])

    def test_getPackagesDetails_detectMoreThanEqualToAndLessSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreThanEqualToAndLess.txt')
        ,[['numpy',[1,23,5],[2,0,0],'moreThanEqualTo','less'],['pypiwin32',[223],[230],'moreThanEqualTo','less'],
        ['soupsieve',[2,3,2,'post1'],[2,3,4,'post1'],'moreThanEqualTo','less'],['certifi',[2022,6,15],[2022,7,15],'moreThanEqualTo','less']])

    def test_getPackagesDetails_detectInvalidSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementInvalid.txt')
        ,[['numpy+1.23.5','invalidSymbol']])
    
    def test_getPackagesDetails_detectInvalidSymbol2(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementInvalid2.txt')
        ,[['numpy+1.23.5,< 1.23.10','invalidSymbol']])

if __name__ == '__main__':
    unittest.main()