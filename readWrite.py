import os
import csv
from csv import writer
import string
import datetime

nameFile = "PoopCount.csv"
fields = ['Name','Date']
#format -> name : count

def add(name: string, date: datetime):
    if(not os.path.isfile(nameFile)):
        input = [{'Name':name, 'Date':str(date)}]
        file = open(nameFile,'x')
        writer_file = csv.DictWriter(file,fieldnames=fields)
        writer_file.writeheader()
        writer_file.writerows(input)
        file.close()
    else:
        with open(nameFile, mode='a') as file:
            input = [{'Name':name, 'Date':str(date)}]
            writer_file = writer(file)
            writer_file.writerow(input)


    
