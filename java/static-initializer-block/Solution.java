import java.util.*;

public class Solution {
    static Scanner scan = new Scanner(System.in);
    static int B = scan.nextInt();
    static int H = scan.nextInt();
    static boolean flag = isNatural(B, H);
    static boolean isNatural(int B, int H) {
        try{
            if (B <= 0 || H <= 0) throw new Exception("Breadth and height must be positive"); 
            return true;
        }
        catch (Exception e){
            System.out.println(e.toString());
            return false;
        }   
    }
    public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
    }
}