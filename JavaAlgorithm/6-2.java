import java.util.*;
  
public class Main {
  public int[] solution(int n, int[] arr) {
   
    for (int i=0; i<n; i++) {
      for (int j=0; j<n-i-1; j++) {
        if (arr[j] > arr[j+1]) {
          int tmp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = tmp;
        }
      }
    }
  	return arr;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
   
    int n = in.nextInt();
    int[] arr = new int[n];
    
    for (int i=0; i<n; i++) {
      arr[i] = in.nextInt();
    }
    

    for (int i : T.solution(n, arr)) {
      System.out.println(i + " ");
    }
    
    return ;
  }
}