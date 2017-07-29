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

    public static void main(String args) {
        root = new Trie(' ');
        addIntoTrie("ababcabcdabcdeabcdef");
        count++;
        addIntoTrie("abcxyzabcdef");
        findLongestCommonSubStringInTwoStrings(root);
    }

    private static void findLongestCommonSubStringInTwoStrings(Trie root) {
        
    }

    private static void addIntoTrie(String string) {
        for (int j=0;j<string.length();j++) {
            Trie recent = root;
            String temp=string.substring(j,string.length());
            for (int i = 0; i < temp.length(); i++) {
                if (recent.nodes[temp.charAt(i)] == null) {
                    recent.nodes[temp.charAt(i) - 'a'] = new Trie(temp.charAt(i), count);
                }
                recent = recent.nodes[temp.charAt(i) - 'a'];
            }
        }
    }
}
