import java.util.*;

public class Main {
  public ArrayList<Integer> Solution(int n, int[] arr) {
    ArrayList<Integer> answers = new ArrayList();
    answers.add(arr[0]);
    for (int i=1; i<n; i++) {
      if (arr[i] > arr[i-1]) answers.add(arr[i]);
    }
    return answers;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    int[] arr = new int[n];
    
    for (int i=0; i<n; i++) {
      arr[i] = in.nextInt(); 
    }
    for (int x : T.Solution(n, arr)) {
      System.out.print(x+" ");
    }
    
    return ;
  }
}