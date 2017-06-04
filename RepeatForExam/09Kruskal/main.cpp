#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream cin("apm.in");
ofstream cout("apm.out");

#define MAXN 200005
#define INF 0x3f3f3f3f

struct muchie {
    int x, y, cost;
};

vector<muchie> graf, rasp;
int gr[MAXN];
int n, m, costAPM;

bool cmp(muchie A, muchie B) {
    return A.cost < B.cost;
}

int grupa(int nr) {
    if(gr[nr] == nr)
        return nr;

    gr[nr] = grupa(gr[nr]);
    return gr[nr];
}

void reuniune(int a, int b) {
    gr[grupa(a)] = grupa(b);
}

int main() {
    int i;
    muchie aux;
    cin >> n >> m;

    for(i = 1; i <= m; i++) {
        cin >> aux.x >> aux.y >> aux.cost;
        graf.push_back(aux);
    }

    for(i = 1; i <= n; i++)
        gr[i] = i;

    sort(graf.begin(), graf.end(), cmp);

    for(i = 0; i < m; i++) {
        if(grupa(graf[i].x) != grupa(graf[i].y)) {
            reuniune(graf[i].x, graf[i].y);
            rasp.push_back(graf[i]);
            costAPM += graf[i].cost;
        }
    }

    cout<<costAPM<<"\n";
    cout<<n-1<<"\n";
    for(i = 0; i < rasp.size(); i++)
        cout<<rasp[i].x<<" "<<rasp[i].y<<"\n";

    return 0;
}