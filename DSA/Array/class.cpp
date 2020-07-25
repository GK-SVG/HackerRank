#include <iostream>
#include <sstream>
#include <string>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student{
    int age,standard;
    string first_name,last_name;
    public:
    void set_age(int a){
        age=a;
    }
    void set_standard(int s){
       standard=s;
    }
     void set_first_name(string fn){
         first_name=fn;
     }
     void set_last_name(string fn){
         last_name=fn;
     }
     int get_age(){
         return age;
     }
     string get_last_name(){
         return last_name;
     }
     string get_first_name(){
         return first_name;
     }
     int get_standard(){
         return standard;
     }
     string to_string(){
         string str1,str2,tstr;
         stringstream s1,s2;  
         s1<<age;
         s2<<standard;   
         s1>>str1; 
         s2>>str2;
         tstr=str1+","+first_name+","+last_name+","+str2;
         return tstr;
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