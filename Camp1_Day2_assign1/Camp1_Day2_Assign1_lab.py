import json
def Readfile():
    file = open("Attended.json", "r") 
    data = json.load(file)
    StrInputSession = data["sessions"]    
    return StrInputSession
    
if __name__ == '__main__':   
   AttendSession = Readfile()
   #print(AttendSession)   
   print ("I have attended ",len(AttendSession.split(','))," sessions!!")