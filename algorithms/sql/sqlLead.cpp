#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream> 
#include <cstdlib>  
#include "sqlite3/sqlite3.h"  

class Tools{
    public:
        std::vector<std::string> readEnv(std::string fileLoc ){

            std::ifstream file(fileLoc);

            if(!file){
                std::cout<<"sqlEnvSetup not found";
                return std::vector<std::string>();
            }

            std::vector<std::string> returnData = {};
            std::string line;
            while(std::getline(file,line)){
                returnData.push_back(line);
            }

            file.close();
            return returnData;
        }
        
        void printVector(std::vector<std::string> &v) {
            for (int i = 0; i < v.size(); i++) {
                std::cout << v[i] << " "<<v[i].length()<<" ";
            }
            std::cout << std::endl;
        }
};

// int main(){
int main(int argc, char* argv[]){
    
    sqlite3 *db ;
    int rc;

    rc = sqlite3_open("../../memory/sql/example.db", &db);    
    
    if (rc) {
        std::cerr << "Error opening database: " << sqlite3_errmsg(db) << std::endl;
        
    } else {
        std::cout << "Database opened successfully.\n";
    }
    std::cout<<(rc);

    Tools tools;
    std::vector<std::string> ret =  tools.readEnv("./sqlEnvSetup.txt");
    
    std::string input = argv[1];

    std::stringstream ss(input);

    std::vector<std::string> arguments = {};
    
    std::string token;
    while (std::getline(ss, token, '~')) {
        arguments.push_back(token);
    }
    
    sqlite3_close(db);

    return 0;
}




