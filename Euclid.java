import java.util.*;
class Main{
    public static int gcd(int a ,int b){
          if(a == 0)
             return b;

          return gcd(b%a,a);

    }
    public static void main(String args[]){
       Scanner sc= new Scanner(System.in);
       System.out.println("Enter two integers-");
       int n1=sc.nextInt();
       int n2=sc.nextInt();
         int g=gcd(n1,n2);
     System.out.println("GCD is "+g);
    }
}