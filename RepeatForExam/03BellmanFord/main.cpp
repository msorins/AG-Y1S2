#include <fstream>
#include <vector>
#include <queue>
using namespace std;

#define MAXN 50005
#define INF 0x3f3f3f3f

ifstream cin("bellmanford.in");
ofstream cout("bellmanford.out");

struct grf {
    int nod, cost;
};

vector<grf> graf[MAXN];
queue<int> coada;
int n, m;
int cost[MAXN], nrc[MAXN];
bool negativ;

int main() {
    int i, j, x, y, z, crtNod, nextNod, nextCost;
    grf aux;

    cin >> n >> m;
    for(i = 1; i <= m; i++) {
        cin >> x >> y >> z;
        aux.nod = y;
        aux.cost = z;
        graf[x].push_back(aux);
    }

    for(i = 1; i <= n; i++)
        cost[i] = INF;

    cost[1] = 0;
    coada.push(1);

    while(!coada.empty()) {
        crtNod = coada.front(); coada.pop();

        for(i = 0; i < graf[crtNod].size(); i++) {
            nextNod = graf[crtNod][i].nod;
            nextCost = graf[crtNod][i].cost;

            if(cost[nextNod] > cost[crtNod] + nextCost) {
                if(nrc[nextNod] > n)
                    negativ = true;
                else {
                    nrc[nextNod]++;
                    cost[nextNod] = cost[crtNod] + nextCost;
                    coada.push(nextNod);
                }

            }

        }
    }

    if(negativ)
        cout<<"Ciclu negativ!";
    else
        for(i = 2; i <= n; i++)
            cout<<cost[i]<<" ";

    return 0;
}