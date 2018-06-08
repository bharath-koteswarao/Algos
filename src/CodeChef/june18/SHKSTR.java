package CodeChef.june18;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Hashtable;
import java.util.StringTokenizer;


/**
 * Created by bk on 02-06-2018.
 */

/*

4
abcd
abce
abcdex
abcde
3
3 abcy
3 abcde
4 abcde


 */

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

class Node {
    char letter;
    String answer = "";
    Node[] nodes;

    Node(Node node) {
        this.letter = node.letter;
        this.answer = node.answer;
        this.nodes = node.nodes;
    }

    Node(char letter) {
        this.letter = letter;
        nodes = new Node[26];
    }

    @Override
    public String toString() {
        return "(" + letter + ", " + answer + ")";
    }


}

class Query {
    int lim;
    String test;

    Query(int lim, String test) {
        this.lim = lim;
        this.test = test;
    }
}

public class SHKSTR {

    public static void main(String[] __) {
        FastIO sc = new FastIO();
        int n = sc.nextInt();
        String[] inp = new String[n];
        String[] ne = new String[n];
        for (int i = 0; i < n; i++) inp[i] = sc.next();
        String min = inp[0];
        for (int i = 0; i < n; i++) {
            min = get_min(min, inp[i]);
            ne[i] = min;
        }
        Hashtable<Integer, Hashtable<String, String>> holder = new Hashtable<>();
        int q = sc.nextInt();
        for (int i = 0; i < n; i++) holder.put(i, new Hashtable<>());
        Query[] queries = new Query[q];
        for (int i = 0; i < q; i++) {
            int lim = sc.nextInt() - 1;
            String test = sc.next();
            queries[i] = new Query(lim, test);
            holder.get(lim).put(test, "");
        }
        Node root = new Node(' ');
        for (int i = 0; i < n; i++) {
            addToTrie(root, inp[i]);
            if (holder.get(i).size() > 0) {
                for (String test : holder.get(i).keySet()) {
                    String ans = getAnswer(test, root);
                    if (ans.length() == 0) ans = ne[i];
                    holder.get(i).put(test, ans);
                }
            }
        }
        for (Query query : queries) System.out.println(holder.get(query.lim).get(query.test));
    }

    private static String getAnswer(String test, Node root) {
        Node recent = root;
        for (int i = 0; i < test.length(); i++) {
            if (recent.nodes[test.charAt(i) - 'a'] == null) break;
            recent = recent.nodes[test.charAt(i) - 'a'];
        }
        return recent.answer;
    }

    private static void addToTrie(Node root, String s) {
        Node recent = root;
        for (int i = 0; i < s.length(); i++) {
            if (recent.nodes[s.charAt(i) - 'a'] == null) {
                recent.nodes[s.charAt(i) - 'a'] = new Node(s.charAt(i));
                recent.nodes[s.charAt(i) - 'a'].answer = s;
            }
            recent.nodes[s.charAt(i) - 'a'].answer = get_min(recent.nodes[s.charAt(i) - 'a'].answer, s);
            recent = recent.nodes[s.charAt(i) - 'a'];
        }
    }

    private static String get_min(String s1, String s2) {
        return s1.compareTo(s2) < 0 ? s1 : s2;
    }
}
