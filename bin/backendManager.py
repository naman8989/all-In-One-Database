import json
import os 
import threading


class backendEnv:
    def __init__(self,envLoc):
        self.envLocation = envLoc
        self.envData = self.setEnv() 

    def setEnv(self):
        return {"selectedDatabase": 0, "selectedDataStructure": 0}
    
    def getEnv(self,pos):
        if pos == 0:
            return self.envData["selectedDatabase"]
        if pos == 1:
            return self.envData["selectedDataStructure"]
        return False
    
    def updateEnv(self,pos,name):
        try:
            if pos == 0:
                self.envData["selectedDatabase"] = name
            if pos == 1:
                self.envData["selectedDataStructure"] = name
        except:
            return False
        return True


class databaseHandler(backendEnv):
    def __init__(self,dbPath,envPath):
        super().__init__(envPath)
        self.databasesPath = dbPath # set path to "../memory"

    def checkFolder(self,checkPath):
        return os.path.isdir(checkPath)

    def create(self,name,bole): # create database
        if not bole:
            tempPath = f"{self.databasesPath}/{name}"
        else:
            if  self.getEnv(0)== 0: # for datastructure 
                return "Database not selected"
            tempPath = f"{self.databasesPath}/{self.getEnv(0)}/{name}"

        if self.checkFolder(checkPath=tempPath):
            return "DataStructure already exist" if bole else "Database already exist"
        if name != None:
            os.makedirs(tempPath,exist_ok=True)
            if self.checkFolder(checkPath=tempPath):
                return True
        return False
    
    def read(self,bole): # read Database
        if not bole:
            tempPath =self.databasesPath
        else:
            if  self.getEnv(0)== 0: # for datastructure 
                return "Database not selected"
            tempPath = self.databasesPath+"/"+self.getEnv(0)

        allInfo = [item for item in os.listdir(tempPath) ]
        allInfo.append(len(allInfo))
        return allInfo
    
    def use(self,name,bole):
        if not bole: 
            if self.checkFolder(self.databasesPath+"/"+name):
                return self.updateEnv(0,name)
            else:
                return "Database don't exist"
        else:
            if  self.getEnv(0)== 0: # for datastructure 
                return "Database not selected"
            elif self.checkFolder(self.databasesPath+"/"+self.getEnv(0)+"/"+name):
                return self.updateEnv(1,name)
            else:
                return "DataStructure don't exist"

        

       
    def delete(self,name,bole):   # delete database
        if not bole:
            tempPath = f"{self.databasesPath}/{name}"
        else:
            if self.getEnv(0) == 0: # delete subdatabase
                return "Database not selected"
            tempPath = f"{self.databasesPath}/{self.getEnv(0)}/{name}"
        if not self.checkFolder(checkPath=tempPath):
            return "DataStructure doesn't exists" if bole else "Database doesn't exists" 
        os.rmdir(tempPath)
        if self.checkFolder(checkPath=tempPath):
            return False
        return True
    
    def databaseProcessIDs(self):
        
        return

        
class queryHandler(databaseHandler):
    def __init__(self,dbPath,envPath):
        super().__init__(dbPath=dbPath,envPath=envPath)
    
    def workflow(self,quer):
        ret = self.parsing(query=quer)
        return self.binding(ret)

    def parsing(self,query):
        queryParts = query.split(" ")
        return queryParts
    
    def binding(self,queryParts):
        match queryParts[0]:
            case "create":
                if queryParts[1] == "database":
                    return super().create(queryParts[2],False) 
                elif queryParts[1] == "datastructure":
                    return super().create(queryParts[2],True) 
                else:
                    return "something wrong with query"
            case "read":
                if queryParts[1] == "databases":
                    return super().read(False)
                elif queryParts[1] == "datastructures":
                    return super().read(True)
                else:
                    return "something wrong with query"
            case "use":
                if queryParts[1] == "database":
                    return self.use(queryParts[2],False) 
                elif queryParts[1] == "datastructure":
                    return self.use(queryParts[2],True)  
                else:
                    return "something wrong with query"
            case "delete":
                if queryParts[1] == "database":
                    return super().delete(queryParts[2],False)
                elif queryParts[1] == "datastructure":
                    return super().delete(queryParts[2],True)                    
                else:
                    return "something wrong with query"
        return "Nothing to bind"

    # def optimization(self):
    #     # if necessary
    #     pass
    
    # def runQuery(self):
    #     pass    


if __name__ == "__main__":
    backend = queryHandler("./memory","./bin/backendEnvSetup.json")
    parseQuery = ""
    while parseQuery != "f":
        print(backend.workflow(parseQuery))
        parseQuery = input("Query >> ")


    



        
    