import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] visited;
    static ArrayList<Integer>[] map;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Tree tree = new Tree();
        for (int i = 0; i < n; i++)
            tree.createNode(sc.next().charAt(0), sc.next().charAt(0), sc.next().charAt(0));
        tree.preorderTraversal(tree.root);
        System.out.println();
        tree.inorderTraversal(tree.root);
        System.out.println();
        tree.postorderTraversal(tree.root);
    }

}

class Tree {

    public Node root;
    void createNode(char data, char leftData, char rightData){
        if (root == null){
            root = new Node(data);
            root.left = (leftData == '.') ? null : new Node(leftData);
            root.right = (rightData == '.') ? null : new Node(rightData);
        }
        else {
            searchNode(root, data,leftData, rightData);
        }
    }

    void searchNode(Node node, char data, char leftData, char rightData){
        if (node == null)
            return;
        else if (data == node.data)
        {
            node.left = (leftData == '.') ? null : new Node(leftData);
            node.right = (rightData == '.') ? null : new Node(rightData);
        }
        else {
            searchNode(node.left, data, leftData, rightData);
            searchNode(node.right, data, leftData, rightData);
        }
    }

    void preorderTraversal (Node node){
        if (node == null)
            return ;
        System.out.printf(String.valueOf(node.data));
        preorderTraversal(node.left);
        preorderTraversal(node.right);
    }

    void inorderTraversal (Node node) {
        if (node == null)
            return;
        inorderTraversal(node.left);
        System.out.printf(String.valueOf(node.data));
        inorderTraversal(node.right);
    }
    void postorderTraversal (Node node) {
        if (node == null)
            return;
        postorderTraversal(node.left);
        postorderTraversal(node.right);
        System.out.printf(String.valueOf(node.data));
    }
}

class Node {
    char data;
    Node left;
    Node right;

    public Node(char data) {
        this.data = data;
    }
}
