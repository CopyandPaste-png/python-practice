"""
file.py

Adds file methopds
"""

def writeToFile(fileName,data):
        with open(fileName,"w") as f:
            f.write(data)
    
def appendToFile(fileName,data):
    with open(fileName,"a") as f:
        f.write(data)

def readFromFileData(fileName):
    with open(fileName,"r") as f:
        return f.read()

def readFromFileLines(fileName):
    with open(fileName,"r") as f:
        return f.readlines() 