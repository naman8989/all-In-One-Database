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
    
    def parsing(self):
        pass
    
    def binding(self):
        # set tempenv here
        pass

    def optimization(self):
        # if necessary
        pass
    
    def runQuery(self):
        pass

class databaseHandler:
    def __init__(self,path):
        self.databasesPath = path
        pass

    def checkDatabaseExit(self):
        return os.path.isdir(self.databasesPath)

    def createDatabase(self,name):
        if not self.checkDatabaseExit(path=f"{self.databasesPath}/{name}"):
            return "already exist"
        if name != None:
            os.makedirs(self.databasesPath,exist_ok=True)
            if self.checkDatabaseExit(path=f"{self.databasesPath}/{name}"):
                return True
        return False
        
    def readDatabases(self):
        allDatabases = [item for item in os.listdir(self.databasesPath) if os.path.isdir(os.path.join(self.databasesPath, item))]
        print(allDatabases)

    def updateDatabaseInUse(self,envPath,name):
        try:
            updDatabase = backendEnv(envPath)
            data = updDatabase.importEnv()
            data["selectedDatabase"] = name
            updDatabase.updateEnv(data)
        except:
            return False
        
        return True    

    def deleteDatabase(self,name):
        os.rmdir(self.databasesPath+"/"+name)
        if self.checkDatabaseExit(path=self.databasesPath+"/"+name):
            return True
        return False



backend = backendEnv("./backendEnvSetup.json")


        
    