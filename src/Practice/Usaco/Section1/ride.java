/*
ID: koteswa1
LANG: JAVA
TASK: ride
*/

import java.io.*;
import java.util.StringTokenizer;

public class ride {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("ride.in"));
        PrintWriter out = new PrintWriter(new FileWriter("ride.out"));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        String comet = st1.nextToken();
        String group = st2.nextToken();
        int a = prod(comet);
        int b = prod(group);
        String ans = a % 47 == b % 47 ? "GO" : "STAY";
        out.println(ans);
        out.close();
    }

    private static int prod(String st) {
        int mul = 1;
        for (int i = 0; i < st.length(); i++) {
            mul *= ((int) st.charAt(i) - (int) 'A' + 1);
        }
        return mul;
    }
}