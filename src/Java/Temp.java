package Java;

/**
 * Created by bk on 24-07-2017.
 */

public class Temp {
    static {

    }
    public static void main(String... args){
        int[] arr=new int[26];
        arr['z'-'a']=10;
        System.out.println(arr['z'-'a']);
    }
}
