#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n,m,size;
    cin>>n>>m;
    //cout<<"n=="<<n<<" m=="<<m<<endl;
    int arr[n][100000];
    for(int i =0;i<n;i++){
        cin>>size;
        //cout<<"size=="<<size<<endl;
        for(int j=0;j<size;j++){
            cin>>arr[i][j];
            //cout<<"i=="<<i<<" j=="<<j;
        }
        //cout<<endl;
    } 
    int qarr[m][2];
    for(int i =0;i<m;i++){
        for(int j=0;j<2;j++){
        cin>>qarr[i][j];
        //cout<<"i=="<<i<<" j=="<<j;
        }
        //cout<<endl;
    }
    for(int i =0;i<m;i++){
        
            cout<<arr[qarr[i][0]][qarr[i][1]]<<endl;
        
    }
    return 0;
}