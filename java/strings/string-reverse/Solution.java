import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        StringBuilder SB_A = new StringBuilder();
        SB_A.append(A);
        if (SB_A.toString().equals(SB_A.reverse().toString()))
            System.out.println("Yes");
        else
            System.out.println("No");
        sc.close();
        
    }
}
