import os
import csv
import string

nameFile = "PoopCount.csv"
fields = ['Name','Count']
#format -> name : count

def add(name: string):
    if(not os.path.isfile(nameFile)):
        dict = [{'Name':name, 'Count':'1'}]
        file = open(nameFile,'x')
        writer = csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(dict)
        file.close()
    else:
        with open(nameFile) as file:
            reader = csv.DictReader(file, fieldnames=fields)
            writer = csv.DictWriter(file, fieldnames=fields)
            for row in reader:
                if row['Name'] == name:
                    row['Name'],row['Count'] = row['Name'],str(int(row['Count'])+1)
                row = {'Name':row['Name'], 'Count':row['Count']}
                writer.writerow(row)



add("Alfonso")
    
