import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int noLine = 0;
        while (scan.hasNext()) {
            noLine++;
            System.out.println(noLine +" "+ scan.nextLine() );
        }
        scan.close();
    }
}
