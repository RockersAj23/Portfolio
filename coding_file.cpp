#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while (t--)
    {
        int n;
        cin>>n;
        string std1;
        cin >>std1;
        char str[2*n];
        for (int i = 0; i < 2*n; i++)
        {
            str[i]=0;
        }
        int j=0;
        for (int i = 0; i < n-1; i++)
        {
            if(std1[i]!='a' && std1[i]!='e' && std1[i+1]!='e' && std1[i+1]!='a'){
                str[j]='.';
            }else{
                str[j]=std1[i];
            }
            j++;
        }
        for (int i = 0; i < 2*n; i++)
        {
            if(str[i]==0){
                continue;
            }
            cout<<str[i];
        }
        cout<<endl;

    }
    return 0;
}