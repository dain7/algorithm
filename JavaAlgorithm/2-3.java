import java.util.*;
  
public class Main {
  public ArrayList<String> Solution(int n, int[] a, int[] b) {
  	ArrayList<String> answers = new ArrayList<>();
   
    for (int i=0; i<n; i++) {
      int A = a[i], B = b[i];
      if ((A == 1 && B == 2) || (A == 2 && B == 3) || (A == 3 && B == 1)) answers.add("B");
      else if ((B == 1 && A == 2) || (B == 2 && A == 3) || (B == 3 && A == 1)) answers.add("A");
      else answers.add("D");
    }
    
    return answers;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    int[] a = new int[n];
    int[] b = new int[n];
    for (int i=0; i<n; i++) {
      a[i] = in.nextInt();
    }
    for (int i=0; i<n; i++) {
      b[i] = in.nextInt();
    }
    for (String answer : T.Solution(n, a, b)) {
      System.out.println(answer);
    }
    
    return ;
  }
}