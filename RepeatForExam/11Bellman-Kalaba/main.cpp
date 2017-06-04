#include <fstream>
#include <iostream>
using namespace std;

ifstream in("graf.in");
#define MAXN 5001
#define INF 0x3f3f3f3f

int n, m;
int d[MAXN][MAXN], dCrt[MAXN][MAXN], l[2][MAXN];

void afisMat(int mat[][MAXN], int n, int m) {
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++)
            cout<<mat[i][j]<<" ";
        cout<<"\n";
    }

    cout<<"\n";
}

void afisV(int v[], int n) {
    for(int i = 1; i <= n; i++)
        cout<<v[i]<<" ";

    cout<<"\n";
}

int main() {

    int i, j, x, y, z, crt, last, minLin;
    bool ok;
    in >> n >> m;

    for(i = 1; i <= n; i++)
        for(j = 1; j <= n; j++)
            if(i == j)
                d[i][j] = 0;
            else
                d[i][j] = INF;

    for(i = 1; i <= m; i++) {
        in >> x >> y >> z;
        d[x][y] = z;
    }

    crt = 1;
    for(i = 1; i <= n; i++)
        l[crt][i] = d[i][n];

    crt = 0; last = 1;
    while(true) {
        for(i = 1; i <= n; i++) {
            minLin = INF;
            for(j = 1; j <= n; j++) {
                dCrt[i][j] = l[last][j] + d[i][j];
                minLin = min(minLin, dCrt[i][j]);
            }

            l[crt][i] = min(l[last][i], minLin);
        }

        ok = false;
        for(i = 1; i <= n; i++)
            if(l[crt][i] != l[last][i])
                ok = true;

        if(!ok)
            break;

        crt = 1 - crt;
        last = 1 - last;

    }

    afisV(l[crt],n);




}