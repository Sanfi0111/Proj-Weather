import csv
from readerCsv import readerCsv
from request import Request
"""
Main method that runs the program
"""
def main():
    reques1t = Request()   
    csv = readerCsv
    reques1t.request(csv.readDataSet('dataset1.csv'))


if __name__ == "__main__":
    main()
        


    

