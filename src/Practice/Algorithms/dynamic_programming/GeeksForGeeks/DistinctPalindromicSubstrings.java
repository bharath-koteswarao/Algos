package Algorithms.dynamic_programming.GeeksForGeeks;

/*
 * Created by bk on 07-12-2017 23:04
 */
/*
2
abaaa
geek
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Hashtable;
import java.util.StringTokenizer;

class FastIO {
    private BufferedReader br;
    private StringTokenizer st;

    FastIO() {
        br = new BufferedReader(new
                InputStreamReader(System.in));
    }

    public String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    public String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
}

public class DistinctPalindromicSubstrings {
    public static void main(String[] args) {
        FastIO fs = new FastIO();
        int tc = fs.nextInt();
        while (tc-- > 0) {
            String s = fs.next();
            Hashtable<String, Integer> ht = new Hashtable<>();
            for (int i = 0; i < s.length(); i++) {
                int a = i - 1, b = i + 1;
                String temp = "" + s.charAt(i);
                while (true) {
                    if (a >= 0 && b < s.length()) {
                        if (s.charAt(a) == s.charAt(b)) {
                            temp = s.charAt(a) + temp + s.charAt(b);
                            a -= 1;
                            b += 1;
                            ht.put(temp, 1);
                        } else break;
                    } else break;
                }
                b = i;
                temp = "" + s.charAt(b);
                while (true) {
                    if (b < s.length() - 1) {
                        if (s.charAt(b) == s.charAt(b + 1)) {
                            temp += s.charAt(b);
                            ht.put(temp, 1);
                            b += 1;
                        } else break;
                    } else break;
                }
            }
            for (int i = 0; i < s.length(); i++) {
                ht.put(s.charAt(i) + "", 1);
            }
            System.out.println(ht.size());
        }
    }
}
