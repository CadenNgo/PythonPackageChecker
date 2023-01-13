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
        ,[
        ['numpy',[1],'more'],
        ['numpy',[1,23],'more'],  
        ['numpy',[1,23,5],'more'],
        ['numpy',[2,3,2,'post1'],'more'],
        ['numpy',[2022,6,15],'more']])

    def test_getPackagesDetails_detectMoreThanEqualToSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreThanEqualTo.txt')
        ,[
        ['numpy',[1],'moreThanEqualTo'],
        ['numpy',[1,23],'moreThanEqualTo'],
        ['numpy',[1,23,5],'moreThanEqualTo'],
        ['numpy',[2,3,2,'post1'],'moreThanEqualTo'],
        ['numpy',[2022,6,15],'moreThanEqualTo']])
    
    def test_getPackagesDetails_detectLessSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementLess.txt')
        ,[
        ['numpy',[1],'less'],
        ['numpy',[1,23],'less'],
        ['numpy',[1,23,5],'less'],
        ['numpy',[2,3,2,'post1'],'less'],
        ['numpy',[2022,6,15],'less']])
    
    def test_getPackagesDetails_detectLessThanEqualToSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementLessThanEqualTo.txt')
        ,[
        ['numpy',[1],'lessThanEqualTo'],
        ['numpy',[1,23],'lessThanEqualTo'],
        ['numpy',[1,23,5],'lessThanEqualTo'],
        ['numpy',[2,3,2,'post1'],'lessThanEqualTo'],
        ['numpy',[2022,6,15],'lessThanEqualTo']])
    
    def test_getPackagesDetails_detectTildeMore(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementTildeEqual.txt')
        ,[
        ['numpy',[1],'tildeEqual'],
        ['numpy',[1,23],'tildeEqual'],
        ['numpy',[1,23,5],'tildeEqual'],
        ['numpy',[2,3,2,'post1'],'tildeEqual'],
        ['numpy',[2022,6,15],'tildeEqual']])
    
    def test_getPackagesDetails_detectEqualSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementEqual.txt')
        ,[
        ['numpy',[1],'equal'],
        ['numpy',[1,23],'equal'],
        ['numpy',[1,23,5],'equal'],
        ['numpy',[2,3,2,'post1'],'equal'],
        ['numpy',[2022,6,15],'equal']])
    
    def test_getPackagesDetails_detectMoreAndLessSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreAndLess.txt')
        ,[
        ['numpy',[1],[2],'more','less'],
        ['numpy',[1,23],[2,0],'more','less'],
        ['numpy',[1,23,5],[2,0,0],'more','less'],
        ['numpy',[2,3,2,'post1'],[2,3,4,'post1'],'more','less'],
        ['numpy',[2022,6,15],[2022,7,15],'more','less']])

    def test_getPackagesDetails_detectMoreThanEqualToAndLessSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreThanEqualToAndLess.txt')
        ,[
        ['numpy',[1],[2],'moreThanEqualTo','less'],
        ['numpy',[1,23],[2,0],'moreThanEqualTo','less'],
        ['numpy',[1,23,5],[2,0,0],'moreThanEqualTo','less'],
        ['numpy',[2,3,2,'post1'],[2,3,4,'post1'],'moreThanEqualTo','less'],
        ['numpy',[2022,6,15],[2022,7,15],'moreThanEqualTo','less']])

    def test_getPackagesDetails_detectMoreAndLessThanEqualToSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreAndLessThanEqualTo.txt')
        ,[
        ['numpy',[1],[2],'more','lessThanEqualTo'],
        ['numpy',[1,23],[2,0],'more','lessThanEqualTo'],
        ['numpy',[1,23,5],[2,0,0],'more','lessThanEqualTo'],
        ['numpy',[2,3,2,'post1'],[2,3,4,'post1'],'more','lessThanEqualTo'],
        ['numpy',[2022,6,15],[2022,7,15],'more','lessThanEqualTo']])

    def test_getPackagesDetails_detectMoreThanEqualToAndLessThanEqualToSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementMoreThanEqualToAndLessThanEqualTo.txt')
        ,[
        ['numpy',[1],[2],'moreThanEqualTo','lessThanEqualTo'],
        ['numpy',[1,23],[2,0],'moreThanEqualTo','lessThanEqualTo'],
        ['numpy',[1,23,5],[2,0,0],'moreThanEqualTo','lessThanEqualTo'],
        ['numpy',[2,3,2,'post1'],[2,3,4,'post1'],'moreThanEqualTo','lessThanEqualTo'],
        ['numpy',[2022,6,15],[2022,7,15],'moreThanEqualTo','lessThanEqualTo']])

    def test_getPackagesDetails_detectInvalidSymbol(self):
        self.assertEqual(methods.getPackagesDetails('sampleRequirementforTestMethod/requirementInvalid.txt')
        ,[
        ['numpy+1.23.5','invalidSymbol'],
        ['numpy+1.23.5<1.23.10','invalidSymbol'],
        ['numpy-1.23.5','invalidSymbol'],
        ['numpy-1.23.5<1.23.10','invalidSymbol'],
        ['numpy%1.23.5','invalidSymbol'],
        ['numpy%1.23.5<1.23.10','invalidSymbol']
        ])
    
if __name__ == '__main__':
    unittest.main()


#Fix ~=

#user will use the pip list or pip freeze
#test on cases which user specific version

#base case is always == 
#base case three scenario 9 systematic versioning,calendar versioning host =1.1.1 == 1.1.0 , 1.1.1 = 1.2.1, 1.1. == 1.0.1, 1.1.1 == text, 1.1.1 == 1.2, 1.1. = 1.2
#beyond check on different symbols strech goals
    
#valid change it to supported or not supported
#pytest 

#Monday schedule afternoon 1 hour