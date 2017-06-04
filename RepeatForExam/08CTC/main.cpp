#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

ifstream cin("ctc.in");
ofstream cout("ctc.out");

#define MAXN 100005
#define INF 0x3f3f3f3f

vector<int> graf[MAXN], grafT[MAXN], rasp[MAXN];
stack<int> st;
bool fol[MAXN];
int n, m, ctc;

void dfs_1(int nod) {
    int nextNod, i;

    for(i = 0; i < graf[nod].size(); i++) {
        nextNod = graf[nod][i];

        if(!fol[nextNod]) {
            fol[nextNod] = true;
            dfs_1(nextNod);
        }
    }

    st.push(nod);
}

void dfs_2(int nod) {
    int nextNod, i;

    for(i = 0; i < grafT[nod].size(); i++) {
        nextNod = grafT[nod][i];

        if(!fol[nextNod]) {
            fol[nextNod] = true;
            dfs_2(nextNod);
        }
    }

    rasp[ctc].push_back(nod);
}

int main() {
    int i, j, x, y, nod;
    cin >> n >> m;

    for(i = 1; i <= m; i++) {
        cin >> x >> y;
        graf[x].push_back(y);
        grafT[y].push_back(x);
    }

    for(i = 1; i <= n; i++) {
        if(!fol[i]) {
            fol[i] = true;
            dfs_1(i);
        }
    }

    for(i = 1; i <= n; i++) {
        fol[i] = false;
    }

    while(!st.empty()) {
        nod = st.top(); st.pop();
        if(fol[nod])
            continue;

        ctc++; fol[nod] = true;
        dfs_2(nod);
    }

    cout<<ctc<<"\n";
    for(i = 1; i <= ctc; i++) {
        sort(rasp[i].begin(), rasp[i].end());
        int x = rasp[i].size();
        for(j = 0 ;j < rasp[i].size(); j++)
            cout<<rasp[i][j]<<" ";

        cout<<"\n";
    }

    return 0;
}