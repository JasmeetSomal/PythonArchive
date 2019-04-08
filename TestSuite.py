import unittest
import os
#import TestLogin
import test_cases.trail
from archive_globals import HTMLTestRunner

direct = os.getcwd()


class TestSuite(unittest.TestCase):
   
    def test_main(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromModule(test_cases.trail)        
        ])
 
        outfile = open(os.path.join(direct, 'Report.html'), "wb")
 
        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Unit Test'
        )
 
        runner1.run(smoke_test)
 
if __name__ == "__main__":
    unittest.main()
    
    
