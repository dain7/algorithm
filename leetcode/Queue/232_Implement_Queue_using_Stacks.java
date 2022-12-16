class MyQueue {

    List<List<Integer>> queue = new ArrayList<>();

    public MyQueue() {
    }
    
    public void push(int x) {
        this.queue.add(Arrays.asList(x));
    }
    
    public int pop() {
        List<Integer> answer = this.queue.get(0);
        this.queue.remove(0);
        return answer.get(0);
    }
    
    public int peek() {
        List<Integer> answer = this.queue.get((0));
        return answer.get(0);
    }
    
    public boolean empty() {
        int len = this.queue.size();
        return len == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */