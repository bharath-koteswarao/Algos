package Datastructures.Strings;

import Java.Datastructures.bk;

public class KmpAlgorithm {
static int a;
    private static int[] calculateTable(char input[]) {
        int[] op = new int[input.length];
        int j = 0, i = 1;
        op[0] = 0;
        for (i = 1; i < op.length; ) {
            if (input[i] == input[j]) {
                op[i] = j + 1;
                i++;
                j++;
            } else {
                if (j == 0) {
                    op[i] = 0;
                    i++;
                } else {
                    j = op[j - 1];
                }
            }
        }
        bk.print_int(op);
        return op;
    }

    public static void main(String... args) {
        String text = "search the string in this";
        String pattern = "ring";
        int[] prefixTable = calculateTable(pattern.toCharArray());
        int i = 0, j = 0;
        while (i < text.length() && j < pattern.length()) {
            if (text.charAt(i)==pattern.charAt(j)){
                i++;
                j++;
            } else {
                if (j==0) {
                    i++;
                } else {
                    System.out.println(prefixTable.length);
                    j=prefixTable[j-1];
                }
            }
            if (j==pattern.length()){
                System.out.println("Match found at "+(i-pattern.length()));
                System.out.println(text.substring(i-pattern.length(),i));
                System.exit(0);
            }
        }
        System.out.println("No match Found");
        System.out.println("abc");
    }
}