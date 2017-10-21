package Usaco.Section1;/*
ID: koteswa1
LANG: JAVA
PROG: friday
*/

import java.io.*;

public class friday {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new FileReader("friday.in"));
        PrintWriter out = new PrintWriter(new FileWriter("friday.out"));
        int n = Integer.parseInt(in.readLine());
        int[] arr = new int[7];
        int start = 1900;
        while (start <= 1900 + n - 1) {
            for (int i = 1; i <= 12; i++) {
                int ans = count(start, i, 13);
                arr[ans] += 1;
            }
            start += 1;
        }
        String op = "";
        for (int i : arr) {
            op += i + " ";
        }
        out.println(op);
        out.close();
    }

    private static int count(int year, int month, int date) {
        if (month == 1) {
            month = 13;
            year -= 1;
        } else if (month == 2) {
            month = 14;
            year -= 1;
        }
        int k = year % 100;
        int j = Math.floorDiv(year, 100);
        int m = month;
        int q = date;
        return (q + (Math.floorDiv((13 * (m + 1)), 5)) + k + (Math.floorDiv(k, 4)) + Math.floorDiv(j, 4) + 5 * j) % 7;
    }
}
