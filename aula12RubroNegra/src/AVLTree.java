class AVLNode {
    int key, height;
    AVLNode left, right;
    AVLNode(int d) {
        key = d;
        height = 1;
    }
}

class AVLTree {
    private AVLNode root;
    private int comparisons = 0;

    private int height(AVLNode N) {
        return (N == null) ? 0 : N.height;
    }

    private int max(int a, int b) {
        return (a > b) ? a : b;
    }

    private AVLNode rightRotate(AVLNode y) {
        AVLNode x = y.left;
        AVLNode T2 = x.right;
        x.right = y;
        y.left = T2;
        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;
        return x;
    }

    private AVLNode leftRotate(AVLNode x) {
        AVLNode y = x.right;
        AVLNode T2 = y.left;
        y.left = x;
        x.right = T2;
        x.height = max(height(x.left), height(x.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;
        return y;
    }

    private int getBalance(AVLNode N) {
        return (N == null) ? 0 : height(N.left) - height(N.right);
    }

    public void insert(int key) {
        root = insertRec(root, key);
    }

    private AVLNode insertRec(AVLNode node, int key) {
        if (node == null)
            return new AVLNode(key);
        comparisons++; // comparação para key < node.key
        if (key < node.key)
            node.left = insertRec(node.left, key);
        else if (key > node.key) {
            comparisons++; // comparação para key > node.key
            node.right = insertRec(node.right, key);
        } else
            return node;
        node.height = 1 + max(height(node.left), height(node.right));
        int balance = getBalance(node);
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }
        return node;
    }

    public void delete(int key) {
        root = deleteRec(root, key);
    }

    private AVLNode deleteRec(AVLNode root, int key) {
        if (root == null)
            return root;
        if (key < root.key)
            root.left = deleteRec(root.left, key);
        else if (key > root.key)
            root.right = deleteRec(root.right, key);
        else {
            if ((root.left == null) || (root.right == null)) {
                AVLNode temp = (root.left != null) ? root.left : root.right;
                if (temp == null) {
                    temp = root;
                    root = null;
                } else
                    root = temp;
            } else {
                AVLNode temp = minValueNode(root.right);
                root.key = temp.key;
                root.right = deleteRec(root.right, temp.key);
            }
        }
        if (root == null)
            return root;
        root.height = max(height(root.left), height(root.right)) + 1;
        int balance = getBalance(root);
        if (balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);
        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        if (balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);
        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }

    private AVLNode minValueNode(AVLNode node) {
        AVLNode current = node;
        while (current.left != null)
            current = current.left;
        return current;
    }

    public int count(int key) {
        return countRec(root, key);
    }

    private int countRec(AVLNode node, int key) {
        if (node == null) return 0;
        if (key < node.key) return countRec(node.left, key);
        if (key > node.key) return countRec(node.right, key);
        return 1;
    }

    public int getComparisons() {
        return comparisons;
    }
}
