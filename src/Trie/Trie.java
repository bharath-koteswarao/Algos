package Trie;

/**
 * Created by bk on 23-07-2017.
 */

class TrieNode {
    TrieNode[] nodes;
    char data;
    boolean is_end_of_string;

    public TrieNode(char ch) {
        data = ch;
        is_end_of_string = false;
        nodes = new TrieNode[26];
    }
}

public class Trie {
    TrieNode root = new TrieNode(' ');
    int wordCount = 0;

    public Trie() {
        root = new TrieNode(' ');
    }

    public boolean searchInTrie(String string) {
        TrieNode recent = root;
        for (int i = 0; i < string.length(); i++) {
            recent = recent.nodes[string.charAt(i) - 'a'];
            if (recent == null) return false;
        }
        return true;
    }


    public void insertInTrie(String string) {
        TrieNode recent = root;
        for (int i = 0; i < string.length(); i++) {
            if (recent.nodes[string.charAt(i) - 'a'] == null) {
                recent.nodes[string.charAt(i) - 'a'] = new TrieNode(string.charAt(i));
            }
            recent = recent.nodes[string.charAt(i) - 'a'];
            if (i == string.length() - 1) recent.is_end_of_string = true;
        }
    }

    public long getNumberOfWords() {
        countWords(root);
        return wordCount;
    }

    private void countWords(TrieNode root) {
        TrieNode recent = root;
        for (int i = 0; i < recent.nodes.length; i++) {
            if (recent.nodes[i] != null) {
                if (recent.nodes[i].is_end_of_string) wordCount++;
                else countWords(recent.nodes[i]);
            }
        }
        System.out.println(wordCount);
    }
}
