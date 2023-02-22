import java.util.*;
  
public class Main {
  
  public ArrayList<Integer> Solution(int n1, int[] arr1, int n2, int[] arr2) {
    ArrayList<Integer> answer = new ArrayList<>();

    int p1=0, p2=0;
    while (p1<n1 && p2<n2) {
        if (arr1[p1] <= arr2[p2]) {
            answer.add(arr1[p1++]);
        } else {
            answer.add(arr2[p2++]);
        }
    }

    while(p1<n1) {
        answer.add(arr1[p1++]);
    }

     while(p2<n2) {
        answer.add(arr2[p2++]);
    }

    return answer;
  }
   
  public static void main(String[] args){
    Main T = new Main();

    Scanner in=new Scanner(System.in);
    int n1 = in.nextInt();
    int[] arr1 = new int[n1];

    for (int i=0; i<n1; i++) {
        arr1[i] = in.nextInt();
    }
    
    int n2 = in.nextInt();
    int[] arr2 = new int[n2];

    for (int i=0; i<n2; i++) {
        arr2[i] = in.nextInt();
    }

    for (int i : T.Solution(n1, arr1, n2, arr2)) {
        System.out.print(i+" ");
    }
    return ;
  }
}