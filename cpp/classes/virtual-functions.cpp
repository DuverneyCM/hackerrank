/*
Sample Input:
4
1
Walter 56 99
2
Jesse 18 50 48 97 76 34 98
2
Pinkman 22 10 12 0 18 45 50
1
White 58 87
Sample Output:
Walter 56 99 1
Jesse 18 403 1
Pinkman 22 135 2
White 58 87 2
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

static int StudentId = 0;
static int ProfessorId = 0;

class Person {
public:
    string name;
    int age;
    virtual void getdata() {
        cin >> name >> age;
    }
    virtual void putdata() {
        cout << name << " " << age << " ";
    }
};

class Professor : public Person {
    int publications, id;
public:
    Professor() {
        ProfessorId++;
    }
    void getdata() {
        id = ProfessorId;
        Person::getdata();
        cin >> publications;
    }
    void putdata() {
        Person::putdata();
        cout << publications << " " << id << endl;
    }
};
class Student : public Person {
    static const int noMarks = 6;
    static int cur_id;
    int id, marks[6];
public:
    Student() {
        StudentId++;
    }
    void getdata() {
        id = StudentId;
        Person::getdata();
        for(int i=0; i<noMarks; i++){
            cin >> marks[i];
        } 
    }
    void putdata() {
        int sum = 0;
        for(int i=0; i<noMarks; i++){
            sum += marks[i];
        } 
        Person::putdata();
        cout << sum << " " << id << endl;
    }
};

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
