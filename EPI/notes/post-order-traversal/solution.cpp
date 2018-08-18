// post-order traversal of a binary tree: left subtree, root, right subtree.

struct b_tree {
  int data;
  b_tree* left;
  b_tree* right;
}

void traversal(b_tree* n) {
  if(!n->left && !n->right) {
    cout << n;
  }
  else {
    traversal(n->left);
    traversal(n->right);
    cout << n;
  }
}

// in extended questions, we can modify the post-order traversal to simualte the bottom-up methods of building a tree and carry desired value.
void traversal(b_tree* n) {
  if(!n->left && !n->right) {
    n->value = 0;
    cout << n;
  }
  else {
    traversal(n->left);
    traversal(n->right);
    n->value = n->left->value + n->right->value;
    cout << n;
  }
}