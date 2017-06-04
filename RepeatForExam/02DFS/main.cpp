#include <fstream>
#include <vector>
using namespace std;

ifstream cin("dfs.in");
ofstream cout("dfs.out");

#define MAXN 100005
#define INF 0x3f3f3f3f

vector<int> graf[MAXN];
int n, m, nrCMP;
bool viz[MAXN];

void dfs(int nod) {
    int nextNod, i;

    for(i = 0; i < graf[nod].size(); i++) {
        nextNod = graf[nod][i];
        if(!viz[nextNod]) {
            viz[nextNod] = true;
            dfs(nextNod);
        }
    }
}

int main() {
    int i, x, y;

    cin >> n >> m;
    for(i = 1; i <=m; i++) {
        cin >> x >> y;
        graf[x].push_back(y);
        graf[y].push_back(x);
    }

    for(i = 1; i <= n; i++) {
        if(!viz[i]) {
            viz[i] = true;
            dfs(i);
            nrCMP++;
        }
    }

    cout<<nrCMP;
}