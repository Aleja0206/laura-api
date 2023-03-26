import csv
def passfile()
    
with open("students.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)