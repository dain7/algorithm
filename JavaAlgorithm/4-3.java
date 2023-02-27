import java.util.*;
  
public class Main {
  public List<Integer> Solution(int day, int k, int[] arr) {
    List<Integer> answer = new ArrayList<>();
    HashMap<Integer, Integer> map = new HashMap<>();

    for (int i=0; i<k; i++) {
         map.put(arr[i], map.getOrDefault(arr[i],0)+1);
    }
    answer.add(map.size());

    for (int i=k; i<day; i++) {
        Integer a = map.get(arr[i-k]);
        if (a-1 == 0) {
            map.remove(arr[i-k]);
        } else {
            map.put(arr[i-k], map.get(arr[i-k])-1);
        }

        map.put(arr[i], map.getOrDefault(0, arr[i]+1));
        answer.add(map.size());
    }

    return answer; 
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int day = in.nextInt();
    int k = in.nextInt();
    int[] arr = new int[day];
    
    for (int i=0; i<day; i++) {
      arr[i] = in.nextInt();
    }
    
    for (Integer i : T.Solution(day, k, arr)) {
        System.out.print(i+" ");
    }
    return ;
  }
}