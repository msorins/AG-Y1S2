#include <fstream>
#include <vector>
#include <queue>
using namespace std;

#define MAXN 50005
#define INF 0x3f3f3f3f

ifstream cin("dijkstra.in");
ofstream cout("dijkstra.out");

struct grf {
    int nod, cost;
};

class comp {
public:
    bool operator() (grf A, grf B) {
        return A.cost > B.cost;
    }
};

vector<grf> graf[MAXN];
priority_queue<grf, vector<grf>, comp> coada;
int n, m;
int cost[MAXN];

int main() {
    int i, j, x, y, z, crtNod, crtCost, nextNod, nextCost;
    grf aux;

    cin >> n >> m;
    for(i = 1; i <= m; i++) {
        cin >> x >> y >> z;
        aux.nod = y;
        aux.cost = z;
        graf[x].push_back(aux);
    }

    for(i = 1; i <=n; i++)
        cost[i] = INF;

    cost[1] = 0;
    aux.nod = 1; aux.cost = 0; coada.push(aux);
    while(!coada.empty()) {
        crtNod = coada.top().nod;
        crtCost = coada.top().cost;
        coada.pop();

        //The cost has already changedd
        if(crtCost != cost[crtNod])
            continue;

        for(i = 0; i < graf[crtNod].size(); i++) {
            nextNod = graf[crtNod][i].nod;
            nextCost = graf[crtNod][i].cost;

            if(cost[nextNod] > cost[crtNod] + nextCost) {
                cost[nextNod] = cost[crtNod] + nextCost;
                aux.nod = nextNod;
                aux.cost = cost[nextNod];

                coada.push(aux);
            }
        }
    }

    for(i = 2; i <= n; i++)
        if(cost[i] == INF)
            cout<<"0 ";
        else
            cout<<cost[i]<<" ";

    return 0;
}