import json

def Readfile():
    file = open("ListNumber.json", "r")
    data = json.load(file)
    StrSequence = data["sequence"]
    return StrSequence

if __name__ == '__main__':
    EvenNumber = []
    sequence = Readfile()
    sequenceList=sequence.split(',')    
    for i in range(len(sequenceList)):
        if(int(sequenceList[i]) % 2 == 0):
            EvenNumber.append(sequenceList[i])
    str1 = ', '.join(EvenNumber)
    print ("The even numbers are "+str1)
