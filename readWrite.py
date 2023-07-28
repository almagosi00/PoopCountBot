import os
from csv import writer
import string
import datetime
import operator

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


def count():
    dictCount = dict()
    with open(nameFile,mode='r') as file:
        rows = file.readlines()
        for row in rows:
            rowList = row.split(separador)
            if(rowList[0] in dictCount):
                
                dictCount.update({rowList[0]:dictCount.get(rowList[0]) + 1})
            else:
                dictCount.update({rowList[0]:1})
    output = ""
    dictOutput = dict( sorted(dictCount.items(), key=operator.itemgetter(1),reverse=True))
    for i in dictOutput:
        output = output + "\n" + i + " --> " + str(dictCount[i])
    return output
            