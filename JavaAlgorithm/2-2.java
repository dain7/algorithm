import java.util.Scanner;
  
public class Main {
  public Integer Solution(int n, int[] arr) {
    int cnt = 1, max = arr[0];
    for (int i=1; i<n; i++) {
      if (arr[i] > max) {
        max = arr[i];
        cnt++;
      }
    }
    return cnt;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    int[] arr = new int[n];
    for (int i=0; i<n; i++) {
      arr[i] = in.nextInt();
    }
    System.out.println(T.Solution(n, arr));
    return ;
  }
}