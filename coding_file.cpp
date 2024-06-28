//                                                     हरि ॐ तत्सत्
#define rep(i, a, b) for (ll i = a; i < b; i++)
#define ll long long
#define pyes cout << "Yes" << endl;
#define pno cout << "No" << endl;
#define checkp cout << "AJAY" << endl;
#define nln cout << endl;
#define show(a)                       \
    rep(i, 0, n) cout << a[i] << " "; \
    nln;
#define MIN(v) *min_element(v.begin(), v.end())
#define MAX(v) *max_element(v.begin(), v.end())
#define acc(x) accumulate(all(x), (ll)0)
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        string s;
        cin >> s;
        ll index = 0;
        ll common = 0;
        ll common_max = 0;
        rep(i, 0, n)
        {
            if (s[i] == s[i + 1])
            {
                common++;
            }
            else
            {
                common = 0;
            }
            if (common > common_max)
            {
                common_max = common;
                index = i + 2;
            }
        }
        ll bat = 0;
        if ((common_max + 1) % 2 == 0)
        {
            bat = index - ((common_max + 1) / 2);
        }
        else
        {
            bat = index - ((common_max) / 2);
        }
        ll a = 0;
        ll b = 0;
        cout << index << " " << common_max + 1 << " " << bat << endl;
        vector<char> sp;
        ll pq = 0;
        for (ll i = 0; i < bat; i++)
        {
            pq = sp.size();

            if (i != 0)
            {
                if (sp[pq - 2] == s[i])
                {
                    continue;
                }
            }
            sp.push_back(s[i]);
        }
        vector<char> spl;
        ll pqr = 0;
        for (ll i = bat; i < n; i++)
        {
            pqr = spl.size();
            if (i != 0)
            {
                if (spl[pqr - 2] == s[i])
                {
                    continue;
                }
            }

            spl.push_back(s[i]);
        }
        cout << sp.size() << " " << spl.size() << endl;
    }
    return 0;
}
