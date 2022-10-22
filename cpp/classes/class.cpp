/*
Sample Input:
15
john
carmack
10
Sample Output:
15
carmack, john
10

15,john,carmack,10
*/

#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student {
  private:
    int age, standard;
    string first_name, last_name;
  public:
    void set_age(int p_age){
        age = p_age;
    }
    int get_age() {
        return age;
    }
    void set_first_name(string p_first_name){
        first_name = p_first_name;
    }
    string get_first_name() {
        return first_name;
    }
    void set_last_name(string p_last_name){
        last_name = p_last_name;
    }
    string get_last_name() {
        return last_name;
    }
    void set_standard(int p_standard){
        standard = p_standard;
    }
    int get_standard() {
        return standard;
    }
    string to_string(){
        string result, str_age, str_standard;
        stringstream ss;
        ss << age;
        ss << ",";
        ss << first_name;
        ss << ",";
        ss << last_name;
        ss << ",";
        ss << standard;
        ss >> result;
        return result;
    }
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}