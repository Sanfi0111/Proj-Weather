import unittest
from sys import path
path.append("../..")
from Python import readerCsv
class test1(unittest.TestCase):
    """ Test that checks all the lines in dataSet1.csv.
    """
    def test_readElementsDataSet(self):
        # assertTrue asegura que un valor es real
        # assertFalse asegura que un valor es falso
        csvReaders = {}
        csv = readerCsv()
        csvReaders = csv.readDataSet() 
        print(len(csvReaders))
        self.assertEqual(len(csvReaders), 3000)
    
    def test_readDataSet():
        dic = {}

if __name__ == "__main__":
    unittest.main()