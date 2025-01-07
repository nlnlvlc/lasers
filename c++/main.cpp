#include <iostream>;
#include <map>;
#include <vector>;
#include <fstream>;
#include <sstream>;

using namespace std;

struct Field{
    vector<vector<int>> field;
};

struct Lasers{
    
    vector<int[2], string[2]> lasers;
    map<vector<int>, vector<string>> maximums;
    Field field;

};

map<int[2], string[2]> insertion(map<int[2], string[2]> data){}

int max(int int1, int int2){
    int max = (int1 > int2) ? int1 : int2;
}

double max(double double1, double double2){
    double max = (double1 > double2) ? double1 : double2;
}

// uses code from https://www.geeksforgeeks.org/how-to-split-string-into-an-array-in-cpp/
vector<int> convertString(string& input, char delimiter,
                 vector<string> arr)
{
    // Creating an input string stream from the input string
    istringstream stream(input);

    // Temporary string to store each token
    string token;

    vector<int> values;
    string newLine = "\n";

    // Read tokens from the string stream separated by the
    // delimiter
    while (getline(stream, token, delimiter)) {
        // Add the token to the array
        arr.push_back(token);
    };

    // iterate through array and convert to int
    // if the item has a newline, remove last two characters before convert
    for (string it : arr){

        if (it[-1] == 'n') {
            it.pop_back();
            it.pop_back();
        }

        values.push_back(stoi(it));
    }

    return values;
};


Field GetMap(string filename){
    ifstream file(filename);
    vector<string> lines;
    vector<vector<int>> values;
    Field field;

    if (file.is_open()) {
        cout << "Loaded: " << filename << endl;
        string line;
        while (getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
    } else {
        cout << "Unable to open file" << endl;
    }

    char delimiter = ' ';

    // convert lines into vector<int>
    for (string line : lines){
        cout << "Line: " << line << endl;
        vector<string> temp;
        vector<int> converted = convertString(line, delimiter, temp);

        values.push_back(converted);
    }

    for (vector<int> val : values){
        cout << "Values: ";
        for (auto v : val){
            cout << v << " ";
        }
        cout << endl;
    }

    field.field = values;

    return field;

};

int PossiblePositions(Field field){

    int total;
    vector<vector<int>> map = field.field;
    

    if (map.size() < 2 || map[0].size() < 2){
        return 0;
    }

    if ((map.size() >= 2 && map[0].size() > 2) || (map.size() > 2 && map[0].size() >= 2)){
        int topBott = (map.size() - 2) * 2;
        int leftRight = (map[0].size() - 2) * 2;
        int middle = (map.size() - 2) * (map[0].size() - 2);
    

        if (topBott == 0 || leftRight == 0){
            return 0;
        }

        total = topBott + leftRight + middle;

        return total;
    } else {
        return 0;
    }

};

void AddEmUp(Field active){
    //call field
    vector<vector<int>> field = active.field;

    //records the coordinates for the center of laser, the direction it's facing
    // and the value of the laser placement with the highest sum
    map<vector<int>, vector<string>> maximums;

    //loops through each spot in each line of the field
    for (int i = 0; i < field.size(); i++){
        for (int j = 0; j < field[0].size(); j++){
            
            int MAX = 0, temp = 0;

            //if there is a legal spot in relation to the current spot, collect that value
            //if there is not legal spot in that direction, value is -1
            int north = -1, south = -1, east = -1, west = -1;

            string pos;
            vector<int> coords;
            vector<string> orientations;

            if (i-1 >= 0){
                north = field[i-1][j];
            }
            if (i+1 < field.size()){
                south = field[i+1][j];
            }
            if (j+1 < field[i].size()){
                east = field[i][j+1];
            }
            if (j-1 >= 0){
                west = field[i][j-1];
            }

            //if at least three directions have legal spots, add those values together
            //if that value is larger than current MAX, save new MAX and record orientation (pos)
            if (north != -1 && west != -1 && east != -1){
                temp = north + west + east;
                if (temp > MAX){
                    MAX = max(MAX, temp);
                    pos = "N";
                }
                    
            }
            if (west != -1 && north != -1 && south != -1){
                temp = west + north + south;
                if (temp > MAX){
                    MAX = max(MAX, temp);
                    pos = "W";
                }
            }
            if (east != -1 && north != -1 && south != -1){
                temp = east + north + south;
                if (temp > MAX){
                    MAX = max(MAX, temp);
                    pos = "E";
                }
            }
            if (south != -1 && east != -1 && west != -1){
                temp = south + east + west;
                if (temp > MAX){
                    MAX = max(MAX, temp);
                    pos = "S";
                }
            }

            //update maximums with the coordinates, orientation, and MAX value with the highest sum for this position
            //key: tuple (i:int (row), j:int (col)), value: tuple (pos: str, MAX: int)
            if (MAX > 0){
                
                maximums.insert({[i,j], [pos, MAX]});
            }
                
        }
    }   
    //store maximums in Lasers.maximums to be used outside of function
   //Lasers.maximums = maximums;
};

void PlaceLasers(int num){};

int LegalInput(string num){};

void UserInput(){};

int main(){};