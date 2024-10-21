import csv

# open file as text
with open ('banknotes.csv','r') as data:
    lines = data.readlines()
    
    
print(type(lines))
print(lines[:10])

# open file as dataset
with open ('banknotes.csv','r') as data:
    reader = csv.reader(data)
    next(reader) # skip the header
    
    bill_data = []
    for line in reader:
        bill_data.append(line)
        
print('------------')        
print(bill_data[:10])

