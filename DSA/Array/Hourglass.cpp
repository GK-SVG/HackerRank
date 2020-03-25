#include<iostream>
using namespace std;
int main()
{
    int n,m,sum=0,max=0;
    cin>>n>>m;
    cout<<n<<" "<<m;
    int arr[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        cin>>arr[i][j];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        cout<<arr[i][j]<<" ";
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; i < n; j++)
        {
            for (int k = i; k <i+3 && k<n ; k++)
            {
                for (int l = j; l < j+3 && l<m; l++)
                {
                    sum+=arr[k][l];
                }
                
            }
            if(max<sum)
            {
                max=sum;
            }
        }
        
    }
    cout<<"max= "<<max;
    return 0;
    
}