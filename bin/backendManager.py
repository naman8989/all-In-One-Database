import json
import os 


class backendEnv:
    def __init__(self,envLoc):
        self.envLocation = envLoc

    def importEnv(self):
        with open(self.envLocation,'r') as file:
            self.envData = json.load(file)
        return self.envData
    
    def updateEnv(self,updatedData):
        try:
            with open(self.envLocation,"w") as file:
                self.envData = updatedData
                file = updatedData
        except:
            return False
        return True

        
class queryHandler:
    def __init__(self):
        pass
    
    def parsing(self,query):
        queryParts = query.split(" ")
        return queryParts
    
    def binding(self,queryParts,pos):
        # set tempenv here
        # and check for avaliable database and file
        if queryParts[0] in ["sql","mongo","Linklist"]: #selecting which database
            pass
        elif queryParts[0] in ["create","read","delete","use"]:
            pass
        else:
            return "something wrong with query"

        

    def optimization(self):
        # if necessary
        pass
    
    def runQuery(self):
        pass



class databaseHandler:
    def __init__(self,path):
        self.databasesPath = path # set path to "../memory"
        pass

    def checkDatabaseExit(self):
        return os.path.isdir(self.databasesPath)

    def createDatabase(self,name): # create database
        if not self.checkDatabaseExit(path=f"{self.databasesPath}/{name}"):
            return "already exist"
        if name != None:
            os.makedirs(self.databasesPath,exist_ok=True)
            if self.checkDatabaseExit(path=f"{self.databasesPath}/{name}"):
                return True
        return False
    
    def readDatabases(self): # read Database
        allDatabases = [item for item in os.listdir(self.databasesPath) ]
        allSubDatabase = []
        for i in allDatabases:
            allSubDatabase.append([item for item in os.listdir(self.databasesPath+"/"+i)])
        return [allDatabases,allSubDatabase]

    def updateDatabaseInUse(self,envPath,name): # update database pointer
        try:
            updDatabase = backendEnv(envPath)
            data = updDatabase.importEnv()
            data["selectedDatabase"] = name
            updDatabase.updateEnv(data)
        except:
            return False
        
        return True    

    def deleteDatabase(self,name):   # delete database
        os.rmdir(self.databasesPath+"/"+name)
        if self.checkDatabaseExit(path=self.databasesPath+"/"+name):
            return True
        return False



backend = backendEnv("./backendEnvSetup.json")


        
    