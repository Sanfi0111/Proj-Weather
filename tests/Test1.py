import unittest
from sys import path
path.append("../..")
class Test1(unittest.TestCase):
    """ Test that checks all the lines in dataSet1.csv.
    """
    def test_readDataSet():
        # assertTrue asegura que un valor es real
        # assertFalse asegura que un valor es falso
        csvReaders = {}
        csv = readerCsv()
        csvReaders = csv.readDataSet() 
        assertTrue(assertEqual(len(csvReaders, 3000)))
        

if __name__ == "__main__":
    unittest.main()