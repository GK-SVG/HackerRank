#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,q;
    cin>>n>>q;
    string str1,tstr;
    while(n){
         cin>>str1;
         tstr+=(str1+"\n");
         n-=1;
    }
    
    return 0;
}
