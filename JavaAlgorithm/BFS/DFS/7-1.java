
/*
DFS
*/

class Main {
    Node root;
    public void DFS(Node root) {
        if(root==null) return ;
        else {
            DFS(root.lt);
            DFS(root.rt);
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        T.DFS(n);
    }
}

