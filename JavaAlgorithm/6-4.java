import java.util.*;
  
public class Main {
  public int[] solution(int cacheSize, int n, int[] arr) {
    int[] cache = new int[cacheSize];

    for (int x : arr) {
        int pos = -1; // 인덱스 저장
        for (int i=0; i<cacheSize; i++) {
            if (cache[i] == x) { pos = i; }
        }
        if (pos == -1) {
            for (int i=cacheSize-1; i>0; i--) {
                cache[i] = cache[i-1];
            }
        } else {
            for (int i=pos; i>=1; i--) {
                cache[i] = cache[i-1];
            }
        }
        cache[0] = x;
    }
 
  	return cache;
  }

  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    
    int cacheSize = in.nextInt();
    int n = in.nextInt();
    int[] arr = new int[n];
    
    for (int i=0; i<n; i++) {
      arr[i] = in.nextInt();
    }
    
    for (int i : T.solution(cacheSize, n, arr)) {
      System.out.println(i + " ");
    }
  }
}