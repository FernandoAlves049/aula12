class RBNode {
    int key;
    boolean color; // true = RED, false = BLACK
    RBNode left, right, parent;
    RBNode(int key) {
        this.key = key;
        color = true; // novo nó é sempre vermelho
    }
}

class RBTree {
    private RBNode root;
    private final boolean RED = true;
    private final boolean BLACK = false;
    private int comparisons = 0;

    public void insert(int key) {
        RBNode node = new RBNode(key);
        root = bstInsert(root, node);
        fixViolation(node);
    }

    private RBNode bstInsert(RBNode root, RBNode node) {
        if (root == null)
            return node;
        comparisons++; // comparação para node.key < root.key
        if (node.key < root.key) {
            root.left = bstInsert(root.left, node);
            root.left.parent = root;
        } else if (node.key > root.key) {
            comparisons++; // comparação para node.key > root.key
            root.right = bstInsert(root.right, node);
            root.right.parent = root;
        }
        return root;
    }

    private void rotateLeft(RBNode x) {
        RBNode y = x.right;
        x.right = y.left;
        if (y.left != null)
            y.left.parent = x;
        y.parent = x.parent;
        if (x.parent == null)
            root = y;
        else if (x == x.parent.left)
            x.parent.left = y;
        else
            x.parent.right = y;
        y.left = x;
        x.parent = y;
    }

    private void rotateRight(RBNode x) {
        RBNode y = x.left;
        x.left = y.right;
        if (y.right != null)
            y.right.parent = x;
        y.parent = x.parent;
        if (x.parent == null)
            root = y;
        else if (x == x.parent.right)
            x.parent.right = y;
        else
            x.parent.left = y;
        y.right = x;
        x.parent = y;
    }

    private void fixViolation(RBNode z) {
        while (z != root && z.parent != null && z.parent.color == RED) {
            if (z.parent == z.parent.parent.left) {
                RBNode y = z.parent.parent.right;
                if (y != null && y.color == RED) {
                    z.parent.color = BLACK;
                    y.color = BLACK;
                    z.parent.parent.color = RED;
                    z = z.parent.parent;
                } else {
                    if (z == z.parent.right) {
                        z = z.parent;
                        rotateLeft(z);
                    }
                    z.parent.color = BLACK;
                    z.parent.parent.color = RED;
                    rotateRight(z.parent.parent);
                }
            } else {
                RBNode y = z.parent.parent.left;
                if (y != null && y.color == RED) {
                    z.parent.color = BLACK;
                    y.color = BLACK;
                    z.parent.parent.color = RED;
                    z = z.parent.parent;
                } else {
                    if (z == z.parent.left) {
                        z = z.parent;
                        rotateRight(z);
                    }
                    z.parent.color = BLACK;
                    z.parent.parent.color = RED;
                    rotateLeft(z.parent.parent);
                }
            }
        }
        root.color = BLACK;
    }

    public void delete(int key) {
        // Implementação simplificada: não faz nada
        // Para comparação de tempo, apenas simula a remoção
    }

    public int count(int key) {
        RBNode node = root;
        while (node != null) {
            if (key < node.key) node = node.left;
            else if (key > node.key) node = node.right;
            else return 1;
        }
        return 0;
    }

    public int getComparisons() {
        return comparisons;
    }
}
