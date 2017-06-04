#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

#define MAXN 1001
#define INF 0x3f3f3f3f

ifstream in("graf.in");

vector<int> graf[MAXN], grafT[MAXN], sortedTopNodes;
queue<int> coada;
bool fol[MAXN];
int n, m;
int dp[MAXN];

void dfsSortTop(int node) {
    int i, next;

    for(i = 0; i < graf[node].size(); i++) {
        next = graf[node][i];
        if(!fol[next]) {
            fol[next] = true;
            dfsSortTop(next);
        }
    }

    sortedTopNodes.push_back(node);
}


int main() {
    int i, j, x, y, crt, next;
    in >> n >> m;

    for(i = 1; i <= m; i++) {
        in >> x >> y;
        graf[x].push_back(y);
        grafT[y].push_back(x);
    }

    /*
     * STEP 1 -> do the sopologicalSort
     */
    dfsSortTop(1);
    reverse(sortedTopNodes.begin(), sortedTopNodes.end());

    //Take the last node and from it do the dynamic
    int last = sortedTopNodes.back();
    coada.push(last);
    while(!coada.empty()) {
        crt = coada.front(); coada.pop();

        for(i = 0; i < grafT[crt].size(); i++) {
            next = grafT[crt][i];

            if(dp[next] < dp[crt] + 1) {
                dp[next] = dp[crt] + 1;
                coada.push(next);
            }
        }
    }

    for(i = 1; i <= n; i++)
        cout<<dp[i]<<" ";

    return 0;
}