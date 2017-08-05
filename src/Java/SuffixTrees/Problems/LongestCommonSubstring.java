package Java.SuffixTrees.Problems;

/**
 * Created by BK on 29-07-2017.
 */

class Trie {
    char data;
    Trie nodes[];
    int[] strings;

    public Trie(char data, int stringNumber) {
        this.data = data;
        nodes = new Trie[26];
        strings = new int[2];
        strings[stringNumber]++;
    }

    public Trie(char data) {
        this.data = data;
        nodes = new Trie[26];
    }
}

public class LongestCommonSubstring {
    static Trie root;
    static int count = 0;
    static String longestSubstring = "";

    public static void main(String... args) {
        root = new Trie(' ');
        addIntoTrie("abcd");
        count++;
        addIntoTrie("cd");
        findLongestSubstring(root);
        System.out.println(longestSubstring);
    }


    private static void findLongestSubstring(Trie root) {
        for (int i = 0; i < root.nodes.length; i++) {
            if (root.nodes[i] != null) {
                System.out.println(root.nodes[i].strings[1]);
                if (root.nodes[i].strings[0] >= 1 && root.nodes[i].strings[1] >= 1) {
                    System.out.println(root.nodes[i].data);
                    root = root.nodes[i];
                    findLongestSubstring(root);
                }
            }
        }
    }


    private static void addIntoTrie(String string) {
        for (int j = 0; j < string.length(); j++) {
            Trie recent = root;
            String substring = string.substring(j);
            for (int i = 0; i < substring.length(); i++) {
                if (recent.nodes[substring.charAt(i) - 'a'] == null) {
                    recent.nodes[substring.charAt(i) - 'a'] = new Trie(substring.charAt(i), count);
                }
                recent = recent.nodes[substring.charAt(i) - 'a'];
            }
        }
    }
}
