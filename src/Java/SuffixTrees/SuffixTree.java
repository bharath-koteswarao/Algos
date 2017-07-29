package Java.SuffixTrees;

import java.util.Scanner;

/**
 * Created by BK on 26-07-2017.
 */

class Trie {
    char data;
    boolean is_end_of_string;
    Trie[] nodes;

    public Trie(char data) {
        this.data = data;
        nodes = new Trie[26];
    }

    public Trie(char data, boolean is_end_of_string) {
        this.data = data;
        this.is_end_of_string = is_end_of_string;
        nodes = new Trie[26];
    }

    public Trie() {
        nodes = new Trie[26];
    }
}

public class SuffixTree {
    static Trie root;

    public static void main(String... args) {
        Scanner sc = new Scanner(System.in);
        root = new Trie(' ');
        String s = sc.next();
        for (int i = 0; i < s.length(); i++) {
            addIntoTrie(s.substring(i, s.length()));
        }
        System.out.println(check(sc.next()) ? "Yes" : "No");
    }

    private static boolean check(String test) {
        Trie recent = root;
        for (int i = 0; i < test.length(); i++) {
            if (recent.nodes[test.charAt(i) - 'a'] == null) {
                return false;
            }
            recent = recent.nodes[test.charAt(i) - 'a'];
        }
        return true;
    }

    private static void addIntoTrie(String substring) {
        Trie recent = root;
        for (int i = 0; i < substring.length(); i++) {
            if (recent.nodes[substring.charAt(i) - 'a'] == null) {
                recent.nodes[substring.charAt(i) - 'a'] = new Trie(substring.charAt(i));
            }
            recent = recent.nodes[substring.charAt(i) - 'a'];
        }
    }
}
