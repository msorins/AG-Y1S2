#include <fstream>
using namespace std;

#define MAXN 105
#define INF 0x3f3f3f3f

ifstream cin("royfloyd.in");
ofstream cout("royfloyd.out");

int graf[MAXN][MAXN], n;

int main() {
    int i, j, k;

    cin >> n ;

    for(i = 1; i <= n; i++)
        for(j = 1; j <= n; j++)
        {
            cin >> graf[i][j];
            if(!graf[i][j])
                graf[i][j] = INF;
        }

    for(k = 1; k <= n; k++)
        for(i = 1; i <= n; i++)
            for(j = 1; j <= n; j++)
                if(i != j && graf[i][k] != INF && graf[k][j] != INF)
                    graf[i][j] = min(graf[i][j], graf[i][k] + graf[k][j]);

    for(i = 1; i <= n; i++)  {
        for(j = 1; j <= n; j++)
            if(graf[i][j] == INF)
                cout<<"0 ";
            else
                cout<<graf[i][j]<<" ";

        cout<<"\n";
    }

}