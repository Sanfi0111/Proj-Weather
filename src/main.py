import csv

file = open('src\dataset1.csv')
print('llegue')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
print('llegue')
file.close()
