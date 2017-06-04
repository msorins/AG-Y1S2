#include <fstream>
#include <vector>
#include <queue>
using namespace std;

ifstream cin("apm.in");
ofstream cout("apm.out");

#define MAXN 200005
#define INF 0x3f3f3f3f

priority_queue< pair<int, int> > coada;
vector< pair<int, int> > graf[MAXN];

int d[MAXN], tata[MAXN];
bool fol[MAXN];
int n, m;

int main() {
    int i, x, y, z, crtNod, crtCost, nextNod, nextCost;
    cin >> n >> m;

    for(i = 1; i <= m; i++) {
        cin >> x >> y >> z;
        graf[x].push_back(make_pair(z, y));
        graf[y].push_back(make_pair(z, x));
    }

    for(i = 1; i <= n; i++)
        d[i] = INF;

    d[1] = 0;
    coada.push(make_pair(0, 1));

    while(!coada.empty()) {
        crtNod = coada.top().second;
        crtCost = -coada.top().first;
        fol[crtNod] = true;
        coada.pop();

        if(crtCost > d[crtNod])
            continue;

        for(i = 0; i < graf[crtNod].size(); i++) {
            nextNod = graf[crtNod][i].second;
            nextCost = graf[crtNod][i].first;

            if(!fol[nextNod] && d[nextNod] > nextCost) {
                d[nextNod] = nextCost;
                tata[nextNod] = crtNod;
                coada.push(make_pair(-nextCost, nextNod));
            }
        }
    }

    int costAPM = 0;
    for(i = 1; i <= n; i++) {
        costAPM += d[i];
    }

    cout<<costAPM<<"\n";
    cout<<n-1<<"\n";
    for(i = 2; i <= n; i++)
        cout<<i<<" "<<tata[i]<<"\n";

    return 0;
}