import os
import csv
from csv import writer
import string
import datetime

nameFile = "PoopCount.csv"
separador = ';'
#formato -> nombre;fecha;hora

def add(name: string, date: datetime):
    """
    if(not os.path.isfile(nameFile)):
        file.close()
    """

    os.path.isfile(nameFile)

    with open(nameFile, mode='a') as file:
        input = name + separador + str(date.date()) + separador + str(date.time()) +"\n"
        file.write(input)



    
