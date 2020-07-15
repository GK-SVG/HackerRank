#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int n,count=1,max=0,temp;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        /* code */
        cin>>arr[i];
    }
    
    sort(arr,arr+n);
    for (int i = 0; i < n; )
    {
        /* code */
        count=1;
        for (int j = i+1; j < n; j++)
        {
           
            if(arr[i]==arr[j] && count<3){
               count++;        
            }
            else
            {
                i=j;
                break;
            }      
        }
        max+=count;
    }
    cout<<max<<endl;
    
}