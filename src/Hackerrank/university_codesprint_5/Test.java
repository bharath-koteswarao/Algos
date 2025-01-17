package Hackerrank.university_codesprint_5;

import java.util.Vector;

class Test {
    static final int MAXN = 1000000001;

    // stores smallest prime factor for every number 
    static int spf[] = new int[MAXN];

    // Calculating SPF (Smallest Prime Factor) for every 
    // number till MAXN. 
    // Time Complexity : O(nloglogn) 
    static void sieve() {
        spf[1] = 1;
        for (int i = 2; i < MAXN; i++)

            // marking smallest prime factor for every 
            // number to be itself. 
            spf[i] = i;

        // separately marking spf for every even 
        // number as 2 
        for (int i = 4; i < MAXN; i += 2)
            spf[i] = 2;

        for (int i = 3; i * i < MAXN; i++) {
            // checking if i is prime 
            if (spf[i] == i) {
                // marking SPF for all numbers divisible by i 
                for (int j = i * i; j < MAXN; j += i)

                    // marking spf[j] if it is not  
                    // previously marked 
                    if (spf[j] == j)
                        spf[j] = i;
            }
        }
    }

    // A O(log n) function returning primefactorization 
    // by dividing by smallest prime factor at every step 
    static Vector<Integer> getFactorization(int x) {
        Vector<Integer> ret = new Vector<>();
        while (x != 1) {
            ret.add(spf[x]);
            x = x / spf[x];
        }
        return ret;
    }

    // Driver method 
    public static void main(String args[]) {
        // precalculating Smallest Prime Factor 
        sieve();
        int x = 1000000000;

        // calling getFactorization function 
        Vector<Integer> p = getFactorization(x);
        for (int i = 2; i <= 1000000000; i++) {
            getFactorization(i);
        }

        System.out.println(p);
    }
} 