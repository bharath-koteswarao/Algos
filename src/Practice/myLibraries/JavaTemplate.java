package myLibraries;

/**
 * Created by bk on 30-08-2018.
 */
public class JavaTemplate {
    private static String decimalDivision(int a, int b, int limit) {
        StringBuilder ans = new StringBuilder();
        ans.append(a / b);
        int re = a % b;
        while (re != 0 && limit > 0) {
            if (re < b) {
                if (ans.toString().contains(".")) re *= 10;
                else {
                    ans.append(".");
                    re *= 10;
                }
            }
            while (re < b) {
                ans.append("0");
                re *= 10;
            }
            ans.append(re / b);
            re = re % b;
            limit -= 1;
        }
        return ans.toString();
    }
}
