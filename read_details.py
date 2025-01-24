import csv

with open('details.csv','r') as file:
    reader=csv.reader(file)

    for details in reader:
        print(details)