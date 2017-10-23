package Algorithms.GameTheory.Hackerrank;

import java.util.Scanner;

public class TowerBreakers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) {
            /*
                * The actual solution is XOR(G(M),G(M),G(M).....)
                * Since XOR becomes 0 if n is even 2nd player wins and first player looses.
                * If n is odd XOR doesn't become zero. So according to Sprague-Grundy Theorem this player doesn't loose.
             */
            int n = sc.nextInt(), m = sc.nextInt();
            System.out.println(m==1 || n % 2 == 0 ? 2 : 1);
        }
    }
}
