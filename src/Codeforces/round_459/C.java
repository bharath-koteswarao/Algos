package Codeforces.round_459;

import java.util.Scanner;

public class C {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.next();
        int ans = 0;
        for (int i = 0; i < inp.length(); i++) {
            int score = 0, qm = 0;
            for (int j = i; j < inp.length(); j++) {
                if (inp.charAt(j) == '(') score += 1;
                else if (inp.charAt(j) == ')') score -= 1;
                else qm += 1;
                if (qm > 0 && qm > score) {
                    qm -= 1;
                    score += 1;
                }
                if (score < 0 && qm <= 0) break;
                else if (score < 0) {
                    score += 1;
                    qm += 1;
                }
                if ((j - i) % 2 == 1) {
                    if (qm >= score) ans += 1;
                }
            }
        }
        System.out.println(ans);
    }
}