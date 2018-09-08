package Hackerrank.university_codesprint_5;

import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by bk on 08-09-2018.
 */

class Set {
    Set parent;
    String key;
    int rank;

    public Set(String key) {
        this.key = key;
        this.parent = this;
        this.rank = 1;
    }

    @Override
    public String toString() {
        return "(" + this.key + ", " + this.rank + ")";
    }
}

public class a_b_special {


    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        long a = sc.nextLong(), b = sc.nextLong();
        HashMap<String, Set> container = new HashMap<>(n + 1);
        for (int i = 1; i <= n; i++) container.put(i + "", new Set(i + ""));
        for (int i = 0; i < m; i++) {
            int p = sc.nextInt(), q = sc.nextInt();
            merge(container.get(p + ""), container.get(q + ""));
        }

    }

    private static Set findParent(Set s) {
        if (s.parent.key.equals(s.key)) return s;
        else return findParent(s.parent);
    }

    private static void merge(Set s1, Set s2) {
        Set p1 = findParent(s1);
        Set p2 = findParent(s2);
        if (!p1.key.equals(p2.key)) {
            if (p1.rank >= p2.rank) {
                p2.parent = p1;
                p1.rank += p2.rank;
                p2.rank = 1;
            } else {
                p1.parent = p2;
                p2.rank += p1.rank;
                p1.rank = 1;
            }
        }
    }
}
