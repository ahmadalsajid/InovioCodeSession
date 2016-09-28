#include<bits/stdc++.h>
using namespace std;

int main()
{
    char str[100000];
    gets(str);
    int len = strlen(str);
    int sqt = sqrt(len);
    for(int i=0;i<len;i+=sqt)
    {
        for(int j=i;j<i+sqt;j++) cout<<str[j];
        cout<<endl;
    }
    return 0;
}
/*
Input: Hi, world

Output:
Hi,
Wo
Rld
*/

