package Hackerearth.codart;

/*
 * Created by bk on 10-02-2018 20:38
 */

import java.util.Scanner;

public class RajatsExportBusiness {

    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int cost = 500;
        long five = sc.nextLong();
        long ten = sc.nextLong();
        long fifteen = sc.nextLong();
        long twenty = sc.nextLong();
        long req = 0;
        req += (five / 4) * cost;
        five = five % 4;
        req += (ten / 2) * cost;
        ten = ten % 2;
        req += twenty * cost;
        req += (fifteen / 4) * 3 * cost;
        fifteen = fifteen % 4;
        
    }
}
