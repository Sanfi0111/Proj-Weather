import unittest
from sys import path
path.append("../..")
from readerCsv import readerCsv
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
    
    " Test that verifies the correct performance of readDataSet()"
    def testReadDataSet(self):
        dicTes = {}
        dicTes ={0:{'State':'Colorado','Team': 'Rockies'},
            1:{'State':'Boston','Team':'Red Sox'},
            2:{'State':'Minnesota','Team':'Twins'}, 
            3:{'State':'Milwaukee','Team':'Brewers'},
            4:{'State':'Seattle','Team':'Mariners'}}
        csv = readerCsv()
        dic = csv.readDataSet('src/test.csv')
        self.assertEqual(dicTes,dic)



if __name__ == "__main__":
    unittest.main()