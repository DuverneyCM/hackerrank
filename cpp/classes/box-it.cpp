/*
Sample Input:
6
2 1039 3749 8473
4
3 1456 3836 283
3 729 3749 272
2 4839 283 273
4
Sample Output:
1039 3749 8473
33004122803
Greater
Lesser
4839 283 273
373856301
*/

#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
class Box {
    //l,b,h are integers representing the dimensions of the box
    int l, b, h;
    // The class should have the following functions : 
    public:
    // Constructors: 
        // Box();
        Box() {
            l = 0; b = 0; h = 0;
        }
        // Box(int,int,int);
        Box(int length, int breadth, int height) {
            l = length; b = breadth; h = height;
        }
        // Box(Box);
        Box(Box *box1) {
            l = box1->getLength();
            b = box1->getBreadth();
            h = box1->getHeight();
        }

        // int getLength(); // Return box's length
        int getLength(){
            return l;
        }
        // int getBreadth (); // Return box's breadth
        int getBreadth(){
            return b;
        }
        // int getHeight ();  //Return box's height
        int getHeight(){
            return h;
        }
        // long long CalculateVolume(); // Return the volume of the box
        long long CalculateVolume() {
            long long result = l*b;
            result *= h;
            return result;//l*b*h;
        }

        //Overload operator < as specified
        //bool operator<(Box& box) {
        bool operator<(Box& box) {
            if (l < box.l) return true;
            else if (b < box.b && l==box.l) return true;
            else if (h < box.h && b == box.b && l == box.l) return true;
            else return false;
        }
        
        //Overload operator << as specified
        //ostream& operator<<(ostream& out, Box& B) {
        friend ostream& operator<<(ostream& out, Box& B) {
            out << B.l << " " << B.b << " " << B.h;
            return out;
        }
};



void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}