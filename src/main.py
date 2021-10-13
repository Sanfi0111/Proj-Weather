import csv
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import readerCsv
from src import request
"""
Main method that runs the program
"""
def main():
    reques1t = request.Request()   
    csv = readerCsv.readerCsv()
    reques1t.request(csv.readDataSet("dataset1.csv"))


if __name__ == "__main__":
    main()
        


    

