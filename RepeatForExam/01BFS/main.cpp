#include <fstream>
#include <vector>
#include <queue>
using namespace std;

ifstream cin("bfs.in");
ofstream cout("bfs.out");

#define MAXN 100005
#define INF 0x3f3f3f3f

vector<int> graf[MAXN];
queue<int> coada;
int dist[MAXN], n, m, start;

int main() {
    int i, j, x, y, crtNod, nextNod;

    cin >> n >> m >> start;
    for(i = 1; i <= m; i++) {
        cin >> x >> y;
        graf[x].push_back(y);
    }

    for(i = 1; i <= n; i++)
        dist[i] = INF;

    dist[start] = 0;
    coada.push(start);

    while(!coada.empty()) {
        crtNod = coada.front(); coada.pop();

        for(i = 0; i < graf[crtNod].size(); i++) {
            nextNod = graf[crtNod][i];
            if(dist[nextNod] > dist[crtNod] + 1) {
                dist[nextNod] = dist[crtNod] + 1;
                coada.push(nextNod);
            }
        }
    }

    for(i = 1; i <= n; i++) {
        if(dist[i] == INF)
            cout<<-1<<" ";
        else
            cout<<dist[i]<<" ";
    }
}