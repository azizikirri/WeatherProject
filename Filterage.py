import json
import pymongo
from pymongo import MongoClient
conection = MongoClient("mongodb://localhost:27017")
db=conection["projet"]
col = db["colprojet"]
list_az = []
#open json file and convert it from json format to object dict format
with open ('donnees-synop-essentielles-omm.json') as json_file:
    data = json.load(json_file)
print (len(data))
#extract the required data
variable = ["nom","date","u","ff","tc"]
#loop for in json file
for i in data:
    j= {}
    for  k in variable :
        if k == "date":
            j["date"]=i["fields"][k][:10]
            j["hours"]=i["fields"][k][11:16]
        else :
            try:
               j[k]=i["fields"][k]
            except KeyError:
                j[k]=0
#add obj to list_az
    list_az.append(j)
c= db.get_collection("colprojet")
#add all data to my list_az
c.insert_many(list_az)
print(type(json_file))   
                
                 

                 
                 
            
            
"""fields = item['fields ']
        t = item ['t']
        pmer = item ['']
        code_epci  = item ['code_epci']
        codegeo = item ['codegeo']
        code_reg = item ['code_reg']
        tc = item ['tc']
        datasetid = item['datasetid']
        data_weather ={
            'fields':fields,
            't':t,
            'pmer':pmer,
            'code_epci':code_epci,
            'codegeo':codegeo,
            'code_reg':code_reg,
            'tc':tc,
            'datasetid':datasetid
        }
        weather_list.append(data_weather)
        print(weather_list)"""







    
    


    




