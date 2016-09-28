#include<bits/stdc++.h>
using namespace std;
int mat[6][6];
int main()
{
    mat[0][0] =1;
    cout<<mat[0][0];
    for(int i=0; i<6; i++)
    {
        for(int j=0; j<=i; j++)
        {
            if(mat[i][j]) continue;
            mat[i][j] = mat[i-1][j-1] + mat[i-1][j];
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

/*
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
*/
