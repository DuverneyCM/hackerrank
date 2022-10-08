import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        int sumLengthAB = A.length() + B.length();
        System.out.printf("%s\n", sumLengthAB);
        if (A.compareTo(B) > 0) 
            System.out.printf("Yes\n");
        else
            System.out.printf("No\n");
        String capitilizedA = A.substring(0, 1).toUpperCase() + A.substring(1).toLowerCase();
        String capitilizedB = B.substring(0, 1).toUpperCase() + B.substring(1).toLowerCase();
        System.out.printf("%s %s", capitilizedA, capitilizedB);
        sc.close();
    }
}