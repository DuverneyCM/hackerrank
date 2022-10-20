/*
Sample Input:
4 3
<tag1 value = "HelloWorld">
<tag2 name = "Name1">
</tag2>
</tag1>
tag1.tag2~name
tag1~name
tag1~value

Sample Output:
Name1
Not Found!
HelloWorld
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, Q;
    string curr = "", attr_name;
    map <string, string> m;
    cin >> N >> Q;
    cin.ignore(); //delete \n of the last line
    
    for (int i=0; i<N; i++) {
        string line, tag, extract;
        char token, previoustoken;
        getline(cin, line);
        stringstream ss(line);
        
        //process HRML lines
        while (getline(ss, extract, ' ')) {
            token = extract[0];
            if (extract[0] == '<'){ //it's a tag
                if (extract[1] != '/') { //it's not a closing tag
                    tag = extract.substr(1);
                    //for tags without attributes...
                    if (tag[tag.length()-1] == '>')
                        tag.pop_back(); //remove '>', the last symbol
                    
                    //for nesting tags...
                    if (curr.length() > 0)
                        curr += "." + tag; //concatenate ".tagx"
                    else
                        curr = tag;
                }
                
                else { //it's a closing tag
                    //remove "</" and ">" from the word
                    tag = extract.substr(2, extract.find('>')-2);
                    //check if the closing tag is the last tag in curr
                    size_t pos = curr.find('.' + tag);
                    //if (tag == curr.substr(pos))
                    if (pos != string::npos)
                        curr = curr.substr(0, pos);
                    else //invalid tag sequence
                        curr = "";
                }
                //cout << curr << endl;
            }
            //it's an attribute value
            else if (extract[0] == '"' && previoustoken == '=') { 
                size_t pos = extract.find_last_of('"');
                string attr_value = extract.substr(1, pos-1);
                m[attr_name] = attr_value;
                //cout << attr_name << ":" << attr_value << endl;
                //cout << previoustoken << endl;
            }
            //it's an attribute name
            else {
                if (extract != "=") {
                    attr_name = curr + "~" + extract;
                }
            }
            
            previoustoken = extract[0];
            
        }
    }
    
    string query;
    map<string,string>::iterator itr;
    for (int i=0; i<Q; i++) {
        getline(cin, query);
        
        //search in the map
        itr = m.find(query);
        if (itr != m.end())
            cout << itr->second << endl;
        else 
            cout << "Not Found!" << endl;
    }
    
    return 0;
}
