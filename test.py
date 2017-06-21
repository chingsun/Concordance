import unittest
import os
import filecmp
from concordance import *

class SemiColonTest(unittest.TestCase):
    def testSemiColon(self):
        concordance = Concordance('input/semiColon.txt')
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path+'/output')
        file = open('semiColon.output', 'w')
        file.write(Concordance.writeConcordance(concordance))
        file.close()
        os.chdir(path)
        self.assertTrue(filecmp.cmp('test/semiColon.test', 'output/semiColon.output'))

class ConcordanceTest(unittest.TestCase):
    def testOpenFile(self):
        concordance = Concordance('input/description.txt')
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path+'/output')
        file = open('description.output', 'w')
        file.write(Concordance.writeConcordance(concordance))
        file.close()
        os.chdir(path)
        self.assertTrue(filecmp.cmp('test/description.test', 'output/description.output'))

if __name__ == '__main__':
    unittest.main()
