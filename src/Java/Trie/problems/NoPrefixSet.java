package Java.Trie.problems;

import java.util.Scanner;

/**
 * Created by BK on 25-07-2017.
 */

class Trie {
    char data;
    Trie[] nodes;
    boolean is_end_of_string;

    public Trie(char data, boolean is_end_of_string) {
        this.data = data;
        this.is_end_of_string = is_end_of_string;
        nodes = new Trie[10];
    }
}

public class NoPrefixSet {
    static Trie root = new Trie(' ', false);

    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 0; i < n; ) {
            String s = scanner.next();
            boolean isPresent = checkPresenceOfString(s);
            if (isPresent) {
                System.out.println("BAD SET\n" + s);
                System.exit(0);
            }
            boolean isValid = addIntoTrie(s);
            if (isValid) i++;
            else {
                System.out.println("BAD SET\n" + s);
                System.exit(0);
            }
        }
        System.out.println("GOOD SET");
    }

    private static boolean checkPresenceOfString(String s) {
        Trie recent = root;
        for (int i = 0; i < s.length(); i++) {
            if (recent.nodes[s.charAt(i) - 'a'] == null) return false;
            recent = recent.nodes[s.charAt(i) - 'a'];
        }
        return true;
    }

    private static boolean addIntoTrie(String str) {
        Trie recent = root;
        for (int i = 0; i < str.length(); i++) {
            if (recent.nodes[str.charAt(i) - 'a'] == null) {
                recent.nodes[str.charAt(i) - 'a'] = new Trie(str.charAt(i), i == str.length() - 1);
            } else {
                if (recent.nodes[str.charAt(i) - 'a'].is_end_of_string) return false;
            }
            recent = recent.nodes[str.charAt(i) - 'a'];
        }
        return true;
    }
}
