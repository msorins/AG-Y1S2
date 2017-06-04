#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAXN 1005
#define INF 0x3f3f3f3f

ifstream in("graf.in");

struct grf {
    int nod, cost;
};

vector<grf> graf[MAXN], grafT[MAXN];
vector<int> sortTNodes;
queue<int> coada;

int depinde[MAXN], d[MAXN];
int n, m;

void sortareTop() {
    grf next;
    int i, crt;

    for(i = 1; i <= n; i++) {
        if(!depinde[i])
            coada.push(i);
    }

    while(!coada.empty()) {
        crt = coada.front(); coada.pop();

        for(i = 0; i < graf[crt].size(); i++) {
            next = graf[crt][i];

            depinde[next.nod]--;
            if(!depinde[next.nod]) {
                coada.push(next.nod);
            }
        }

        sortTNodes.push_back(crt);
    }
}

int main() {
    int i, j, x, y, z, crt;
    grf prev, aux;

    in >> n >> m;
    for(i = 1; i <= m; i++) {
        in >> x >> y >> z;

        aux.nod = y; aux.cost = z;
        graf[x].push_back(aux);

        aux.nod = x; aux.cost = z;
        grafT[y].push_back(aux);

        depinde[y]++;
    }

    /*
     * 1st step: sortare topologica
     */
    sortareTop();


    /*
     * 2nd step: reverse bellman ford
     */

    for(i = 1; i <= n; i++)
        d[i] = -INF;

    int startNode = sortTNodes.back();
    d[startNode] = 0;
    coada.push(startNode);

    while(!coada.empty()) {
        crt = coada.front(); coada.pop();

        for(i = 0; i < grafT[crt].size(); i++) {
            prev = grafT[crt][i];

            if(d[prev.nod] < d[crt] + prev.cost) {
                d[prev.nod] = d[crt] + prev.cost;
                coada.push(prev.nod);
            }
        }
    }

    for(i = 1; i <= n; i++)
        cout << d[i] << " ";






    return 0;
}