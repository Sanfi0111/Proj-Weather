import csv
import unittest
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import readerCsv

class test1(unittest.TestCase):
    """ Test that checks all the lines in dataSet1.csv.
        Returns :
        True if both elements are the same
    """
    def test_readElementsDataSet(self):
        # assertTrue asegura que un valor es real
        # assertFalse asegura que un valor es falso
        csvReaders = {}
        csv = readerCsv.readerCsv()
        csvReaders = csv.readDataSet("tests/dataset1.csv") 
        print(len(csvReaders))
        self.assertEqual(len(csvReaders), 3000)
    
    """ Test that verifies the correct performance of readDataSet()
        True if both elements are the same
    """
    def testReadDataSet(self):
        dicTes = {}
        dicTes ={0:{'State':'Colorado','Team': 'Rockies'},
            1:{'State':'Boston','Team':'Red Sox'},
            2:{'State':'Minnesota','Team':'Twins'}, 
            3:{'State':'Milwaukee','Team':'Brewers'},
            4:{'State':'Seattle','Team':'Mariners'}}
        csv = readerCsv.readerCsv()
        dic = csv.readDataSet("tests/test.csv")
        self.assertEqual(dicTes,dic)



if __name__ == "__main__":
    unittest.main()