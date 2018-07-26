package transtutors;

import java.util.Scanner;

/**
 * Created by bk on 26-07-2018.
 */

class Polynomial {
    private int maxDegree;
    private int[] coeffs;

    Polynomial() {
        getInput();
    }

    private void getInput() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter max degree: ");
        this.maxDegree = sc.nextInt();
        this.coeffs = new int[maxDegree + 1];
        for (int i = 0; i < coeffs.length; i++) {
            System.out.printf("Enter coefficient of degree %d: ", i);
            coeffs[i] = sc.nextInt();
        }
    }

    public int degree() {
        return maxDegree;
    }

    public int coefficient(int x) {
        return coeffs[x];
    }

    public void changeCoefficient(int x, int y) {
        coeffs[y] = x;
    }
}
public class id_1596953 {
    public static void main(String[] __) {
        Polynomial p1 = new Polynomial();
        Polynomial p2 = new Polynomial();
    }
}
