package Trie.problems;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by BK on 24-07-2017.
 */

class Tri {
    char data;
    Tri[] nodes;
    boolean isEndOfString;
    int count = 1;

    public Tri(char data) {
        this.data = data;
        nodes = new Tri[26];
        isEndOfString = false;
    }
}

public class HackerrankContacts {

    static Tri root;

    public static void main(String... args) throws IOException {
        root = new Tri(' ');
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(reader.readLine());
        for (int i = 0; i < tc; i++) {
            String s = reader.readLine();
            String[] vals = s.split(" ");
            if (vals[0].equals("add")) {
                addToTrie(vals[1]);
            } else {
                System.out.println(getCountOfWord(vals[1]));
            }
        }
    }

    private static int getCountOfWord(String val) {
        Tri recent = root;
        for (int i = 0; i < val.length(); i++) {
            recent=recent.nodes[val.charAt(i)-'a'];
            if (recent==null)return 0;
        }
        return recent.count;
    }

    private static void addToTrie(String val) {
        Tri recent = root;
        for (int i = 0; i < val.length(); i++) {
            if (recent.nodes[val.charAt(i) - 'a'] == null) {
                recent.nodes[val.charAt(i) - 'a'] = new Tri(val.charAt(i));
            } else {
                recent.nodes[val.charAt(i) - 'a'].count++;
            }
            recent = recent.nodes[val.charAt(i) - 'a'];
        }
    }
}
