/**
 * Created by bk on 22-07-2017.
 */
public class BruteStringMatching {
    public static void main(String... args) {
        String pattern = "his", text = "chisking in this string";
        for (int i = 0; i < text.length(); i++) {
            int j = 0;
            while (j < pattern.length() && pattern.charAt(j) == text.charAt(i + j)) {
                j += 1;
                if (j == pattern.length()) System.out.println("matched at " + i);
            }
        }
    }
}
