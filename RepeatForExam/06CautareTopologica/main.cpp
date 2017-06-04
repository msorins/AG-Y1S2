#include <fstream>
#include <vector>

using namespace std;

ifstream cin("sortaret.in");
ofstream cout("sortaret.out");

#define MAXN 50005
#define INF 0x3f3f3f3f

vector<int> graf[MAXN];
vector<int> sortTop;
int n, m, counterM;
bool fol[MAXN];

void dfsSortareTop(int nod) {
    int nextNod, i;

    for(i = 0 ; i < graf[nod].size(); i++) {
        nextNod = graf[nod][i];

        if(!fol[nextNod]) {
            fol[nextNod] = true;
            counterM++;
            dfsSortareTop(nextNod);
        }
    }

    sortTop.push_back(nod);
}

int main() {
    int i, x, y;
    cin >> n >> m;

    for(i = 1; i <= m; i++) {
        cin >> x >> y;
        graf[x].push_back(y);
    }

    for(i = 1; i <= n; i++) {
        if(!fol[i]) {
            fol[i] = true;
            dfsSortareTop(i);
        }
    }

    for(i = n - 1; i >= 0; i--)
        cout << sortTop[i] << " ";

    if(m != counterM)
        cout<<"E CICLIC";

    return 0;
}