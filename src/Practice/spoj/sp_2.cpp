#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    int ma = 31623;
    int* sieve = (int*)malloc((ma + 1) * sizeof(int));
    for (int i = 0; i <= ma; i++) sieve[i] = 1;
    for (int i = 4; i < ma; i += 2) sieve[i] = 0;
    for (int p = 3; p * p <= ma; p += 2) {
        if (sieve[p]) {
            for (int j = p * 2; j < ma; j += p) sieve[j] = 0;
        }
    }
    vector<int> primes;
    for (int i = 2; i < ma; i++) {
        if (sieve[i]) {
            primes.push_back(i);
        }
    }
    int n;
    cin >> n;
    while (n--) {
        int l, r;
        cin >> l >> r;
        int* segment = (int*)malloc((r - l + 1) * sizeof(int));
        for (int i = 0; i < r - l + 1; i++) segment[i] = 1;
        for (int i = 0; i < primes.size() && (primes.at(i) * primes.at(i) < r); i++) {
            int prime = primes.at(i);
            int start = (l / prime) * prime;
            if (start < l) start += prime;
            for (int j = start; j <= r; j += prime) segment[j] = 0;
        }
        for (int i = l; i <= r; i++) {
            if (segment[i]) cout << i << "\n";
        }
        cout << "\n";
    }
}