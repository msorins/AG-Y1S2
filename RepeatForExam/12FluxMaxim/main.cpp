#include <fstream>
#include <vector>
#include <queue>
using namespace std;

#define MAXN 1005
#define INF 0x3f3f3f3f

ifstream cin("maxflow.in");
ofstream cout("maxflow.out");

vector<int> graf[MAXN];
queue<int> coada;
int capacitate[MAXN][MAXN], flux[MAXN][MAXN], tata[MAXN];
int n, m, fluxTotal;

bool bfs(int st, int dr) {
    int i, crt, urm;

    while(!coada.empty())
        coada.pop();

    for(i = 1; i <= n; i++)
        tata[i] = 0;

    tata[st] = -1;
    coada.push(st);

    while(!coada.empty()) {
        crt = coada.front(); coada.pop();

        if(crt == dr)
            return 1;

        for(i = 0; i < graf[crt].size(); i++) {
            urm = graf[crt][i];

            if(!tata[urm] && capacitate[crt][urm] > flux[crt][urm]) {
                tata[urm] = crt;
                coada.push(urm);
            }
        }
    }

    return 0;
}

int main() {
    int i, j, x, y, z, ant, crtFlux;

    cin >> n >> m;
    for(i = 1; i <= m; i++) {
        cin >> x >> y >> z;
        graf[x].push_back(y);
        graf[y].push_back(x);
        capacitate[x][y] = z;
    }

    while(bfs(1, n)) {
        for(i = 0; i < graf[n].size(); i++) {
            ant = graf[n][i];

            if(tata[ant] && capacitate[ant][n] > flux[ant][n]) {
                crtFlux = INF;
                tata[n] = ant;

                for(j = n; j != 1; j = tata[j])
                    crtFlux = min(crtFlux, capacitate[ tata[j] ][j] - flux[ tata[j] ][j]);

                for(j = n; j != 1; j = tata[j]) {
                    flux[ tata[j] ][j] += crtFlux;
                    flux[j][ tata[j] ] -= crtFlux;
                }

                fluxTotal += crtFlux;
            }
        }
    }

    cout << fluxTotal;
}