import csv
ifile  = open('sample.csv', "rb")
read = csv.reader(ifile)
for row in read :
    print (row) 
