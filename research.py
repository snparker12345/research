import json
import traceback
file_path = "C:/Users/snpar/csc216/research/logFile.json" 
#file_path = "C:/Users/snpar/csc216/research/formatted.json"
eventList = []
eventTypeList = []
noEventTypeList = []
with open(file_path) as f:
    for jsonObj in f:
        try: 
            studentDict = json.loads(jsonObj)
            try:
                if studentDict['client']['event'] not in eventList:
                    eventList.append(studentDict['client']['event'])
            except:
                print("error: no event " + jsonObj)
            try:
                if studentDict['client']['event_type'] not in eventTypeList:
                    eventTypeList.append(studentDict['client']['event_type'])
            except:
                print("error: no event_type " + jsonObj)
                eventTypeList.append(studentDict['client']['event'])
                #add list of unique events where there are no event types
        except Exception as e:
            print(repr(e))
            # traceback.print_exc()
            #print(jsonObj)
            #print character
            #dict of unique events, list of events
            #look at doc loaded and document history
print("events: ")
print(eventList)
print("event types: ")
print(eventTypeList)

