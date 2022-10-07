package datatypes;

import java.util.*;
import static java.lang.Math.pow;

class Solution{
    public static void main(String []argh) {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++) {
            try {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-pow(2,7) && x<=pow(2,7)-1)System.out.println("* byte");
                if(x>=-pow(2,15) && x<=pow(2,15)-1)System.out.println("* short");
                if(x>=-pow(2,31) && x<=pow(2,31)-1)System.out.println("* int");
                System.out.println("* long");
                //Complete the code
            }
            catch(Exception e) {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }
        }
        sc.close();
    }
}



