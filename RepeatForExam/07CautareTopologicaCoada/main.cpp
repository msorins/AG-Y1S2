#include <fstream>
#include <vector>
#include <queue>
using namespace std;

ifstream cin("sortaret.in");
ofstream cout("sortaret.out");

#define MAXN 50005
vector<int> graf[MAXN];
queue<int> coada;

int n, m;
int depinde[MAXN];

int main() {
    int i, x, y, nod;

    cin >> n >> m;
    for(i = 1; i <= m; i++) {
        cin >> x >> y;
        graf[x].push_back(y);
        depinde[y]++;
    }

    for(i = 1; i <= n; i++)
        if(!depinde[i])
            coada.push(i);

    while(!coada.empty()) {
        nod = coada.front(); coada.pop();

        for(i = 0; i < graf[nod].size(); i++) {
            depinde[graf[nod][i]]--;
            if(!depinde[graf[nod][i]])
                coada.push(graf[nod][i]);
        }

        cout<<nod<<" ";
    }

    /*
     * to see if it is really dag check depinde vector, if it has some non-null value it has an cycle
     */

    return 0;
}