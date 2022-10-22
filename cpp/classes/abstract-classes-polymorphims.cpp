/*
Sample Input:
3 1
set 1 2
get 1
get 2
Sample Output:
2
-1
*/

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

//Very well explained
//https://yasemingerboga.medium.com/hackerrank-abstract-classes-polymorphism-solution-c-47bb92f31e44
class LRUCache : Cache {
public:
    LRUCache(int capacity)
    {
        this->head = this->tail = NULL;
        this->cp = capacity;
    }
    void set(int key, int value) {
        Node* newNode = new Node(key, value);
        if (newNode == NULL) return;
        if (head == NULL) {
            //first time 
            head = tail = newNode;
            mp[key] = newNode;
            return;
        }
        if (mp.size() == cp) {
            //when it reaches capacity, it will delete from the map, 
            //double linked list and add a new head node.
            mp.erase(tail->key);
            tail = tail->prev;
            delete tail->next;
            tail->next = NULL;
        }
        head->prev = newNode;
        newNode->next = head;
        head = newNode;
        mp[key] = newNode;
    }
    int get(int key) {
        map<int, Node*>::iterator it = mp.find(key);
        if (it == this->mp.end()) return -1;
        else return it->second->value;
    }
};

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}
